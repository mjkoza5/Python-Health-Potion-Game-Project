#create class for $1 coin
#our coin class will have 6 states
import random


class Dollar:

    #Method that increases value if coin is Rare
    def __init__(self, rare = False): #CONSTRUCTOR METHOD
        self.rare = rare    #rare is boolean

        if self.rare == True: #if self.rare: <-- This code is same thing as == True.
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 26.49 #mm
        self.thickness = 25.5 #mm
        self.heads = True #boolean


    #Method that will make the coin rust
    def rust(self):
        self.color = "greenish" #if our coin rust's it will become "greenish"


    #Method that will Clean the coin if it's RUSTY
    def clean(self):
        self.color = "gold"


    #Method that will make out Coin FLIP
    def flip(self):
        heads_options = [True, False]   #heads can be true or false
        choice = random.choice(heads_options) #randomly select True or False
        self.heads = choice
 

    #Method to allow coin to be spent
    #To do this, we need to use the DESCTUCTOR METHOD
        #Desturctor method is called automatically when program finishes
        # and is used to destory the object.
    def __del__(self):
        print("Coin Spent!")


        
