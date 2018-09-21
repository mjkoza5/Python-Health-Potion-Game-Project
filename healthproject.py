import random #imported Pythons Random Module function. Generates Random numbers. always put at top

#variables
health = 50
difficulty = 2  #difficulty is 1-3. 1 being the easiest. 


potion_health = int(random.randint(25,50) / difficulty)  #Here had to use casting. Division changes the type to a float and gives us Decimal.
                                                         #so we add INT to keep it an integer or whole number. That is Casting.
                                                        #random.randint is the random funtion
health = health + potion_health
print(health)

