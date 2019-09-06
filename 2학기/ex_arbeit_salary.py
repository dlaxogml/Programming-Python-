#알바비 계산기
#일주일에 몇 시간 일하는지, 몇 주 일하는지, 시급이 얼마인지 입력하면 총 알바비 계산
#주 15시간 이상이면, 주휴수당(주 5일 근무로 생각하고 +1일치 지급) 지급

week_time = input("? 너는 일주일 동안에 몇 시간 일하고 있어 ? ")
week_time = int(week_time)
how_long = input("? 너는 지금까지 몇 주 정도 일했어 ? ")
how_long = int(how_long)
how_much = input("? 너는 시급을 얼마나 받고 있어 ? ")
how_much = int(how_much)
print()

if week_time >= 15:
    week_time += (week_time / 5)

salary = int(week_time) * int(how_long) * int(how_much)
print("너의 총 알바비는 ", salary, "원이야.")
print("수고했어*^^*")

