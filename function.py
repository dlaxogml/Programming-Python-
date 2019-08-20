#내장함수 연습
print(10, "의 절대값 : ", abs(10))
print(-10, "의 절대값 : ", abs(-10))

print(128, "의 2진수 : ", bin(128))
print(255, "의 2진수 : ", bin(255))
print(7, "의 8진수 : ", oct(7))
print(8, "의 8진수 : ", oct(8))
print(15, "의 16진수 : ", hex(15))
print(16, "의 16진수 : ", hex(16))

numbers = [1, 5, -2, 0, 6]
print(numbers, "중 가장 큰 값은", max(numbers))
print(numbers, "중 가장 작은 값은", min(numbers))
print(numbers, "합계는", sum(numbers))
print("2의 10승은 ", pow(2, 10))

strings = ["강은서", "슈퍼주니어", "율무", "박성래"]
print(strings, "중 가장 큰 값은", max(strings))
print(strings, "중 가장 작은 값은", min(strings))
#print(strings, "합계는", sun(strings))
#print("강은서의 10승은 ", pow("강은서", 10))

pi = 3.141592
print(pi, "의 반올림은", round(pi))
print(pi, "의 소수점 0자리 반올림은", round(pi, 0))
print(pi, "의 소수점 1자리 반올림은", round(pi, 1))
print(pi, "의 소수점 2자리 반올림은", round(pi, 2))
print(pi, "의 소수점 3자리 반올림은", round(pi, 3))
print(pi, "의 소수점 4자리 반올림은", round(pi, 3))
print(5.5, "의 반올림은 ", round(5.5))
print(-5.5, "의 반올림은 ", round(-5.5))

# user_name = input("이름은")
# user_age = input("나이는")
# print(user_name + "님! 나이는 " + str(user_age) + "세군요!")

# say = "{}님! 나이는 {}세군요!"
# print(say.format(user_name, user_age))
# say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요!"
# print(say.format(user_name, user_age))
# say = "{name}님! 나이는 {age}세군요! {age}세라니 놀라워요!"
# print(say.format(name = user_name, age = user_age))

py = "3.14159"
print("문자열 출력: ", pi)
print("실수 변환 출력: ", float(pi))
print((pi) + 1000)
year = "2018"
print("올해 연도: ", year)
print("100년 뒤는 ", int(year)+100, "년입니다.")
print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
print("올해는 " + str(year) + "년입니다.")

list = ['d', 'c', 'a', 'b']
list.reverse()
print("리스트 항목 순서 뒤집기", list)
list.sort()
print("리스트 항목 정렬하기", list)
list.sort(reverse = True)
print("리스트 항목 역정렬하기", list)
for index, value in enumerate(list):
    print("인덱스", index, "위치의 값은 ", value)

str + "나는 문자열이다"
print(str)
n = 3
print(str(n))
