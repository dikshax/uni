# importing pi from maths module
from math import pi


def triangle_area(base, height):
    '''
    To work the area of triangle.
        Premeters:
            base: the base of the shape.
            height: the height of the shape.

        returns:
            base * height, the area of the shape.
    '''
    return (0.5 * base * height)


def circular_area(radius):
    '''
    Working out the area of a circular shape.
        Premeters:
            radius: radius of the shape.
        Returns:
            pi * (radius **), the area of the shape.
    '''
    return pi * (radius ** 2)

def working_price(area):
    '''
    To find the price per square meter.
        Parameters:
            area: the area of the garden
        returns:
            NONE
    '''
    if area >= 300:
        print(f'The area is {round(area,3)} > 300 so the price is £35 pms')
    elif area >= 150 and area < 300:
        print(f'The area is {round(area,3)} > 150 so the price is 40 pms')
    else:
        print(f'The area is {round(area,3)} and the pricing should be £50 pms')


# Asking user for the shape of the garden
shape = input('Please enter the shape if the garden, circle or triangle: ').lower()

if shape in ['c', 'circle']: # checking if the shape is circle
    radius = float(input('Please enter the radius of the gard: '))
    area = circular_area(radius)
    working_price(area)
elif shape in ['t', 'triangle']: # checking if the shape is triangle
    base = float(input('Please enter the base of the garden: '))
    height = float(input('Please enter the height of the garden: '))
    area = triangle_area(base, height)
    working_price(area)
else:
    print(f'Please make sure your inputs matches one of what you been asked for! "{shape}" does not!!')

