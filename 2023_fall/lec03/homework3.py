

def cancellation(list, stop_word):
    output_list = []
    
    for element in list:
        if element == stop_word:
            break 
        else:
            output_list.append(element)  
    return output_list  

    pass

def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for element in input_list:
        if element == skip_word:
            continue  
        else:
            output_list.append(element)  
    return output_list  

    pass

def my_average(input_list):
    total = 0
    for num in input_list:
        total += num  
    average = total / len(input_list)
    return average  
    pass

