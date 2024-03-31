def rootCal(a,b,c): #근의 공식 함수
    root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return root1, root2


def root(a,b,c): #근의 개수에 따른 출력 함수
    if ((b**2) - 4*a*c) > 0:
        print(rootCal(a,b,c))
    elif ((b**2) - 4*a*c) == 0:
        print(rootCal(a,b,c) )
        print("중근을 갖습니다.") 
    else:
        print("실근을 갖지 않습니다.")


print("인자 a, b, c를 입력하세요:")
input_a = float(input("a: "))
input_b = float(input("b: "))
input_c = float(input("c: "))

root(input_a, input_b, input_c) #함수 호출

