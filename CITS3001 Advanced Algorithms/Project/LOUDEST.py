
def calculate_volume(integer_str, volumes):
    total_volume = sum(volumes[int(digit)] for digit in integer_str)
    return total_volume / 9  # Average volume


n = int(input())
volumes = list(map(int, input().split()))

# Initializing variables to store the loudest integer and its volume
loudest_integer = ""
max_volume = -1

# Processing each n int
for _ in range(n):
    integer = input().strip() 
    volume = calculate_volume(integer, volumes)
    
    # check for highest vol
    if volume > max_volume:
        max_volume = volume
        loudest_integer = integer


print(loudest_integer)
