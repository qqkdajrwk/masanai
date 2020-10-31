def print_sum():
    global a,b 
    b=200
    result = a+b
    print('print_sum() 내부:',a,'과',b,'의 합은',result,'입니다..')
a=10
print_sum:print_sum
print_sum()
result=a+b
print('print_sum() 외부:',a,'과',b,'의 합은',result,'입니다..')