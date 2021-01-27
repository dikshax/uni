

length = 12
width = 1

def find_area(length, width):
    '''
    Finding the area of the regtangle.
        Parameters:
            length: the length of the regtangle
            width: the width of the regtangle
        Returns:
            lenght * width, the area
    '''
    return length * width

area = find_area(length, width)

def working_price(area):
    '''
    Given the size of the area, working the price.
        Parameters:
            area: area size of the garden
        Returns:
            NONE
    '''
    if area >= 300:
        print(f'The area is {area} > 300 so the price is £35 pms')
    elif area >= 150 and area < 300:
        print(f'The area is {area} > 150 so the price is 40 pms')
    else:
        print(f'The area is {area} and the pricing should be £50 pms')


working_price(area)
