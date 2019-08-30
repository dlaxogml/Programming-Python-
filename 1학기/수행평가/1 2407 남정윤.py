# 학번->학녀 학과 반 번호
num = input("학번을 입력하세요.")
if num[0] == 3:
    if num[1] == "1" or num[1] == "2":
        depart = "인터렉티브미디어"
    elif num[1] == "3" or num[1] == "4":
        depart = "뉴미디어디자인"
    elif num[1] == "5" or num[1] == "6":
        depart = "뉴미디어솔루션"
else:

    if num[1] == "1" or num[1]=="2":
        depart = "뉴미디어소프트웨어"
    elif num[1] == "3"or num[1]=="4":
        depart = "뉴미디어웹솔루션"
    elif num[1] == "5"or num[1]=="6":
        depart = "뉴미디어디자인"

print(num[0]+"학년 "+depart+"과 "+num[1]+"반 "+num[2:]+"번입니다.")