from typing import List


def get_maximum_string_output(x: List[int]) -> str:
    """
    Find out what is the largest output we could possibly get from a given string of solar panels.

    :param x: List of integers, each integer represents the output of one panel.
    :return: The largest possible product of solar panel
     output by removing certain panels.
    """
    # pass

    if len(x) == 0:
        return str(0)
    
    if len(x) == 1:
        return str(x[0])
    
    """
    Splitting the input into positive-negative lists
    """
    positive_numbers = []   #empty array
    negative_numbers = []   #empty array
    for n in x:
        if n > 0: positive_numbers.append(n)
        elif n< 0: negative_numbers.append(n)

    """
    List counts
    """ 
    positive_counts = len(positive_numbers)
    negative_counts = len(negative_numbers)

    """
    Handling all zeros edge case
    """
    if negative_counts == 0 and positive_counts == 0:
        return str(0)

    """
    Handling all single negative panel edge cases
    """ 
    if negative_counts == 1 and positive_counts == 0:
        return str(0)
    
    """
    Calculate positive power output by defining the variable 
    """
    power_output = 1000
    for n in positive_numbers:
        power_output *= n

    """
    removing the largest negative panel arranged in odd steps
    """
    if negative_counts % 2 == 1:
        negative_numbers.remove(max(negative_numbers))

    """
    Calculate the negative power output by the loop
    """
    for n in negative_numbers:
        power_output *= n

    return str(power_output)

     
