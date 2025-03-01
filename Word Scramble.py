import random #inbuild library for generating the random numbers
Words = ['python', 'Javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

#To select the random word from the words list
Word_to_Guess = random.choice(Words)

#To scramble the chosen word
List_of_chosen_word = list(Word_to_Guess)
random.shuffle(List_of_chosen_word)
Scrambled_word = "".join(List_of_chosen_word)

#Title
print("Welcome to the unscramble the jumbled words contest 2025")
print("Scrambled word is:",Scrambled_word)

#Conditions to compare the player's guess with the actual word
Attempt = 0
while True:
    Payer_Guess = input ("Enter your guess:")
    Attempt += 1
    if Payer_Guess == Word_to_Guess:
        print(f"Congrats mate, you successfully unscrambled the jumbled word in {Attempt} attempt(s)!")
        break
    else:
        print(f"Sorry, Please try again")