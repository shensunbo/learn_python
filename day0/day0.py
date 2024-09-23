def learn_python():
    print("hello world")

    a = 1
    b = 2
    c = a + b
    print(c)

    d = {1,2,3,4,5,6,7,8,9,10}
    print(d)

    s = "hello world"
    print(s)
    print(s[0::3])
    
def myprint(s):
    print(s)
    
if __name__ == "__main__":
    print("main")
    learn_python()
    myprint("hello")
    myprint(1)
    myprint({1,2,3,4,5})
    myprint([1,2,3,4,5])
    myprint((1,2,3,4,5))
    
    testdict = { "a":"balabala", 1:"hello" , "b": 123}
    myprint(testdict)
    myprint(testdict["a"])
    myprint(testdict[1])
    