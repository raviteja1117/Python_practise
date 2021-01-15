#def len(arr):
    #print(arr)
    #return 6

def __len__(test_list):
    return 7

test_list = [1,2,3,4,5]
print(len(test_list))
print(test_list.__len__())
print(__len__(test_list))


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))

person = Person(23, 'Adam')
other = Person(23, 'Adam')
print(eq(person,other))
print(hash(person))