def function_with_uncommon_bug(x):
    if x == 0:
        return 0  # This is correct
    elif x == 1:
        return 1  # This is correct
    else:
        return function_with_uncommon_bug(x - 2)  #The bug is here! This will cause a recursion error if x is an odd number greater than 1, as it will never reach the base cases. 