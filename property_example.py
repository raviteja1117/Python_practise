class Student:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    @property
    def name(self):
        print('Getting name')
        return self._name

    @property
    def id(self):
        print("'Getting id'")
        return self._id

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @id.setter
    def id(self, value):
        print('Setting id to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

    @id.deleter
    def id(self):
        print('Deleting id')
        del self._id



p = Student('Sumanth','428')
print("The details are",p.name," and ",p.id)
p.name = 'Ravindra'
p.id = '474'
del p.name
del p.id