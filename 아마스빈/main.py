#아마스빈 주문 앱           1.음료 이름 // 2. 컵 사이즈 // 3. 얼음량 // 4. 당도 // 5. 펄
#Drink <- Coffee    // <- 상속받는다.
#      <- Bubbletea // <- 상속받는다.
#Order
#  메뉴 보여주자.
#  음료 주문하자.
#  주문한 음료 보여주자.
#  총 금액 계산하자. 
from order import Order
              
o = Order()
o.order_drink()