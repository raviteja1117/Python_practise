class Test_main:
    def test_method(self):
        print("Hello")

    def __init__(self):
        print("Instantiated.")

    def __main__(self):
        print("main overrided.")

class Test_main1:
    Test_main()
    def testing(self):
        if __name__ == '__main__':
            Test_main().__main__()


t=Test_main1()