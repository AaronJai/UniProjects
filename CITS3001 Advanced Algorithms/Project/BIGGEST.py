def biggest(digit, original_number):
    for i in range(len(original_number)):
        if original_number[i] < digit:
            return original_number[:i] + digit + original_number[i:]
    
    return original_number + digit


# x = input().split()
# digit, original_number = x[0], x[1]

# print(biggest(digit, original_number))

print(biggest('6', '7853'))
print(biggest('1', '111111111'))
print(biggest('9', '123456789012345678901234567890'))