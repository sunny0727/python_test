print("a" + "b")
print("a" , "b")

#방법 1
print("나는 %d살입니다." %20) # %d는 정수만 입력 가능
print("나는 %s을 좋아해요" %"파이썬") # %s는 문자열을 입력
print("Apple 은 %c로 시작해요." % "A") # %s는 문자를 입력

print("나는 %s살입니다." %20)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

#방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print('저는 \'나도코딩\'입니다.')

# \\ : 문장 내에서 \
print("F:\\2017\\work\\나주시청(리뉴얼)★")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple
print("Red Apple\rPinee") # Pineepple
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple
# \t : 탭
print("Red\tApple") # Red     Apple

url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")] # my_str에서 첫번째 .이 나올때 까지 / my_str[0:5] -> 0 ~ 5 직전까지. (0,1,2,3,4)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호")) # 1
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']
# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']
# 지하철에 있는 사람을 한 명 씩 뒤에서 꺼냄
print(subway.pop()) # 하하
print(subway) # ['유재석', '정형돈', '조세호', '박명수']
print(subway.pop()) # 박명수
print(subway) # ['유재석', '정형돈', '조세호']
print(subway.pop()) # 조세호
print(subway) # ['유재석', '정형돈']
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 2

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1,2,3,4,5]
num_list.reverse()
print(num_list) # [5,4,3,2,1]
# 모두 지우기
num_list.clear()
print(num_list) # []

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)
# 리스트 확장
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]

# 사전
cabinet = {3:"유재석", 100:"김태호"} # 사전형은 {}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호
print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 5가 없기 때문에 에러
print(cabinet.get(5, "사용 가능")) # 사용 가능
print("에러 없이 진행")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새 손님
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}
# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])
#value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])
#key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])
# 목욕탕 폐점
cabinet.clear()
print(cabinet) # {}