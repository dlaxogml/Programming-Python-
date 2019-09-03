from datetime import datetime

print('현재 날짜 시각 객체 얻기')
today = datetime.now()
print('today = datetime.now() : ', today)
print('연, 월, 일 : ', today.year, today.month, today.day)
print('시, 분, 초 : ', today.hour, today.minute, today.second)
print('요일 : ', today.weekday())
print('특정 날짜 시각 객체 만들기')
day = datetime(2019, 1, 1, 0, 0, 0)
print('day = datetime(2019, 1, 1, 0, 0, 0) : ', day)
print('2019년부터 지나온 시간 구하기')
print('today - day : ', today - day)

#태어난지 며칠인지 구하기
print("당신이 태어난지 며칠이 되었나요? ", today - datetime(2002, 1, 4, 0, 0, 0))
#올해 크리스마스 며칠 남았는지 구하기
print("올해 크리스마스가 되기까지 며칠이 남았나요? ", today - datetime(2019, 12, 25, 0, 0, 0))
#내년 내 생일 며칠 남았는지 구하기
print("내년 당신 생일이 되기까지 며칠이 남았나요? ", today - datetime(2020, 1, 4, 0, 0, 0))