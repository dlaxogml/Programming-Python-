#아마스빈 주문 앱           1.음료 이름 // 2. 컵 사이즈 // 3. 얼음량 // 4. 당도 // 5. 펄
#Drink <- Coffee    // <- 상속받는다.
#      <- Bubbletea // <- 상속받는다.
#Order
#  메뉴 보여주자.
#  음료 주문하자.
#  주문한 음료 보여주자.
#  총 금액 계산하자. 
from order import Order
from file_manager import Filemanager


# 주문내역 불러오고, 보여주자
file_manager = Filemanager("history.bin")
#answer = input("주문내역을 볼까요?(y or n)")
print("sdjfoisj")
#if answer == "y":
try:
    history = file_manager.load()
    for h in history:
        print(h)
except FileNotFoundError:
    print("주문내역이 없습니다.")

o = Order()
o.order_drink()

# 주문내역 저장하자
file_manager.save(o.order_menu)