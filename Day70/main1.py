n = int(input())
score = list(map(int, input().split()))
print(score)

unique_scores = set(score)
print(unique_scores)

max_score = max(unique_scores)
print(max_score)

unique_scores.remove(max_score)

runner_score = max(unique_scores)
print(runner_score)

