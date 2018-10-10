#Pig Latin Translator project

#1) Get sentance from user
original = input("write a short sentance: ").strip().lower()

#2) split sentance into words. We do this by using the string method called SPLIT
#this split string method will split a string at every word by default

words = original.split()

#3) loop through words and convert into pig latin

new_words = []

for word in words:
    if word[0] in "aeiou":                #if word starts with vowel, add "yay"
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0                   #move consonant cluster to the end of the word and add "ay"
        for letter in word:             #we can loop through each letter in the word, and find index    
            if letter not in "aeiou":   #where the letters turn into vowels. Need to keep track of index with vowel_pos variable
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)


#if word starts with vowel, add "yay"
#otherwise, move first consonant cluster to end and add "ay"

#4) stick words back together

output = " ".join(new_words) #using the join method(a string method). Basically Joins
                            #each word in the new words list together but add a space between each word.


#5) output the final string

print(output)
