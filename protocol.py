from typing import Protocol

class Toy(Protocol):
    def move_around(self, moving: str) -> None:
        ...

class Barbie:
    def __init__(self,model):
        self.model = model
    
    def getModel(self):
        return self.model
    
    def move_around(self, moving: str) -> None:
        if(bool(moving) == True):
            print("The doll moved from where it was")
        else:
            print("Its where you left it")
class BouncyBall:
    def __init__(self,color):
        self.color = color
        self.position = 0

    def getColor(self):
        return self.color

    def where_is_ball(self):
        print('the ball is' ,self.position, 'feet away from you')

    def move_around(self, moving:str ) -> None:
        self.position += int(moving)

Super_ball = BouncyBall('red')
Super_ball.where_is_ball()
Super_ball.move_around('15')
Super_ball.where_is_ball()

Docter_Barbie = Barbie("doctor")
Docter_Barbie.move_around('False')