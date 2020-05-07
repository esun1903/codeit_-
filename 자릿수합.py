# n의 각 자릿수의 합을 리턴
def sum_digits(n):  #321이라고하자. 
    # 코드를 작성하세요.
    if n/10 < 1: # n이 일의 자리일때 n이 return됨 
        return n
         # 321이 string으로 변경됨
    
     #s = n[0]
    s = str(n)  #n의 string값을 s로 저장  
    n = int(s)
    return int(s[0]) + sum_digits(n)
    def sum_digits(n):
    numstr = str(n)
    if len(numstr) == 1:
        return int(n)
    if len(numstr) != 1:
        return int(numstr[0]) + sum_digits(int(numstr[1:]))

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))