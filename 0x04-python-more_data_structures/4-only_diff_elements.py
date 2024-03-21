#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing all elements present in only one set.
    """
    # Create a new set to store the unique elements
    unique_elements = set()

    # Add elements from set_1 that are not in set_2
    for element in set_1:
        if element not in set_2:
            unique_elements.add(element)

    # Add elements from set_2 that are not in set_1
    for element in set_2:
        if element not in set_1:
            unique_elements.add(element)

    return unique_elements
