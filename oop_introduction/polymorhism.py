class Polymorphism:

    def __init__(self):
        pass

    def my_sum(*args):
        print("calling my_sum")
        result = 0
        # Iterating over the Python args tuple
        for x in args:
            result += x
        return result

    print(my_sum(1, 2, 3))
    print("I am done")
    print(my_sum(1, 2, 3, 4))


poly= Polymorphism()
#poly.my_sum(1, 2, 3)

