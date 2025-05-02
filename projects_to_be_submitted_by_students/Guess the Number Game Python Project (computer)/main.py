import random
def main():
    secret_number=random.randint(0,99)
    print("I am thinking of a number between 1 and 99...")
    user_input:int=0
    while user_input!= secret_number:
        user_input:int=int(input('I am thinking of a number between 0 and 99... Enter a guess: '))
        if user_input>secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        print()
        
        
    print(f'Congrats! The number was: {secret_number}')
if __name__ == '__main__':
    main()