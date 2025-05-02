from words import words
import random
import string

def random_word():
    word:str=random.choice(words)
    while '-' in word or ' ' in word:
        word:str=random.choice(words)
    return word.upper()

def main():
    word:str=random_word()
    word_letters:set[str]=set(word)
    used_letters:set[str]=set()
    alphabets = set(string.ascii_uppercase)
    lives:int=6
    
    while len(word_letters)>0 and lives>0:
        current_word:str=' '.join([letter if letter in used_letters else '-' for letter in word])
        print(f"Current word: {current_word}")  
        if used_letters!=set():
            print(f"used letters: {' '.join(used_letters)}")
        user_guess_letter:str=input('Guess a letter.').upper()
        if user_guess_letter in alphabets:
            if user_guess_letter not in used_letters:
                used_letters.add(user_guess_letter)
                if user_guess_letter in word:
                    word_letters.remove(user_guess_letter)
                else:
                    print('This letter is not in word')
                    lives-=1
                    print(f"{lives} lives left!")
                    print()
            else:
                print('You have already used this letter. try again')
                print()
        else:
            print('Inappropriate letter')
        print()   
    if lives==0:
        print(f'oops, you died! , the word was {word}')
    else:
        print(f'congrats you gussed the word {word} right.')
        
if __name__ == '__main__':
    main()