class Heart:
    def beat(self):
        print("Heart beating...")

class Human:
    def __init__(self):
        self.heart = Heart() 

person = Human()
person.heart.beat()


