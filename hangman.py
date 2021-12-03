import random

stages = ['''
   +----+
   |    |
   O    |
  /|\   |
  / \   |
        |
  ========
  ''', '''
   +----+
   |    |
   O    |
  /|\   |
  /     |
        |
 =========
 ''',''''
   +----+
   |    |
   O    |
  /|\   |
        |
        |
  ========
  ''',''''
   +----+
   |    |
   O    |
  /|    |
        |
        |
  ========
  ''','''
   +----+
   |    |
   O    |
        |
        |
  =======
  ''','''
   +----+
   |    |
        |
        |
        |
        |
   =======
   ''']

end_of_game = False
word_list = ["mainul","Dhoni","love"]
random_choice = random.choice(word_list)
word_length = len(random_choice)
# create a var called 'lives' to keep track of the number of lives left.
# set lives to equal 6

lives = 6

print(f"Psst,the solution is {random_choice}") #testing code
display=[]   #create blank
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = random_choice[position]
        if letter == guess:
            display[position] = letter
        else:
            print("No Match")
    #If guess is not a letter in the random_choice,
    #then reduce 'lives' by 1
    #if lives goes down to zero then the gme stop a nd you lose.
    if guess not in random_choice:
        lives -= 1;
        if lives == 0:
            end_of_game = True
            print("You lose..")

    #join all the elements in the list and turn it into a string
    print (f"{' '.join(display)}")
    # check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You Win")

        #print the ascii art from stages that corresponds to
        #the current no of 'lives' the user has remainning

    print(stages[lives])
