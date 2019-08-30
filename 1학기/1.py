# print(hex(10)) 
# print(max([1, -1, -2]))
# print(pow(3, 4))
# print(round(2.55, 1))

def star():
    pass

star()
star()
star()


















def rolling_dice(pip, repeat):
    for r in range(1, reqeat + 1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린 결과 ", r, " : ", n)

#rolling_dice(2)
rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0)
rolling_dice(20, -3)


def 안녕(*args):
    for a in args:
        print("안녕, ", a)

안녕  = ("가연아", "수빈아", "정윤아")



def star():

star("음", 3)

star("할", 1, 2, 3)




#p118 혼자해보기
def star(mark, repeat, space, space_repeat, line):
        for i in range(1, line):
                string = (mark * repeat)
                for j in range(2, repeat)
                        string += (space * space_repeat) + (mark * repeat)
                print(string)

star("*", 2, "+", 3, 5)
print("-------------------------")
star(mark = "*", repeat = 2, space = "+", space_repeat = 3, line = 5)

def star2(mark, repeat, space, space_repeat, line):
        string = mark *