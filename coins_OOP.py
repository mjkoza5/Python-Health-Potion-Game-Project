#create class for $1, Quarter, Dime, and Nickel coins
import random


class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs): #CONSTRUCTOR METHOD

        for key, value in kwargs.items():
            setattr(self,key,value)             #setattr = set attributes
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = True

        #if coin is rare
            #then coinValue = coinOriginalValue * 1.25
        #otherwise:
            #coinValue = coinOriginalValue
        if self.is_rare:
            self.value = self.original_value * 1.25 #this will give coin +25% value
        else:
            self.value = self.original_value


        #if coin is clean
            #the coin color = the coin color when it's clean
        #otherwise
            #the coin color = the coin color when it's rusty
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color


    #Method that will make the coin rust
    def rust(self):
        self.color = self.rusty_color #if our coin rusts, it will become a rusty color

    #Method to clean the coin
    def clean(self):
        self.color = self.clean_color #coin color is it's original color whatever that color is

    #DESTRUCTOR METHOD (aka coin is spent/used)
    def __del__(self):
        print("Coin Spent!")

    #Method that will make out Coin FLIP
    def flip(self):
        heads_options = [True, False]   #heads can be true or false
        choice = random.choice(heads_options) #randomly select True or False
        self.heads = choice

    def __str__(self): #this defines what comes out when you print an object.
                        #if it's a quarter, it needs to say "Quarter"
        if self.original_value >= 1:
            return "${} coin".format(int(self.original_value))
        if self.original_value == 0.25:
            return "Quarter"
        if self.original_value == 0.10:
            return "Dime"
        else:
            return "Nickel"


class Quarter(Coin): 
    def __init__(self): 
        data = {
            "original_value": 0.25,
            "clean_color": "silver",
            "rusty_color": "orangish",
            "num_edges": 1,
            "diameter": 15.21,
            "thickness": 4.5,
            "mass": 1.5
            }
        super().__init__(**data)



class Dime(Coin): 
    def __init__(self): 
        data = {
            "original_value": 0.10,
            "clean_color": "silver",
            "rusty_color": "orangish",
            "num_edges": 1,
            "diameter": 9.3,
            "thickness": 1.5,
            "mass": 1.5
            }
        super().__init__(**data)

        #POLYMORPHISM - When a method has mutiple forms inside a class.
        #To do this we will override the rust and clean methods
        def rust(self):
            self.color = self.clean_color #Dimes are made of silver and don't rust
                                          #so we override the standard behavior from the
                                          #parent class for the rust and clean methods
        def clean(self):
            self.color = self.clean_color


class Nickel(Coin): 
    def __init__(self): 
        data = {
            "original_value": 0.05,
            "clean_color": "silver",
            "rusty_color": "orangish",
            "num_edges": 1,
            "diameter": 15.21,
            "thickness": 4.5,
            "mass": 1.5
            }
        super().__init__(**data)


            

class Dollar(Coin):  #So this is class called Dollar that will inherit from Parent class COIN
                     #By default, this class will inherit all the methods above from Coin
    def __init__(self):
        #making a DICTIONARY with this specific Dollar's values
        #ex. clean color = green. Rusty color = orange. value = 1.00
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 26.46,
            "thickness": 25.3,
            "mass": 9.5
            }
        #We're going to pass all the "Dollar" class data into the Parent class (Coin)
        #init function. To run the Parents init function, we need to access the parent
        #class. To do this we use the "super" function/class. The super class and the parent
        #class are the same thing. Essentially, super means parent class.

        #In this super function/class we want to run the "init" function aka CONSTRUCTOR,
        #and pass all the data as KEYWORD Arguments. How do we do that?
        #We UNPACK the **data!!! from data dictionary into keyword arguments.
        
        super().__init__(**data)

        #We need the Parent class to accept all the data. So at the top, in the Coin Class,
        #in the Parameters, you'll see "**kwargs": which is where all the info will be packed down
        #into keyword arguments called kwargs.
        #SO it's taking the keywaord arguments and packing them into a dictionary called "kwargs".





coins = [Quarter(), Dime(), Nickel(), Dollar()] #List of coins

for coin in coins: #Loop through each of the coins in our List above:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness, coin.num_edges,
                 coin.mass]

    string = "{} - Color: {}, value: {}, diameter(mm): {}, thickness(mm): {}, number of edges: {}, mass(g): {}".format(*arguments)
                                                                                                    #unpacking the arguments above
    print(string)
        
