input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]

print(input_list)

# comperhension syntax [iter_variabe loop condition]
# even
listhello_using_comp = [var for var in input_list if var % 2 == 0]
print(listhello_using_comp)
listhello_using_comp = [var for var in input_list if var % 2 != 0]

print(listhello_using_comp)

dict_square = {var:var ** 2 for var in input_list}
print(dict_square)

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

dict_state_info = {key: value for (key, value) in zip(state, capital)}
print(dict_state_info)

set_comperhension = {var for var in input_list if var % 2 == 0}
print(set_comperhension)