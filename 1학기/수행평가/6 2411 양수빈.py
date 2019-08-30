print("┏━━━━━━━ 369 게임을 시작하겠습니당 ━━━━━━━┓")

for number in range(1, 100):
    number = str(number)

    if len(number) == 1:
        if number[0] == "3" or number[0] == "6" or number[0] == "9":
            print("* 박수 짝 *")
        else:
            print(number)
    elif len(number) == 2:
        if number[0] == "3" or number[0] == "6" or number[0] == "9":
            if number[1] == "3" or number[1] == "6" or number[1] == "9":
                print("* 박수 짝짝 *")
            else:
                print("* 박수 짝 *")
        elif number[1] == "3" or number[1] == "6" or number[1] == "9":
            print("* 박수 짝 *")
        else:
            print(number)

print("┗━━━━━━━ 369 게임을 마치겠습니당. ━━━━━━━┛")