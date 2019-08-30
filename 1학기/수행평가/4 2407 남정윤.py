#주차요금 계산
import sys

time = int(input("몇 분동안 주차했나요?"))

if time > 60*24:
    sys.exit("주차 시간 위반")

if time <= 30:
    money = 2000

else:
    money = 2000+1000*(((time-31)//10)+1)

if money >= 25000:
    sys.exit("25000원 이상 받지 않습니다.")


print("주차요금은 {}원입니다.".format(money))