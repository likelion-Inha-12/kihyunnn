from 실습2클래스 import Acount

class saving_account (Acount):# 이자기능추가
    def __init__(self, name, amount, rate):
        super().__init__(name, amount)
        self.rate = rate

    def display_balance(self):# 잔액 확인 함수
        print(self.name + "님의 계좌 잔액은 " + str(self.amount) + "원입니다.")

    def add_interest(self):# 이자 추가 함수
        interest = self.amount * self.rate  # 이자 금액 계산
        self.amount += interest
        print(self.name + "님의 계좌에" + str(interest) + "원의 이자가 추가되었습니다.")

    def deposit(self):# 입금 함수
        self.display_balance()
        print("이자율: " + str(self.rate) )
        depositAmount = int(input("입금하실 금액을 입력해주세요 : "))
        if depositAmount <= 0:
            print("입금 금액은 양수여야 합니다.")
        else:
            self.amount += depositAmount
            print(str(depositAmount) + "원이 입금되었습니다.")
            self.add_interest()
    
    def withdraw(self): # 출금 함수
        self.display_balance()
        print("이자율: " + str(self.rate) )
        withdrawMoney = int(input("출금하실 금액을 입력해주세요 : "))
        if withdrawMoney > self.amount:
            print("출금 금액이 잔액을 초과합니다")
        elif withdrawMoney <= 0:
            print("출금 금액은 양수여야 합니다.")
        else:
            self.amount -= withdrawMoney
            print(str(withdrawMoney) + "원이 출금되었습니다.")



kihyunSavingAcount = saving_account("kihyun", 0, 0.05) # 이자 기능 계좌 객체 생성

print("Saving Account")

while(1):
    print("--------------------")
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액확인")
    print("4. 종료")
    select = int(input("메뉴를 선택해주세요 : "))
    if select == 1:
        kihyunSavingAcount.deposit()
    elif select == 2:
        kihyunSavingAcount.withdraw()
    elif select == 3:
        kihyunSavingAcount.display_balance()
    elif select == 4:
        break
    else:
        print("잘못된 입력입니다. 1~3번을 입력해주세요.")
        continue
