# N 자리수의 각 자리 숫자 합
num = input("숫자를 입력해주세요")
box=0
for i in num:
    box += int(i)
print(box)
