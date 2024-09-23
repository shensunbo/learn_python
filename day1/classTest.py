class Test:
    s = "hello"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("name:", self.name, " age:", self.age)
        
    @staticmethod
    def retS():
        return Test.s

#-------------------------------------------------

if __name__ == "__main__":
    print("class test")
    
    classTest = Test("bob", 123)
    classTest.show()
    classTest.name = "linda"
    classTest.age = 9
    classTest.show()
    
    classTest.gender = True;
    print(classTest.gender)
    print(Test.s)
    Test.s = "helloworld"
    print(Test.s)
    print(getattr(classTest, "gender"))
    
    print(Test.__name__)
    print(Test.__doc__)
    
    print(Test.retS())
    