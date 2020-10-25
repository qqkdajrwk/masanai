number=[1,2,3,4,5,6,7,8,9]
dan=[2,3,4,5,6,7,8,9]
for a in dan:
    if a==3: continue
    for b in number:
        print(a,'x',b,'=',a*b)

