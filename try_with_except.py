try:
    a,b = input('Please enter two number : ').split()
    # c=int(a)/int(b)
    c=(a)/(b)
    print(c)
except Exception as e:
    print('please enter it correctly',e)
