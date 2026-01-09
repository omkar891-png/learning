n = int (input())
scores = []
for i in range (n):
    score = float(input(f"Enter the score of student {i+1}: "))
    if score >=-100 and score <= 100:
        scores.append(score)
first_prize = max (scores)
scores.sort(reverse=True)
for i in  scores :
    if i < first_prize:
        second_prize = i
        break
print("The runner-up score is:", second_prize)

 
