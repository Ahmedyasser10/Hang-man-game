import hangman_art
import random
print(hangman_art.logo)
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
diplay=[]
for i in chosen_word:
    diplay.append("_")
lives=6
end_game=False
while not end_game:
    print(' '.join(diplay))
    letter=input("enter a letter ")
    for i in range(len(chosen_word)):
        if letter == chosen_word[i]:
            diplay[i]=letter
    if letter not in chosen_word:
        print(hangman_art.stages[lives])
        lives-=1
        print(f"you have chosen the letter {letter} ")
        if lives==0:
            print("You lose!")
            print(hangman_art.stages[0])
            end_game=True
    if "_" not in diplay:
        end_game=True
        print("You win!")
