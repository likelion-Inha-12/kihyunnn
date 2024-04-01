class Acount: # 입금, 출금, 잔액확인 기능을 가진 계좌 클래스
    def __init__(self, name, amount): # 생성자
        self.name = name
        self.amount = amount

    def display_balance(self): # 잔액 확인 함수
        print(self.name + "님의 계좌 잔액은 " + str(self.amount) + "원 입니다.")

    def deposit(self): # 입금 함수
        depositAmount = int(input("입금하실 금액을 입력해주세요 : "))
        if depositAmount <= 0: # 입금 금액이 0보다 작거나 같을 경우, 안내 메시지
            print("입금 금액은 양수여야 합니다.")
        else: # 입금 금액이 0보다 클 경우, 정상적으로 기능 작동
            self.amount += depositAmount # 계좌 잔액에 입금 금액을 더함
            print(str(depositAmount) + "원이 입금되었습니다.")

    def withdraw(self):
        withdrawMoney = int(input("출금하실 금액을 입력해주세요 : "))
        if withdrawMoney > self.amount: # 출금 금액이 잔액을 초과할 경우, 안내 메시지
            print("출금 금액이 잔액을 초과합니다")
        elif withdrawMoney <= 0: # 출금 금액이 0보다 작거나 같을 경우, 안내 메시지
            print("출금 금액은 양수여야 합니다.")
        else: # 출금 금액이 0보다 클 경우, 정상적으로 기능 작동
            self.amount -= withdrawMoney # 계좌 잔액에서 출금 금액을 뺌
            print(str(withdrawMoney) + "원이 출금되었습니다.")


if __name__ == "__main__": # 메인 함수
    kihyunAcount = Acount("kihyun", 0) # 계좌 객체 생성
    print("기본기능 Acount")
    while(1): 
        print("--------------------")
        print("1. 입금")
        print("2. 출금")
        print("3. 잔액확인")
        print("4. 종료")
        select = int(input("메뉴를 선택해주세요 : "))
        if select == 1:
            kihyunAcount.deposit()
        elif select == 2:
            kihyunAcount.withdraw()
        elif select == 3:
            kihyunAcount.display_balance()
        elif select == 4: # 종료문 선택시 프로그램 종료
            break
        else: #1~3번외에 번호 입력시 다시 반복
            print("잘못된 입력입니다.1~3번을 입력해주세요.")
            continue
