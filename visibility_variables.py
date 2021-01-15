"""
This test demonstrates concepts like protected private and public,
 these are indicated by it's underscores preceded
 private __
 protected _
 public no underscore
"""
class Test1:
    __private_Test1 = 3
    _protected_Test1 = 4
    public_Test1 = 5
    print("private is{}, protected is {}, public is {}".format(__private_Test1,_protected_Test1,public_Test1))

class Test2(Test1):
    sample_variable = "Hello!!"

class Driver:
    print(Test1.public_Test1)
    # here we are not accessing static variables
    print(Test1._protected_Test1)
    #print(Test1.__private_Test1)

