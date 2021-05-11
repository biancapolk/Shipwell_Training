'''DECORATORS'''
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

out_square = calc_square(array)

def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)