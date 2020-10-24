''' create a function multiplication_table. it should take a single parameter n, which determines the size of the grid to be output.'''

def multiplication_table(n):
    for x in range(1, n):
        for z in range(1, 12):
            print(f'the x is {x} and the z is {z}')



one = []
for x in range(1, 11):

    if x % 2 == 0:
        print(x)
        one.append(x)
print(len(one))
print(one)

