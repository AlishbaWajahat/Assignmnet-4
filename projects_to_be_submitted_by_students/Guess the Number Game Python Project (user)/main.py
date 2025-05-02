import random

def guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is my guess {guess} too high (H) ,too low (L) OR CORRECT(C): ").lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'Yayy! I guessed {guess} right and won')
    
guess(10)
    
    