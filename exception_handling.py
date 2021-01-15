class Sample1:
    sample_list = [1,2,3,4,4,5,5]
    sample_string = "Hello,sumanth!!"
    def __init__(self):
        print("calling construcor")

try:
    s=Sample1()
    print(s.sample_list)
    print(s.sample_list[1])
    print(s.sample_list[8])
    Sample1.sample_string[2]= 'j'
    print(Sample1.sample_string)
    raise ("Dummy raise..")

except IndexError as error:
    print("It is index error")
    #raise ("Hello!! I AM FAILING HERE !! HAVE A LOOK!!!")
finally:
    print("Bye list!!")

try:
    Sample1.sample_string[2]= 'j'
    print(Sample1.sample_string)

except Exception as e:
    print("It is string error")
    raise ("Hello!! I AM FAILING HERE !! I am string!!!")
finally:
    print("Bye string!!")
