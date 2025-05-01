import random

NUM_ROUND=5
def main():
    score=0
    print('Welcome to the High-Low Game!')
    print('-'*8)
    for i in range(5):
        computer_number:int=random.randint(1,100)
        user_number:int=random.randint(1,100)
        print(f"Round: {i+1}")
        print(f'Your number is {user_number}')
        while True:
            guess: str = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()
            if guess in ['higher', 'lower']:
                break
            else:
                print("Invalid input. Please enter 'higher' or 'lower'.")
        higher_and_correct:bool=guess=='higher' and computer_number<user_number
        lower_and_correct:bool=guess=='lower' and computer_number>user_number
        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_number}")
            score+=1
            print(f"Your score is now {score}")
            print()

        else :
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
            print()

    print(f"Your final score is {score}")
    if score==5:
        print('Wow! You played perfectly!')
    elif 2<score<5:
        print('Good job, you played really well!')
    else:
        print('Better luck next time!')
            

if __name__=='__main__':
    main()
    
        
        
            
            
        
    
    
    