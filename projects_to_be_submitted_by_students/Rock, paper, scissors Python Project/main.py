import random

def main():
    user_choice=input('What\'s your choice ; rock (r) , paper (p) or scissor (s)? ')
    computer_choice=random.choice(['r','p','s'])
    is_user_win:bool=(user_choice=='r' and computer_choice=='s') or (user_choice=='p' and computer_choice=='r') or (user_choice=='s' and computer_choice=='p')
    
    if user_choice==computer_choice:
        print('Oops , it\'s a tie!')
    elif is_user_win:
        print('You won!')
    else:
        print('you lost!')
        
if __name__=='__main__':
    main()
    
