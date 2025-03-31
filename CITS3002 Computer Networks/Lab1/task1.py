def hamming_distance(codeword1, codeword2):
    # check if codewords are same length
    if len(codeword1) != len(codeword2):
        raise ValueError("Codewords must be of the same length")
    
    distance = 0
    
    # Iterate through bits of the codewords
    for bit1, bit2 in zip(codeword1, codeword2):
        if bit1 != bit2:
            distance += 1
    
    return distance


"""
for each valid codeword in the list, the function calcs the HDist between that codeword and the
received data using our original function.
"""


def checking_codewords(codewords, received_data):
    # Initialise variables
    min_distance = float('inf')  
    corrected_codeword = None
    
    # Iterate through codewords list given
    for codeword in codewords:
        # Calculate the HDist between the received data and the current codeword
        distance = hamming_distance(received_data, codeword)
        
        
        # If the dist is smaller than the curr min, update the min and corrected codeword
        if distance < min_distance:
            min_distance = distance  
            corrected_codeword = codeword    
            
            
        # If the distance is equal to the curr min, it means there's a tie (error cannot be corrected)
        elif distance == min_distance:
            corrected_codeword = 'error detected'
    

    return corrected_codeword 


###################################################################################################################################################

# Test hamming_distance function
# print("hamming dist test: ")
# print(hamming_distance('10011101', '10111110')) # 3


# # Test checking_codewords function:
# codewords = ['0000000000', '1111100000', '0000011111', '1111111111']
# received_data = '0000000010'
# print("checking codewords test: ")
# print(checking_codewords(codewords, received_data))  # Output: '0000000000'





###################################### LAB


# codewords = ['1010101101', '0101110101', '1110100110', '0000010110', '1101101001']
# received_data = '0010110111'
# print('Question 1: ', checking_codewords(codewords, received_data))

# codewords = ['1010111101', '0101110101', '1110101110', '0010110010', '1111000110', '1100101001']
# received_data = '1001100101'
# print('Question 2: ', checking_codewords(codewords, received_data)) 

# codewords = ['1010111101', '0101110101', '1110101110', '0000000110', '1100101001']
# received_data = '0001000101'
# print('Question 3: ', checking_codewords(codewords, received_data))


# ATTEMPT 2
# codewords = ['1010101101', '0101110101', '1110100110', '0000010110', '1101101001']
# received_data = '0010110111'
# print('Question 1: ', checking_codewords(codewords, received_data))

# codewords = ['1010111101', '0101110101', '1110101110', '0010110010', '1111000110', '1100101001']
# received_data = '1001111101'
# print('Question 2: ', checking_codewords(codewords, received_data))

# codewords = ['1010111101', '0101110101', '1110101110', '0000000110', '1100101001']
# received_data = '1011110000'
# print('Question 3: ', checking_codewords(codewords, received_data))

# 3
codewords = ['1010111101', '0101110101', '1110101110', '0010110010', '1111000110', '1100101001']
received_data = '1000011100'
print('Question 1: ', checking_codewords(codewords, received_data))

codewords = ['1010101101', '0101110101', '1110100110', '0000010110', '1101101001']
received_data = '0010110111'
print('Question 2: ', checking_codewords(codewords, received_data))

codewords = ['1010111101', '0101110101', '1110101110', '0000000110', '1100101001']
received_data = '0001000101'
print('Question 3: ', checking_codewords(codewords, received_data))