#list of known users
known_users = ["Alice", "Matt", "Bart", "Greg", "Collin", "Tom", "Robert", "Donald"]


while True:
    print("Hi! My name is Travis")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Hello {}! Your name is Recognized and access is granted.".format(name))
        remove = input("Would you like to be removed from the system (y/n)? ").strip().lower()

        if remove == "y":
            known_users.remove(name)
            print("Your name has been deleted and you're no longer in the system!")
        elif remove == "n":
            print("No problem. You have not been removed.")

            
    else:
        print("hmmm I don't think I'v met you yet {}.".format(name))
        add_me = input("Would you like to be added to the system (y/n)? ").strip().lower()
        
        if add_me == "y":
            known_users.append(name) #append function adds whatever user inputs into the list
            print("Your name has been added to the database!")

        elif add_me == "n":
            print("No problem, you have not been added. Bye Bye.")
            
