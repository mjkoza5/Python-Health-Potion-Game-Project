#Get user email address
email = input("What is your email address? ").strip()
    #the strip method strips away blank spaces
    # incase user makes a mistake and put in spaces


#Slice out username
user = email[:email.index("@")]


#Slice out domain name
domain = email[email.index("@") + 1:]
    #add +1 so it retunrs everything after the @ symbol, without the @ symbol.
    #So the @ symbol will not appear in the output.

#format message

output = "Your username is {} and your domain is {}".format(user, domain)


#Display output message
print(output)
