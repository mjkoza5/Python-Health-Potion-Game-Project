#creating our dictionary

films = {
    "Bond":[13,4],
    "Scream":[18,3]
    }

#ask user which movie they'd like to see
#put in while loop
#store users input into choice variable

while True:
    print("Hi! Our films are Bond or Scream. Which would you like to see?")
    choice = input("Which film would you like to see? ").strip().title()

    #Gathering age and checking if old enough to see selected film
    if choice in films:
        age = int(input("please provide your age: ").strip())

        if age >= films[choice][0]:
            
            #number of seats

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1 #subtracts a seat

            else:
                print("Sorry, we're sold out!")

        else:
            print("You're not old enough to watch this movie.")

    else:
        print("We don't currently show this film. Sorry.")
