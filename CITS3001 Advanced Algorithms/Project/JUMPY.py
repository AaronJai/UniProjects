# from itertools import permutations

# def jumpy(num_children, wolf_distance, wolf_speed, children_distance, children_speed):
    
#     wolf_time = wolf_distance / wolf_speed
    
#     count = num_children
    
#     for i in permutations(children_speed):
        
#         num_caught = 0
        
#         for j in range(num_children):
#             child_time = children_distance[j] / i[j]
            
#             if child_time > wolf_time:
#                 num_caught += 1
                
#         count = min(count, num_caught)

#     return count

##############################################

# def jumpy(num_children, wolf_distance, wolf_speed, children_distance, children_speed):
    
#     wolf_time = wolf_distance / wolf_speed
    
 
#     num_caught = num_children 
    
#     for i in range(num_children):
#         caught_count = 0

#         for j in range(num_children):
#             child_time = children_distance[i] / children_speed[j]
            
#             if child_time > wolf_time:
#                 caught_count += 1
        

#         num_caught = min(num_caught, caught_count)

#     return num_caught


#################################################

def jumpy(num_children, wolf_distance, wolf_speed, children_distance, children_speed):

    wolf_time = wolf_distance / wolf_speed

    minimum_speeds_required = []
    for i in range(num_children):
        minimum_speeds_required.append(children_distance[i] / wolf_time)
    
    minimum_speeds_required.sort()
    children_speed.sort()
    
    count = 0
    # for i in range(num_children):
    #     if children_speed[i] < minimum_speeds_required[i]:
    #         count += 1

    speed_pointer = 0

    for required_speed in minimum_speeds_required:
        while speed_pointer < num_children and children_speed[speed_pointer] < required_speed:
            speed_pointer += 1
        
        if speed_pointer < num_children:
            speed_pointer += 1
        else:
            count += 1
    
    return count




num_children, wolf_distance, wolf_speed = map(int, input().split())
children_distance = list(map(int, input().split()))
children_speed = list(map(int, input().split()))
print(jumpy(num_children, wolf_distance, wolf_speed, children_distance, children_speed))

# # test 1
# num_children, wolf_distance, wolf_speed = 3, 100, 10
# children_distance = [25, 35, 40]
# children_speed = [2, 3, 4]

# print("test 1 expected 1. Got:", jumpy(num_children, wolf_distance, wolf_speed, children_distance, children_speed))  

# # test 2
# num_children, wolf_distance, wolf_speed = 3, 100, 4
# children_distance = [35, 40, 25]
# children_speed = [2, 3, 4]

# print("test 2 expected 0. Got:", jumpy(num_children, wolf_distance, wolf_speed, children_distance, children_speed))  


# # test 3
# num_children, wolf_distance, wolf_speed = 2, 2, 100
# children_distance = [1, 1]
# children_speed = [100, 1]

# print("test 3 expected 1. Got:", jumpy(num_children, wolf_distance, wolf_speed, children_distance, children_speed))  


# # test 4
# num_children, wolf_distance, wolf_speed = 3, 2, 100
# children_distance = [1, 1, 1]
# children_speed = [5, 10, 15]

# print("test 4 expected 3. Got:", jumpy(num_children, wolf_distance, wolf_speed, children_distance, children_speed))  


