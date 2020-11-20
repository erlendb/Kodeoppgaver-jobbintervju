from copy import copy

def multiply_n_highest_in_list(list, n):
    list = copy(list) # Ensure we only manipulate the list in the function scope
    n = min(len(list), n) # Ensure n is inside bounds of the list
    
    list.sort()
    
    product = 1
    i = len(list) - 1
    while n > 0:
        product *= list[i]
        i -= 1
        n -= 1
        
    return product

if __name__ == '__main__':
    list = [1, 2, -3, 4, 5, -7]
    n = 3
    print(multiply_n_highest_in_list(list, n))
    print(list)