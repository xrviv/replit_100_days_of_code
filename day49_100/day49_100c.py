# OpenAIGPT3 Assisted Code
print("""🌟Current Leader🌟

Analyzing high scores......""")
print()
scores = {}
f = open("high.score", "r")

for line in f:
  name, score = line.strip().split("\t")
  scores[name] = int(score)
max_value = max(scores, key=scores.get)
print(f"HIGH SCORE: {scores[max_value]} belongs to: {max_value}")

f.close()

