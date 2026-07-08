
class Rectangle:
    #member variable :
    length = 0
    breadth = 0
    #method to initialize data :
    def initialize(self,l,b):
        self.length = l
        self.breadth = b
        
    #method to display data :
    def display_data(self):
        print("----Rectangle-----")
        print("length : ",self.length,"cm")
        print("breadth : ",self.breadth,"cm")

#main program:
#obejct creation:
rect = Rectangle()
rect.initialize(10,20)
rect.display_data()

