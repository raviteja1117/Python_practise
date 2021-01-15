class Person:

    def __init__(self, name,name1):
        self._name = name
        self._name1=name1

    def get_name(self):
        print('Getting names')
        return [self._name,self._name1]

    def set_name(self, value):
        print('Setting names to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting names')
        del self._name
        del self._name1

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')


p = Person('Adam','Sumath')
print(p.name)
print("************")
print(p.name1)
p.name = 'John'
print(p.name1)
p.name1 = 'ravi'
del p.name
del p.name1