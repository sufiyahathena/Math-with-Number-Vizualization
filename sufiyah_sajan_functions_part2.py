#sufiyah sajan
#functions

# part 2

def horizontal_line(width):
    hstars = '*' * int(width)
    return hstars

def vertical_line(shift, height):
    line = ''
    left = ' ' * int(shift)
    x = 0
    while x < height:
        if x == height-1:
            line += left + '*'
        else:
            line += left + '*\n'
        x += 1
    return line

def two_vertical_lines(height, width):
    hor = ''
    x = 0
    while x < height:
        hor += '*'
        for y in range(width):
            hor += ' '
        x += 1
        if x != height:
            hor += '*\n'
        if x == height:
            hor += '*'
    return hor

w = int(input("What is the width: "))

def number_0(width):
    zero = horizontal_line(width)
    zero1 = two_vertical_lines(3, width-2)
    zero2 = horizontal_line(width)
    print(zero, end = '\n')
    print(zero1, end = '\n')
    print(zero2)

number_0(w)
print()

def number_1(width):
    print(vertical_line(width-1, 5))

number_1(w)
print()

def number_2(width):
    two = horizontal_line(width)
    two1 = vertical_line(width-1, 1)
    two2 = vertical_line(0, 1)
    print(two, end = '\n')
    print(two1)
    print(two, end = '\n')
    print(two2)
    print(two)

number_2(w)
print()

def number_3(width):
    three = horizontal_line(width)
    three1 = vertical_line(width-1, 1)
    print(three, end = '\n')
    print(three1)
    print(three, end = '\n')
    print(three1)
    print(three)

number_3(w)
print()

def number_4(width):
    four = horizontal_line(width)
    four1 = two_vertical_lines(2, width-2)
    four2 = vertical_line(width-1, 2)
    print(four1, end = '\n')
    print(four, end = '\n')
    print(four2)

number_4(w)
print()

def number_5(width):
    five = horizontal_line(width)
    five1 = vertical_line(width-1, 1)
    five2 = vertical_line(0, 1)
    print(five, end = '\n')
    print(five2)
    print(five, end = '\n')
    print(five1)
    print(five, end = '\n')

number_5(w)
print()

def number_6(width):
    six = horizontal_line(width)
    six1 = vertical_line(0, 1)
    six2 = two_vertical_lines(1, width-2)
    print(six, end = '\n')
    print(six1)
    print(six, end = '\n')
    print(six2)
    print(six)

number_6(w)
print()

def number_7(width):
    seven = horizontal_line(width)
    seven1 = vertical_line(width-1, 4)
    print(seven, end = '\n')
    print(seven1)

number_7(w)
print()

def number_8(width):
    eight = horizontal_line(width)
    eight1 = two_vertical_lines(1, width-2)
    print(eight, end = '\n')
    print(eight1)
    print(eight, end = '\n')
    print(eight1)
    print(eight)

number_8(w)
print()

def number_9(width):
    nine = horizontal_line(width)
    nine1 = two_vertical_lines(1, width-2)
    nine2 = vertical_line(width-1, 2)
    print(nine, end = '\n')
    print(nine1)
    print(nine, end = '\n')
    print(nine2)

number_9(w)
print()
