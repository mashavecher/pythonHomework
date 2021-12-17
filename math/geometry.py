import math


def get_non_negative_int(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("numbers only.")
            continue
        if value <= 0:
            print("number must be positive")
            continue
        else:
            break
    return value


def circle(r):
    aoc = math.pi * (r**2)
    print('area of a circle is :', aoc)


def polygon(ap, p):
    aop = 1/2 * p * ap
    print('area of a polygon is :', aop)


def triangle(a, b, c):
    aot = math.sqrt(((a + b + c) / 2) * (((a + b + c) / 2) - a) * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c))
    if aot == 0:
        print('sides lengths do not match triangle shape')
    else:
        print('area of a triangle is :', aot)


def rectangle(ra, rb):
    aor = ra * rb
    print('area of a rectangle is :', aor)


def trapezium(ta, tb, th):
    aotr = 1/2 * (ta + tb) * th
    print('area of a trapezium is :', aotr)


print('What is it you want? \n'
      '1 - area of a circle \n'
      '2 - area of a polygon \n'
      '3 - area of a triangle \n'
      '4 - area of a rectangle \n'
      '5 - area of a trapezium \n'
      '6 - nothing')
answer = get_non_negative_int('What is it you want? ')

if answer == 1:
    r = get_non_negative_int('radius : ')
    circle(r)

elif answer == 2:
    p = get_non_negative_int('perimeter : ')
    ap = get_non_negative_int('apothem : ')
    polygon(ap, p)

elif answer == 3:
    a = get_non_negative_int('triangle side a : ')
    b = get_non_negative_int('triangle side b : ')
    c = get_non_negative_int('triangle side c : ')
    triangle(a, b, c)

elif answer == 4:
    ra = get_non_negative_int('rectangle side a : ')
    rb = get_non_negative_int('rectangle side b : ')
    rectangle(ra, rb)

elif answer == 5:
    ta = get_non_negative_int('trapezium side a : ')
    tb = get_non_negative_int('trapezium side b : ')
    th = get_non_negative_int('trapezium hight : ')
    trapezium(ta, tb, th)

elif answer == 6:
    print('ok than')
else:
    print('no such option')


