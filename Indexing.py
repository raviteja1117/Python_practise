input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(input_list)
print(input_list[:])
print(input_list[::])
# start : end : direct/reverse step size
print(input_list[2:6])
print(input_list[2:6:2])
print("******postiive done*****************")

print(input_list[2:6:-1])
print(input_list[9:6:-1])
print(input_list[9:2:-2])
print(input_list[9:2:-3])

test_string = "Hello! THis is Sumanth!!"
print("the reverse string is", test_string[::-1])
print("the reverse string is", test_string[::-2])

if "Sumanth" in test_string:
    print("substring exist!!")

