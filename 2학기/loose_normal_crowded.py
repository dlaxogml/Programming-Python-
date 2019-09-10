# 버스 여유, 보통, 혼잡 알리미
# 탑승객, 하차객 입력받아서 분석하기
# 0 <= 탑승객 < 10 : 여유
# 10 <= 탑승객 < 20 : 보통
# 20 <= 탑승객 : 혼잡

sum = 0
while True:
    in0 = input("탑승객(-1 : 끝) => ")
    if in0 == "-1":
        break
    in0 = int(in0)

    out = input("하차객 : ")
    out = int(out)
    sum += in0 - out
    print()

print("버스에 있는 인원 => ", sum)

if 0 <= sum < 10:
    print("## 버스는 지금 여유입니다 ##")
elif 10 <= sum < 20:
    print("## 버스는 지금 보통입니다 ##")
else:
    print("## 버스는 지금 혼잡입니다 ##")