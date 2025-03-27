
from random import random
import os

CORRUPTION_RATE = 0.25

def crc16(data: bytes):
    xor_in = 0x0000  # initial value
    xor_out = 0x0000  # final XOR value
    poly = 0x8005  # generator polinom (normal form)

    reg = xor_in
    for octet in data:
        # reflect in
        for i in range(8):
            topbit = reg & 0x8000
            if octet & (0x80 >> i):
                topbit ^= 0x8000
            reg <<= 1
            if topbit:
                reg ^= poly
        reg &= 0xFFFF
        # reflect out
    return reg ^ xor_out


def corrupt_data(data : bytes):
    '''
    some random corruption of byte data
    modify as needed, mostly the CORRUPTION_RATE global constant
    ''' 
    temp = data[:]
    while True:
        location = int(len(temp) * random())
        data_list = list(temp)
        if random() < 0.5:
            data_list[location] = (data_list[location] + 1) % 256
        else: 
            data_list[location] = (data_list[location] - 1) % 256
        temp = bytes(data_list)
        if random() < CORRUPTION_RATE and temp != data:
            break
    return temp
###############################################################################################

"""
CRC16: The polynomial division used in CRC16 ensures that even small changes in the data (e.g., flipping a single bit) result in a significantly different checksum. This high sensitivity makes it more likely to detect errors.

Trivial Checksum: The trivial checksum is less sensitive to small changes. For example, if two bytes are swapped, the sum remains the same, and the checksum does not change, failing to detect the error. - it only checks for basic arithmetic changes


"""

# task 3

def random_message(n):
    return os.urandom(n)

# task 4

def trivial_checksum(data: bytes):
    return sum(data) % 256 


# after getting first attempt wrong, I decided to run it for up to 1 million trials.
# saw that it would not detect about 5-9 errors out of the million
def evaluate_performance(trials):
    detected_errors = 0
    
    for i in range(trials):
        data = random_message(10)
        checksum_value = crc16(data)

        corrupted_data = corrupt_data(data)
        checksum_corrupted = crc16(corrupted_data)

        if checksum_value != checksum_corrupted:
            detected_errors += 1

    print(f"Detected errors: {detected_errors} out of {trials}")

print("CRC16")
evaluate_performance(1000000)


def evaluate_performance(trials):
    detected_errors = 0
    
    for i in range(trials):
        data = random_message(10)
        checksum_value = trivial_checksum(data)

        corrupted_data = corrupt_data(data)
        checksum_corrupted = trivial_checksum(corrupted_data)

        if checksum_value != checksum_corrupted:
            detected_errors += 1

    print(f"Detected errors: {detected_errors} out of {trials}")

print("Trivial Checksum")
evaluate_performance(10000)



# data = random_message(10)
# checksum_value = crc16(data)


# corrupted_data = corrupt_data(data)
# checksum_corrupted = crc16(corrupted_data)


##usecase for crc16 function
#data = b"helloworld"
#print(crc16(data))

##usecase for corrupt_data function
#corrupt_data(b"helloworld")