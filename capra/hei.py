def count_occurences(string, character):
    count = 0
    for i in range(len(string)):
        if character == string[i]:
            count += 1
    return count

# 
def replace_with_greatest(list):
    new_list = []
    for i in range(len(list) - 1):
        highest = list[i + 1]
        for j in range(i + 1, len(list)):
            if list[j] > highest:
                highest = list[j]
        new_list.append(highest)
    new_list.append(-1)
    return new_list

def is_palindrome(number):
    

def get_palindrome(number):
    new_number = number
    while (!is_palindrome(new_number)):
        reverse = int(str(number[::-1]))
        new_number = number + reverse
    return new_number


print(str(123)[::-1])