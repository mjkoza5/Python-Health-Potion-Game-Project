import random

questions = ["Why is the earth round? ", "Why do dogs bark? ", "Why do you suck at python? "]

question = random.choice(questions)             #using the random.choice function. import random module
answer = input(question).lower().strip()

while answer != "just because":
    answer = input("Why? ").strip().lower()

print("oh...okay")
