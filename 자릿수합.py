# n의 각 자릿수의 합을 리턴
def sum_digits(n):  #321이라고하자. 
    # 코드를 작성하세요.
    if n/10 < 1: # n이 일의 자리일때
        return n
         # 321이 string으로 변경됨
    
     #s = n[0]
    s = str(n)
    print(int(s[0]))
    return 0
    
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))