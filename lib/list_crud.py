def create_an_empty_list():
    return []

def create_a_list():
    return [1, 'apple', True, 3.14]

    
def add_element_to_end_of_list(input_list, element):
    input_list.append(element)
    return input_list


def add_element_to_start_of_list(input_list, element):
    input_list.insert(0, element)
    return input_list

def remove_element_from_end_of_list(input_list):
    if input_list:  # Check if the list is not empty
        input_list.pop()
    return input_list

def remove_element_from_start_of_list(input_list):
    if input_list:  # Check if the list is not empty
        del input_list[0]
    return input_list

def retrieve_first_element_from_list(input_list):
    if input_list:  # Check if the list is not empty
        return input_list[0]
    else:
        return None  # Return None if the list is empty

def retrieve_element_from_index(l, index):
    if l and 0 <= index < len(l):
        return l[index]
    else:
        return None

def retrieve_last_element_from_list(input_list):
    if input_list:  # Check if the list is not empty
        return input_list[-1]  # Use negative indexing to get the last element
    else:
        return None  # Return None if the list is empty
