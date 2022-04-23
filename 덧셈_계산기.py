hap = 0

while True:
    a = input("더할 첫 번째 수를 입력하세요 :")
    if a == '$' :
        break
    b = input("더할 두 번째 수를 입력하세요 :")
    hap = a+b
    print("%s + %s = %s" %(a,b,hap))

print("$를 입력해 반복문을 탈출했습니다.")

