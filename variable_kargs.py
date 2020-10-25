def makeURL(**kwargs):
    my='123123123123'
    for k,v in kwargs.items():
        my=my+k+'='+v+'&'

    my=my.rstrip('&')
    print(my)

makeURL(user="psy", index="5", page="10")