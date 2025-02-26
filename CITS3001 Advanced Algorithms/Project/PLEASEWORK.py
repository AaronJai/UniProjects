from collections import Counter

def find(num_questions, her_answers, cor_answers):
    initial_score = 0
    for i in range(num_questions):
        if her_answers[i] == cor_answers[i]:
            initial_score += 1
    
    jenny_count = Counter(her_answers)
    correct_count = Counter(cor_answers)
    mismatch = Counter()

    for i in range(num_questions):
        if her_answers[i] != cor_answers[i]:
            mismatch[her_answers[i]] += 1

    max_score = initial_score

    for ch1 in 'ABCDE':
        if mismatch[ch1] == 0:
            continue
        for ch2 in 'ABCDE':
            if ch1 == ch2:
                continue
            gained = min(mismatch[ch1], correct_count[ch2])
            lost = jenny_count[ch1] - mismatch[ch1]
            new_score = initial_score + gained - lost
            max_score = max(max_score, new_score)

    return max_score

num_questions = int(input())
her_answers = input().strip()
cor_answers = input().strip()

print(find(num_questions, her_answers, cor_answers))
