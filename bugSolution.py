def function_with_uncommon_bug_solution(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x % 2 == 0:
        return function_with_uncommon_bug_solution(x - 2)
    else:
        return function_with_uncommon_bug_solution(x-1) # handle odd numbers correctly

#Example usage:
print(function_with_uncommon_bug_solution(5))  # Output: 5
print(function_with_uncommon_bug_solution(10)) # Output: 0