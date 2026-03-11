class Demo:
    def __init__(self, x, y): 
        self.x = x
        self.__y = y

    def show(self):
        print(self.x)
        print(self.__y)

ob = Demo(10, 20)
ob.show()