

def find(n, jenny_answers, correct_answers):
    
    # initialise initial score
    initial_score = 0
    for i in range(n):
        if jenny_answers[i] == correct_answers[i]:
            initial_score += 1
    
    # Initialize max score 
    max_score = initial_score
    
    for original_answer in 'ABCDE':
        for new_answer in 'ABCDE':
            if original_answer == new_answer:
                continue
            
            new_score = initial_score
            
            for i in range(n):
                if jenny_answers[i] == original_answer and correct_answers[i] == new_answer:
                    new_score += 1
                    
                if jenny_answers[i] == original_answer and correct_answers[i] == original_answer:
                    new_score -= 1
            
            max_score = max(max_score, new_score)
    
    return max_score



num_questions = int(input())
her_answers = input().strip()
correct_answers = input().strip()

print(find(num_questions, her_answers, correct_answers))


# # test 1:
# n = 4
# jenny_answers = "ABCD"
# correct_answers = "ABDE"
# print(find(n, jenny_answers, correct_answers))  # Output: 3

# # test 2:
# n = 1
# jenny_answers = "A"
# correct_answers = "A"
# print(find(n, jenny_answers, correct_answers))  # Output: 1

    
# # test 3
# n = 4
# jenny_answers = "ABCC"
# correct_answers = "ABCA"
# print(find(n, jenny_answers, correct_answers))  # Output: 3


# # test 4
# n = 5
# jenny_answers = "AAAAA"
# correct_answers = "BCDEA"
# print(find(n, jenny_answers, correct_answers))  # Expected output: 1

# # test 5
# n = 200000
# jenny_answers = "A" * 200000
# correct_answers = "A" * 199999 + "B"
# print(find(n, jenny_answers, correct_answers))  # Expected output: 199999

# # test 6
# n = 6
# jenny_answers = "AAABBB"
# correct_answers = "AAACCC"
# print(find(n, jenny_answers, correct_answers))  # Expected output: 6
