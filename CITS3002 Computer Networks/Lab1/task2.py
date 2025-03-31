"""
RESEARCH

Hamming Code is an error-detecting and error-correcting code used to ensure data integrity during transmission. 
It uses parity bits to detect and correct single-bit errors in a transmitted codeword.

Parity Bits: These bits are inserted into the data at specific positions and used to check the parity (even or odd) of certain positions in the codeword. 
The idea is that if a single bit gets flipped during transmission (e.g., due to noise), the parity check will detect the error, and the bit can be corrected.

Codeword Structure:
In an (11, 7) Hamming Code:

7 data bits (D1, D2, ..., D7) are encoded into 11 bits.
4 parity bits (P1, P2, P4, P8) are added to create the full codeword. i.e., parity bits are placed at positions that are powers of 2 (1, 2, 4, 8)


Position (1-based)	Bit Type
1   				P1
2					P2
3					D1
4					P4
5					D2
6					D3
7					D5
8					P8
9					D6
10					D7
11					D8

"""

def hamming_code_generator(codeword):
    # Ensure the input codeword is 7 bits
    if len(codeword) != 7:
        raise ValueError("Input codeword must be 7 bits long")
    
    # Convert to list of integers
    codeword = [int(bit) for bit in codeword]
    
    # Initialise 11-bit Hamming Code
    hamming_code = [0] * 11
    
    
    # followed the format of the table in the lecture p55 #
    
    # Place data bits (D1 to D7)
    hamming_code[2] = codeword[0]  # D1
    hamming_code[4] = codeword[1]  # D2
    hamming_code[5] = codeword[2]  # D3
    hamming_code[6] = codeword[3]  # D4
    hamming_code[8] = codeword[4]  # D5
    hamming_code[9] = codeword[5]  # D6
    hamming_code[10] = codeword[6]  # D7
    
    # Calculate parity bits (direct assignment for clarity)
    hamming_code[0] = hamming_code[2] ^ hamming_code[4] ^ hamming_code[6] ^ hamming_code[8] ^ hamming_code[10]  # P1
    hamming_code[1] = hamming_code[2] ^ hamming_code[5] ^ hamming_code[6] ^ hamming_code[9] ^ hamming_code[10]  # P2
    hamming_code[3] = hamming_code[4] ^ hamming_code[5] ^ hamming_code[6]                                       # P4
    hamming_code[7] = hamming_code[8] ^ hamming_code[9] ^ hamming_code[10]                                      # P8
    
    # Return as string
    return ''.join(map(str, hamming_code))





def hamming_code_error_detection(received_data):
    # Ensure input is 11 bits
    if len(received_data) != 11:
        raise ValueError("Received data must be 11 bits long")
    
    # Convert to list of integers
    received_data = [int(bit) for bit in received_data]
    
    # Calculate syndrome bits
    s1 = received_data[0] ^ received_data[2] ^ received_data[4] ^ received_data[6] ^ received_data[8] ^ received_data[10]
    s2 = received_data[1] ^ received_data[2] ^ received_data[5] ^ received_data[6] ^ received_data[9] ^ received_data[10]
    s4 = received_data[3] ^ received_data[4] ^ received_data[5] ^ received_data[6]
    s8 = received_data[7] ^ received_data[8] ^ received_data[9] ^ received_data[10]
    
    # Compute error position
    # << = bitwise left shiift operator
    error_position = s1 + (s2 << 1) + (s4 << 2) + (s8 << 3)
    
    # Correct error if detected
    if error_position != 0:
        print(f"Error detected at position {error_position}")
        received_data[error_position - 1] ^= 1  # Flip bit (0-based index)
    else:
        print("No error detected")
    
    # Return corrected data as string
    return ''.join(map(str, received_data))


#test - from lecture 1100011 should be 11111000011
# received_data = '1100011'
# hamming_code = hamming_code_generator(received_data)
# print('Test: ' + hamming_code)


# received_data = '1011101'
# hamming_code = hamming_code_generator(received_data)
# print('Question 4: ' + hamming_code)

# received_data = '0011101'
# hamming_code = hamming_code_generator(received_data)
# print('Question 5: ' + hamming_code)

# received_data = '1100010'
# hamming_code = hamming_code_generator(received_data)
# print('Question 6: ' + hamming_code)

# ATTEMPT 2

# print("Question 4: ")
# received_data = "00100100110"
# corrected_data = hamming_code_error_detection(received_data)

# print("Question 5: ")
# received_data = "11000111101"
# corrected_data = hamming_code_error_detection(received_data)

# received_data = '1100010'
# hamming_code = hamming_code_generator(received_data)
# print('Question 6: ' + hamming_code)

# 3
received_data = '1100010'
hamming_code = hamming_code_generator(received_data)
print('Question 4: ' + hamming_code)

print("Question 5: ")
received_data = "10111010011"
corrected_data = hamming_code_error_detection(received_data)

received_data = '0011101'
hamming_code = hamming_code_generator(received_data)
print('Question 4: ' + hamming_code)