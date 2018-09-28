#-Health Potion game
#-health = 50
#-Difficulty: Ranges from 1 to 3; 1 being easiest and 3 most difficult
#-Health potion needs to give you random amount of added health
#  ranging from 25-50 and add that to existing health.
#  Must import random module to make this work.
#-The harder the difficulty, the less health boost you recieve. Divide
#  the health potion by the difficulty


import random

health = 50
difficulty = input("Select Difficulty Level between 1-3. 3 is Hardest. 1 is easiest: ")


potion = int(random.randint(25,50) / int(difficulty))

health = health + potion
print(health) 

