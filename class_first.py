class Calculator:
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result +=num
        return self.result

    def subt(self,num):
        self.result -+num
        return self.result

c1= Calculator()
print(c1.add(3))
print(c1.subt(11))