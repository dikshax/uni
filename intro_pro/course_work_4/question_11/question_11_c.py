from math import pi
import time


def triangle_area(base, height):
    '''
    To work the area of triangle.
        Parameters:
            base: the base of the shape.
            height: the height of the shape.

        returns:
            base * height, the area of the shape.
    '''
    return (0.5 * base * height)


def circular_area(radius):
    '''
    Working out the area of a circular shape.
        Parameters:
            radius: radius of the shape.
        Returns:
            pi * (radius **), the area of the shape.
    '''
    return pi * (radius ** 2)

def regtangular_area(length, width):
    '''
    Working out the area of a regangular shape.
        Parameters:
            length: the lenght of the shape
            width: the width of the shape
        Returns:
            length * width, the area of the shape.
    '''
    return length * width

def working_price(area):
    '''
    Working out the price according to the zise of the garden/shape.
        Parameters:
            area: area of the shape or garden
        Returns:
                price: pricing per square meter.
    '''
    if area >= 300:
        return 35
    elif area >= 150 and area < 300:
        return 40
    else:
        return 50

print('Please make sure that you enter the shape of the garden as:')
time.sleep(2)
print('regtangle')
time.sleep(2)
print('circle')
time.sleep(2)
print('or triangle')
time.sleep(1)

num_garden = int(input('How many garden are you working with: '))
total_price = 0

for x in range(1, num_garden + 1):
    shape = input('Please enter the shape of the garden: ')

    if shape == 'regtangle':
        length = float(input('Please enter the length of the garden: '))
        width = float(input('Please enter the width of the garden: '))
        area = regtangular_area(length, width)
        price_psm = working_price(area)
        total = area * price_psm
        total_price += total

    elif shape == 'triangle':
        base = float(input('Please enter the base of triangle: '))
        height = float(input('Please enter the height of triangle: '))
        area = triangle_area(base, height)
        price_psm = working_price(area)
        total = area * price_psm
        total_price += total

    elif shape == 'circle':
        radius = float(input('Please enter the radius of the garden: '))
        area = circular_area(radius)
        price_psm = working_price(area)
        total = area * price_psm
        total_price += total
    else:
        print('Make sure you enter, "regtangle", "triangle" or "circle" as your inputs!!')

final = f'The total price for all "{num_garden}" gardens is: £{round(total_price,2)}'
print(final)


