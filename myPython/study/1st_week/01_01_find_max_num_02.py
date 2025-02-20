array = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    max_num = 0
    
    for compared_num in array:
        if compared_num > max_num:
            max_num = compared_num
    
    return max_num

print(find_max_num(array))