# Recursion means function calling itself

# A recursive function must have:

#  Base Case: The condition under which the function stops calling itself to prevent infinite recursion.
#  Recursive Case: The part of the function where it calls itself with a smaller or simpler argument.


#here's simple example

def recursive_sum(n):
    # Base Case: If n is 1, return 1
    if n == 1:
        return 1
    # Recursive Case: If n is greater than 1, call the function with n-1
    else:
        return n + recursive_sum(n-1)
    
#calling the function
print(recursive_sum(5))  # Output:15 (5+4+3+2+1)

