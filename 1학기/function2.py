def hello(msg = "안녕하세요");
    print(msg + "!")

    hello("오랜만이에요")
    hello("강은서")
    hello()

def hello2(name = "무명", msg = "안녕하세요"):
    print(name + "님, " + msg + "!")

hello3("김봄이", "오랫만이에요")
hello3("김소현")
hello3()

















def gugudan(dan):
    pass

gugudan(3)
gugudan()




def sum(*numbers):
    sum_value = 0
    for number in number:
        sum_value += number
    
    return sum_value

result = sum(1, 3)
print("1 + 3 =", result)
print("1 + 3 + 5 + 7 =", sum(1, 3, 5, 7))

def min(*numbers):
    min_value = numbers[0]
    for number in numbers:
        if min_value > number:
            min_value = number
    
    return min_value

print("min(1, 3_) = "., min(1, 3))
print("min(0, 3, -11) = ", min(0, 3, -11))


