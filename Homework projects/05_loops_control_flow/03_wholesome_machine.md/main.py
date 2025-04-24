AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    user_input:str=input(f'Please type the following affirmation:{AFFIRMATION}')
    while user_input!=AFFIRMATION:
        print("That was not the affirmation.")
        user_input:str=input(f'Please type the following affirmation:{AFFIRMATION}')

    print("That's right! :)")    
    
if __name__ == '__main__':
    main()  
    