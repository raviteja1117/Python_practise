class Test1:
    # called with class name
    class_name="Test1"
    @classmethod
    def classmethod_Test1(cls):
        print("This is class method for Test1")
    @staticmethod
    def staticmethod_Test1():
        print("This is static method for Test1")

    # called with object name
    def non_static_method_1(self):
        print("This is non_static method")

    def __init__(self):
        self.variable_name="Test1, variable"

class Driver:
    Test1.classmethod_Test1()
    # static or class variable
    print("The class name is",Test1.class_name,"Thanks you!!")
    Test1.staticmethod_Test1()
    # Non_static method
    #Test1.non_static_method_1()
    test=Test1()
    test.non_static_method_1()
    # non_static or instance or object variable
    print("The class name is", test.variable_name, "Thanks you!!")