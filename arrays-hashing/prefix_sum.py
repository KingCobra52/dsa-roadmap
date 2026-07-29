from typing import List

def build_prefix(input_list: List[int]):
    prefix_list = [0] * (len(input_list) + 1)
    for i in range(len(input_list)):
        prefix_list[i + 1] = prefix_list[i] + input_list[i]
    return prefix_list
