import sys
minute = int(input("주차하신 시간을 입력해 주세요. "))

if minute > 60 * 24:
    sys.exit("주차 시간을 위반하셨습니다.")
if minute <= 30:
    fee = 2000
elif minute > 30:
    fee = 2000
    for i in range(31, minute+1, 10):
        fee += 1000
print("주차 요금은 " + str(fee) + " 원입니다.")