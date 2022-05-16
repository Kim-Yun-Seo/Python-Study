somethingInput = str(input(" 원하는 것을 입력하세요: "))

if somethingInput.isdigit() :
    print("숫자입니다.")
    
elif somethingInput.isalpha() :
    print("글자입니다.")
    
elif somethingInput.isalnum() :
    print("글자+숫자입니다.")

else :
    print("모르겠습니다.")

