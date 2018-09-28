#-Health Potion game
#-health = 50
#-Difficulty: Ranges from 1 to 3; 1 being easiest and 3 most difficult
#-Health potion needs to give you random amount of added health
#  ranging from 25-50 and add that to existing health.
#  Must import random module to make this work.
#-The harder the difficulty, the less health boost you can get

import random #imported Pythons Random Module function. Generates Random numbers. always put at top

#variables
health = 50
difficulty = 2  #difficulty is 1-3. 1 being the easiest. 


potion_health = int(random.randint(25,50) / difficulty)  #Here had to use casting. Division changes the type to a float and gives us Decimal.
                                                         #so we add INT to keep it an integer or whole number. That is Casting.
                                                        #random.randint() is the random funtion which comes from imported random module at top.
health = health + potion_health
print(health)

