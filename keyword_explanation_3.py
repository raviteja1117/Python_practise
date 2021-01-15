
variable = 1
print(id(variable))

variable_1=variable
print(id(variable_1))

variable_2=1.0
print(id(variable_2))

variable_3 = 1

if variable_2 == variable_1:
    print("Values are same")

think = True
feel = False
species_name = "Human" if think and feel else "Robot"
print(species_name)




if variable_1 is variable:
    print("Hello1")
if variable_2 is variable_1:
    print("Hello2")
if variable_3 is variable_1:
    print("Hello3")
if type(3) is int:
    print("3 is interger")

sample_string = "sumanth"
for letter in sample_string:
    print(letter, end= " ")
print("\n\n")

sample_list = ["sujatha", "sumanth"]
for element in sample_list:
    for letter in element:
        print(letter, end="\t")
    print("\n")
    
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))