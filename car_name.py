class Car_name:
    def __init__(self,color,speed):
        self.color=color
        self.speed= speed
    def car(self,name,speed):
        print (name,self.color,'차는',self.speed,'km입니다.')
        print(speed)

redcar=Car_name('red','500')
redcar.car('volvo','300')