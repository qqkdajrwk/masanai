def get_sum(a,b):
    result=a+b
    return result

#키워드 인자
n1=get_sum(10,20)
print('10과 20의 합 =', n1)

n2=get_sum(100,200)
print('10과 20의 합 =', n2)

#위치 인자
def get_sum_1(a=1,b=2):
    result=a+b
    return result

print(get_sum_1(5))

# #섞어국밥
# def get_sum_2(b,d,a=1,c=3):

#     result_1=a+b
#     result_2=c+d
#     return result_1, result_2

# n4=get_sum_2(5,6)
# print(n4)

# #가변인자
