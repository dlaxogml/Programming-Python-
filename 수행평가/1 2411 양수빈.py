myNumber = input("학번을 입력해 주세요 : ")

if myNumber[0] == "3":
    if myNumber[1] == "1" or myNumber[1] == "2":
        major = "인터랙티브미디어과"
    elif myNumber[1] == "3" or myNumber[1] == "4":
        major = "디자인과"
    else:
        major = "솔루션과"
else:
    if myNumber[1] == "1" or myNumber[1] == "2":
        major = "뉴미디어소프트웨어과"
    elif myNumber[1] == "3" or myNumber[1] == "4":
        major = "뉴미디어솔루션과"
    else:
        major = "뉴미디어디자인과"

print(myNumber[0] + "학년 " + major + " " + myNumber[2:] + " 번입니다.")