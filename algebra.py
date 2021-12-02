

def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value <= 0:
            print("Sorry, your response must be positive.")
            continue
        else:
            break
    return value


# so we need a function to create lists
def create_input_lists():
    lst1 = []
    print('Define values for the 1 list (positive numbers only)')
    val1 = input('numbers: ')
    lst1.append([float(value) for value in val1.split(', ')])
    lst2 = []
    print('Define values for the 2 list (positive numbers only)')
    val2 = input('numbers: ')
    lst2.append([float(value) for value in val2.split(', ')])
    return lst1, lst2

i = 3
def additional_lists():
    print('Do you need more input lists?')
    reply = input('y/n: ')
    if reply == 'y':
        lst = []
        print('Define values for the', i, 'list (positive numbers only)')
        val[i] = input('numbers: ')




print('What is it you want? \n'
      '1 - exponentiation \n'
      '2 - root extraction \n'
      '3 - extraction of the logarithm \n'
      '4 - none')

answer = get_non_negative_int('What is it you want? ')
if answer == 1:
    create_input_lists()
