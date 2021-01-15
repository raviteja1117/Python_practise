class Test_Generators:

    def call_names_for_viva(self):
        print("calling first person to exam room")
        yield "Sumanth"
        print("calling first person to exam room")
        yield "Ravindra"
        print("calling first person to exam room")
        yield "Raviteja"



class Driver:
    test=Test_Generators()
    print("Invisilator entered Exam hall,Students waiting outside and "
          "need to send them inside one by one based on ID number")
    method = test.call_names_for_viva()
    print(next(method))
    print(next(method))
    print(next(method))
