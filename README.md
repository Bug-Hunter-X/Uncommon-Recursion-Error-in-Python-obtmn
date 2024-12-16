# Uncommon Recursion Error in Python

This repository demonstrates an uncommon recursion error in a Python function. The function `function_with_uncommon_bug` is designed to return 0 if x is 0, 1 if x is 1, otherwise, it recursively calls itself with `x-2`. However, if `x` is an odd number greater than 1, the base cases (x==0 or x==1) are never reached, leading to infinite recursion and eventually a stack overflow error. 

The `bugSolution.py` file provides a corrected version of the function that correctly handles odd numbers.