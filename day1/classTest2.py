class Base:
    attr = "hello"
    def __init__(self, name, age):
        print("Base init")
        self.name = name
        self.age = age
    def show(self):
        print("base name:", self.name, " age:", self.age)

class subClass(Base):
    __attr = "hello hello"
    def __init__(self, name, age):
        print("subClass init")
        Base.__init__(self, name, age)

    def show(self):
        print("sub name:", self.name, " age:", self.age)
        Base.show(self)
        print(self.__attr)
        print(self.__show())

    def __show(self):
        print(self.__attr + " __show")
    

        
        
#-------------------------------------------------

if __name__ == "__main__":
    sub = subClass("bob", 123)
    sub.show()
    print(sub.attr)
    sub.age = 100
    sub.name = "linda"
    sub.show()
    # print(sub.__attr)

