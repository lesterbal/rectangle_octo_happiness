unit = 'cm'

def calculate_rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def calculate_rectangle_area(length, width):
    area = length * width
    return area

length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

perimeter_result = calculate_rectangle_perimeter(length, width)
area_result = calculate_rectangle_area(length, width)

print('The perimeter of the rectangle is {0} {1}'.format(perimeter_result, unit))
print('The area of the rectangle is {0} {1}'.format(area_result, unit))
