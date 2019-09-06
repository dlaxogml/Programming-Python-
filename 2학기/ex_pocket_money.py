#총점 / 평균 구하기(국어, 영어, 수학, JAVA, PYTHON, JSP)
#용돈 구하기
#90점 이상 => 100000원, 80점 이상 => 90000원, 70점 이상 => 80000원, 60점 이상 => 70000원, 50점 이상 => 60000원, 그 외 미만 => 50000원
print("<~ 국어 점수 입력하세요 ~> ")
korean = int(input())
print("<~ 영어 점수 입력하세요 ~> ")
english = int(input())
print("<~ 수학 점수 입력하세요 ~> ")
math = int(input())
print("<~ JAVA 점수 입력하세요 ~> ")
java = int(input())
print("<~ PYTHON 점수 입력하세요 ~> ")
python = int(input())
print("<~ JSP 점수 입력하세요 ~> ")
jsp = int(input())
print()

total = korean + english + math + java + python + jsp
print("시험 점수 총점 => ", total)

average = total / 6
print("시험 점수 평균 => ", round(average, 2))

if(average >= 90):
    print("!! 용돈 100000원을 획득하셨습니다 !!")
elif(average >= 80):
    print("!! 용돈 90000원을 획득하셨습니다 !!")
elif(average >= 70):
    print("!! 용돈 80000원을 획득하셨습니다 !!")
elif(average >= 60):
    print("!! 용돈 70000원을 획득하셨습니다 !!")
elif(average >= 50):
    print("!! 용돈 60000원을 획득하셨습니다 !!")
else:
    print("!! 용돈 50000원을 획득하셨습니다 !!")