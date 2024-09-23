import time

def timeTest():
    print(time.time())
    print(time.localtime(time.time()))
    print(time.localtime(123456789))
    print(time.asctime(time.localtime(time.time())))

def funcTest(name = "none", age = 0):
    print("name:", name, " age:", age)
    
def returnTest(x):
    return x

def returnTest2(key, value):
    return {key: value}
    
def returnTest3(key, value):
    return key, value

def returnTest4(key, value):
    return [key, value]

def returnTest5(key, value):
    return{key, value}

#-------------------------------------------------

if __name__ == "__main__":
    # timeTest();
    funcTest("hello", 123)
    funcTest(age = 666, name = "bob")
    funcTest("linda")
    funcTest(age = 9)
    
    sum = lambda x, y: x + y
    print(sum(1, 2))
    
    print(returnTest(1))
    print(returnTest("hello"))
    print(returnTest([1,2,3,4,5]))
    
    print(returnTest2("hello", 123))
    print(returnTest3("hello", 123))
    print(returnTest4("hello", 123))
    print(returnTest5("hello", 123))
    
    
    
    