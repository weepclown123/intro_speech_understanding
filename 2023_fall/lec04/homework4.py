
def list_to_dict(input_list):
    '''
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`. 
    '''
    result = {}  # 创建一个空字典以存储结果
    for index, value in enumerate(input_list):
        result[index] = value  # 将列表中的元素与其索引映射到字典中
    return result




