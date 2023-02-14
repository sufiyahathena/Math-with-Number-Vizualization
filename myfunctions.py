#sufiyah sajan
#functions

# All of my functions

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

def number_0(width):
    zero = horizontal_line(width)
    zero1 = two_vertical_lines(3, width-2)
    zero2 = horizontal_line(width)
    print(zero, end = '\n')
    print(zero1, end = '\n')
    print(zero2)

def number_1(width):
    print(vertical_line(width-1, 5))

def number_2(width):
    two = horizontal_line(width)
    two1 = vertical_line(width-1, 1)
    two2 = vertical_line(0, 1)
    print(two, end = '\n')
    print(two1)
    print(two, end = '\n')
    print(two2)
    print(two)

def number_3(width):
    three = horizontal_line(width)
    three1 = vertical_line(width-1, 1)
    print(three, end = '\n')
    print(three1)
    print(three, end = '\n')
    print(three1)
    print(three)

def number_4(width):
    four = horizontal_line(width)
    four1 = two_vertical_lines(2, width-2)
    four2 = vertical_line(width-1, 2)
    print(four1, end = '\n')
    print(four, end = '\n')
    print(four2)

def number_5(width):
    five = horizontal_line(width)
    five1 = vertical_line(width-1, 1)
    five2 = vertical_line(0, 1)
    print(five, end = '\n')
    print(five2)
    print(five, end = '\n')
    print(five1)
    print(five, end = '\n')

def number_6(width):
    six = horizontal_line(width)
    six1 = vertical_line(0, 1)
    six2 = two_vertical_lines(1, width-2)
    print(six, end = '\n')
    print(six1)
    print(six, end = '\n')
    print(six2)
    print(six)

def number_7(width):
    seven = horizontal_line(width)
    seven1 = vertical_line(width-1, 4)
    print(seven, end = '\n')
    print(seven1)

def number_8(width):
    eight = horizontal_line(width)
    eight1 = two_vertical_lines(1, width-2)
    print(eight, end = '\n')
    print(eight1)
    print(eight, end = '\n')
    print(eight1)
    print(eight)

def number_9(width):
    nine = horizontal_line(width)
    nine1 = two_vertical_lines(1, width-2)
    nine2 = vertical_line(width-1, 2)
    print(nine, end = '\n')
    print(nine1)
    print(nine, end = '\n')
    print(nine2)

def plus(width):
    vert = vertical_line(width//2, 2)
    hors = horizontal_line(width)
    print(vert)
    print(hors, end = '\n')
    print(vert)

def minus(width):
    print(horizontal_line(width))

def check_answer(num1, num2, ans, op):
    if op == '+':
        if num1 + num2 == ans:
            return True
        else:
            return False
    elif op == '-':
        if num1 - num2 == ans:
            return True
        else:
            return False
