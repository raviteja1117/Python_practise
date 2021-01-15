from Test1 import method1
from Test1 import Test_class_1


class Test2:
    def method2(self):
        print("Method 2 in Test2")
        test1= Test_class_1()
        test1.class_Test1_method1()
        method1()

test2 = Test2()
test2.method2()