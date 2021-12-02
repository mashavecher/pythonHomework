import math


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


print('What is it you want? \n'
      '1 - area of a circle \n'
      '2 - area of a polygon \n'
      '3 - area of a triangle')
answer = get_non_negative_int('What is it you want? ')
if answer == 1:
    radius = get_non_negative_int('radius : ')
    def circle(r):
        aoc = math.pi * (r**2)
        print('area of a circle is :', aoc)
    r = radius
    circle(r)