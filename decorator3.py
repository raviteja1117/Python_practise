def make_him_bride_groom(func):
    def inner():
        print("Apply him Lot of makeup!!!")
        func()
    return inner

@make_him_bride_groom
def enter_marriage_venue():
    print("Person entered for his marriage...")

enter_marriage_venue()

print("***************************************************************")

enter_marriage_venue1 = make_him_bride_groom(enter_marriage_venue)
enter_marriage_venue1()

