text = "Hello, World!"

# count # 특정 문자의 개수
count = text.count("l")
print(count)  # 3

# find # 특정 문자열이 처음 나오는 위치
position1 = text.find("World")
print(position1)  # 7
position2 = text.find("wow")  # 없을 경우 -1 return
print(position2)  # -1

# index # 특정 문자열이 처음 나오는 위치
try:
    position3 = text.index("wow")
    print(position3)
except ValueError:  # 없을 경우 ValueError
    print("없어")

# join # 특정 문자열 기준 다른 문자열들을 합쳐줌
fruits = ["Strawberry", "pear", "grape"]
joined_fruits = "_".join(fruits)
print(joined_fruits)  # Strawberry_pear_grape

# upper # 소문자를 대문자로
upper_text = text.upper()
print(upper_text)  # HELLO, WORLD!

# lower # 대문자를 소문자로
lower_text = text.lower()
print(lower_text)  # hello, world!

# replace # 문자열 내에서 특정 문자열을 다른 문자열로 바꿔줌
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Hello, Python!

# split # 문자열을 특정 문자 기준으로 나눠줌
split_text = text.split(",")
print(split_text)  # ['Hello', ' World!'] # 결과는 리스트형태

# len # 리스트의 길이를 반환
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

# del # 리스트에서 특정 요소를 삭제
del numbers[4]
print(numbers)  # [1, 2, 3, 4]

# append # 리스트의 맨 뒤에 새로운 요소를 추가
numbers.append(7)
print(numbers)  # [1, 2, 3, 4, 7]

# sort # 리스트를 오름차순으로 정렬
numbers = [3, 4, 5, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]
numbers.sort(reverse=True)  # 내림차순
print(numbers)  # [5, 4, 3, 2, 1]

# reverse # 리스트의 요소 순서를 반대로
numbers.reverse()
print(numbers)  # [1, 2, 3, 4, 5]

# index # 리스트에서 특정 요소의 인덱스를 반환
print(numbers.index(3))  # 2

# insert # 리스트의 특정 위치에 요소를 삽입
numbers.insert(3, 2)
print(numbers)  # [1, 2, 3, 2, 4, 5]

# remove # 리스트에서 특정 요소를 제거
numbers.remove(3)
print(numbers)  # [1, 2, 2, 4, 5]

# pop # 리스트에서 마지막 요소를 빼낸 뒤 삭제
numbers.pop()
print(numbers)  # [1, 2, 2, 4]

# count # 리스트에서 특정 요소의 개수를 셈
print(numbers.count(2))  # 2

# extend # 리스트를 확장하여 새로운 요소들을 추가
numbers.extend([5, 6, 7])
print(numbers)  # [1, 2, 2, 4, 5, 6, 7]
numbers += [8, 9, 10]  # += 연산자와 같다
print(numbers)  # [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]

# 딕셔너리 만들기
empty_dict = {}
my_dict = {"grape": 1, "orange": 2, "apple": 3}

# 딕셔너리 쌍 추가
my_dict["banana"] = 5
print(my_dict)  # {'grape': 1, 'orange': 2, 'apple': 3, 'banana': 5}

# del # 딕셔너리에서 특정 요소를 삭제
del my_dict["apple"]
print(my_dict)  # {'grape': 1, 'orange': 2, 'banana': 5}

# 특정 key의 value 얻기
print(my_dict["grape"])  # 1
# print(my_dict["pear"])  # KeyError

# keys # 모든 key를 리스트로
print(my_dict.keys())  # dict_keys(['grape', 'orange', 'banana'])
print(list(my_dict.keys()))  # ['grape', 'orange', 'banana']

# values # 모든 value를 리스트로
print(my_dict.values())  # dict_values([1, 2, 5])
print(list(my_dict.values()))  # [1, 2, 5]

# items # 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
# dict_items([('grape', 1), ('orange', 2), ('banana', 5)])
print(my_dict.items())
print(list(my_dict.items()))  # [('grape', 1), ('orange', 2), ('banana', 5)]

# clear # 딕셔너리의 모든 요소를 삭제
person = {'name': 'bob', 'age': 20, 'gender': 'male'}
# person.clear()
print(person)  # {}

# get # 딕셔너리에서 지정한 키에 대응하는 값 반환
print(person.get('name'))  # bob
print(person.get('age'))  # 20
print(person.get('gender'))  # male
print(person.get('email'))  # None # key가 없음

email = person.get('email', 'unknown')  # 기본값 지정
print(email)  # unknown

# in # 해당 키가 딕셔너리 안에 있는지 확인
print('name' in person)  # True
print('email' in person)  # Flase
