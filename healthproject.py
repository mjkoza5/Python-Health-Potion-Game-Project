import random #this is Pythons Random Module that we imported. Generates Random numbers. always put at top

#variables
health = 50
difficulty = 2  #difficulty is 1-3. 1 being the easiest. 


potion_health = int(random.randint(25,50) / difficulty)  #Here we are casting. Division changes the type to a float.
                                                         #so we add INT to keep it an integer or whole number. That is Casting
                                                        #random.randint is the random funtion
health = health + potion_health
print(health)

