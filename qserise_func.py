import os
import requests
import socket
import sys
import urllib.request, json
from urllib.parse import quote
import time

def log_file(filename):
    global logFile, log_formatter
    logFile = filename

def log_print(obj,msg):
    global lastlog
    import logging
    from logging.handlers import RotatingFileHandler

    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
    my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024,   backupCount=2, encoding="UTF-8", delay=0)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.INFO)
    logger = logging.getLogger('root')
    if len(logger.handlers) > 0:
        pass
    else:
        logger.setLevel(logging.INFO)
        logger.addHandler(my_handler)
    print (obj, ":", msg )
    logger.info(obj+ ":"+ msg )

def sleep(sec):
    from time import sleep
    import sys

    for i in range(sec):
        sys.stdout.write('\r')
        sys.stdout.write("재접속 대기중 %-10s  " % ('.'*i))
        sys.stdout.flush()
        time.sleep(1)
    print(".")

class IRC:
    irc = socket.socket()
    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        self.irc.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))

    def send_command(self, command):
        global config
        try:
            self.irc.send(bytes(command+ "\n", "UTF-8"))
        except ConnectionResetError:
            log_print("Yubi community server",self.config_server+ " 커뮤니티 서버에서 연결을 종료하였습니다.")
            self.reconnect()
        except ConnectionAbortedError:
            log_print("Yubi community server",self.config_server+ " 커뮤니티 서버 연결오류.")
            self.reconnect()
        except Exception as ex:
            log_print("Yubi community server",self.config_server+ " 알수없는 오류" + ex)
            self.reconnect()

    def connect(self, server='', port='', chan='', botnick='', botpass='', botnickpass=''):
        global channel
        if server != "":
            self.config_server = server
            self.config_port = port
            self.config_channel = chan
            self.config_botnick = botnick
            self.config_botnickpass = botnickpass
            self.config_botpass = botpass

        channel=self.config_channel
        #print("Connecting to: " + self.config_server)
        try:
            self.irc.connect((self.config_server, self.config_port))
        except Exception as ex:
            log_print("Yubi community server",str(ex))
            try:
                if self.irc.getpeername()!="":
                    print("소켓을 닫습니다.")
                    self.irc.close()
                    self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except:
                pass
            self.reconnect()
        log_print("Yubi community server", " Connected to: " + self.config_server)
        self.irc.send(bytes("USER " + self.config_botnick + " 0 * :" + self.config_botnick + "\n", "UTF-8"))
        self.irc.send(bytes("NICK " + self.config_botnick + "\n", "UTF-8"))

    def reconnect(self):
        log_print("Yubi community server", self.config_server + " re connected to: " + self.config_server)
        sleep(15)
        self.connect(self.config_server, self.config_port, self.config_channel, self.config_botnick, self.config_botpass, self.config_botnickpass)

    def get_response(self):

        try:
            resp = self.irc.recv(2040).decode("UTF-8")
        except:
            resp = ''

        if resp.find('End of MOTD command') != -1:
            log_print("Yubi community server", self.config_server + " connect!!  ")
            self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))
        if resp.find('Nickname already in use') != -1:
            log_print("Yubi community server", self.config_server + " device id already in use!!  ")
            self.reconnect()
            sys.exit()
        if resp.find('PING') != -1:
            self.irc.send(bytes('PONG ' + '\r\n', "UTF-8"))
        return resp


# 로그인 ===================
def login(api_url, device_id, device_pwd):
    # command=login&data1={디바이스 아이디}&data2={디바이스 비밀번호}

    param = "command=login&data1=" + device_id + "&data2=" + device_pwd
    api_url = api_url + '?' + param
    try:
        with urllib.request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
            if data["StatResult"]!='True':
                log_print("Yubi Auth server", " 아이디 또는 비밀번호 오류 입니다 ")
                sys.exit()
            else:
                return data
    except Exception as ex:
            log_print("Yubi Auth server", " connect error " + ex)
            sys.exit()
# API 제어 ===================
def openapi(command, data1, data2, data3, log, config):
    # command={resultvalue}&data1={idx}&data2={complete | error | pass}&log={오류메세지}

    param = "command=" + command + "&data1=" + data1 + "&data2=" + data2 + "&data3=" + data3 + "&log=" + quote(log)
    api_url = str(config['DEFAULT']['api_url']) + '?' + param

    log_print("Yubi openAPI server", " Query : " + param)
    try:
        with urllib.request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
            print(data["StatResult"])
    except Exception as ex:
            log_print("Yubi openAPI server", " connect error " + ex)

            return "False"

# 파일 다운로드
def download_file(link,file_name,idx):
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush
    print(".")