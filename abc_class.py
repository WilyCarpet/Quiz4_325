from abc import ABC, abstractmethod

class Toy(ABC):

    @abstractmethod
    def move_around(self, moving):
        pass

class Barbie(Toy):
    def __init__(self,model):
        self.model = model
    
    def getModel(self):
        return self.model
    
    def move_around(self, moving):
        if(moving == True):
            print("The doll moved from where it was")
        else:
            print("Its where you left it")

class BouncyBall(Toy):
    def __init__(self,color):
        self.color = color
        self.position = 0
    
    def getColor(self):
        return self.color

    def where_is_ball(self):
        print('the ball is' ,self.position, 'feet away from you')
    
    def move_around(self, moving):
        self.position += moving



Super_ball = BouncyBall('red')
Super_ball.where_is_ball()
Super_ball.move_around(5)
Super_ball.where_is_ball()

Docter_Barbie = Barbie("doctor")
Docter_Barbie.move_around(True)
