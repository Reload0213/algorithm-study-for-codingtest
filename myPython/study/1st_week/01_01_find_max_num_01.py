array = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    #  flag 방식
     for number in array:
        is_max_num = True
        for compare_number in array:
            if number < compare_number:
                is_max_num = False
        if is_max_num:
            return number

print(find_max_num(array))