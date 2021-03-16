## REZA AZIMI
## py__version = 3.8.6
# You can replace the list_of_words file with your own file 
# to get more options 
import os
import random
from list_of_words import word_list
from termcolor import colored, cprint

def print_hangman_logo():
    print("  _   _   _____   _   _    _____   _       _   _____   _   _       +----+     ")
    print(" | | | | |  _  | | \ | |  / __  \ | \     / | |  _  | | \ | |      |    |     ")
    print(" | |_| | | |_| | |  \| | | /  |_| |  \   /  | | |_| | |  \| |      O    |     ")
    print(" |  _  | |  _  | | \ \ | | |  __  | \ \ / / | |  _  | | \ \ |     /|\   |     ")
    print(" | | | | | | | | | |\  | | |__\ \ | |\ \ /| | | | | | | |\  |     / \\   |    ")
    print(" |_| |_| |_| |_| |_| \_| |______| |_| \_/ |_| |_| |_| |_| \_|           |     ")
    print(" ------------------------------------------------------------", end='')
    cprint("     =======", 'red')

def lives(hp):
    print("HP: ", end='') 
    cprint(("<3 " * hp), 'green')

def print_hangman(p1, p2, p3, p4, p5, p6):
    print("     +----+       ")
    print("     |    |       ")
    print(f"     {p1}    |       ")
    print(f"    {p2}{p3}{p4}   |       ")
    print(f"    {p5} {p6}   |       ")
    print("          |       ")
    print("    =========     ")    

def main():
    
    session = True      
    while session:

        os.system("cls")
        print_hangman_logo()
        random_word = random.choice(word_list).lower()
        word_with_blanks = ["_" for x in range(len(random_word))] # ["_", "_", "_", "_", "_"]
        life = 6
        
        legit_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        all_letters_archive = []
        right_letters_archive = []
        
        body_part_counter = 0
        hangman_body = ['O', '/', '|', '\\','/', '\\']
        blank_body = [' ' for x in range(len(hangman_body))]
        
        
        while life > 0:
            guess = input("\nGuess a letter: ").lower()
            if guess in legit_alphabets:        
                os.system("cls")
                
                if guess in random_word:
                    for i in range(len(random_word)):
                        if random_word[i] == guess:
                            word_with_blanks[i] = guess
                            
                    for i in word_with_blanks:
                        print(i + " ", end='')
                    
                    # Won game
                    if list(random_word) == word_with_blanks:
                        cprint("\n You Won!", 'green')
                        lives(life)
                        break
                    if guess in right_letters_archive:
                        cprint("\n\nYou have already tried this letter! Try another letter!", 'yellow')
                    else:
                        cprint("\n\nCorrect guess! Keep going!", 'green')
                    if guess not in all_letters_archive:
                                right_letters_archive.append(guess)
                                all_letters_archive.append(guess)
                else:
                    # Calculating the maximum "Health Point"
                    life -= 1
                    blank_body[body_part_counter] = hangman_body[body_part_counter]
                    body_part_counter += 1
                    # Archiving the entered letter
                    if guess not in all_letters_archive:
                                right_letters_archive.append(guess)
                                all_letters_archive.append(guess)
                                
                    for i in word_with_blanks:
                        print(i + " ", end='')
                    cprint("\n\nYour guess was wrong! Try again!", 'red')
                
                print_hangman(
                    blank_body[0],
                    blank_body[1],
                    blank_body[2],
                    blank_body[3],
                    blank_body[4],
                    blank_body[5]
                )            
                lives(life)
                
                # Printing Archived Letters:
                print("\nUsed Letters: ", end='')
                for i in all_letters_archive:
                    print(i + " ", end ='')  
                print("")
            else:
                os.system("cls")
                for i in word_with_blanks:
                        print(i + " ", end='') 
                cprint("\n\nThe letter you entered is not valid!", 'yellow')
                cprint("Choose a letter from [a-z] to continue!", 'yellow')
                
                print_hangman(
                    blank_body[0],
                    blank_body[1],
                    blank_body[2],
                    blank_body[3],
                    blank_body[4],
                    blank_body[5],
                )            
                lives(life)
                
                # Printing Archived Letters:
                print("\nUsed Letters: ", end='')
                for i in all_letters_archive:
                    print(i + " ", end ='')  
                print("")
        else:
              
            cprint("\n>>>>>>>>> You lost! <<<<<<<<<", 'red')
            cprint("The Correct Answer was " + '"' + random_word + '"', 'yellow' )   
        retry = input("\nOne more game? (y/n)").lower()
        if retry == "n":       
            session = False
        
main()
