import random

def dice_roll():
    dice1 : int =random.randint(1,6)
    dice2 : int =random.randint(1,6)
    Total=dice1 + dice2
    print(f'total of two dice is {Total}')
    
    
def main():
    dice1 : int=10
    print(f'Dice 1 starts as {dice1}')
    dice_roll()
    dice_roll()
    dice_roll()
    print(f'Dice 1 is still {dice1}')
    
if __name__=='__main__':
    main()
    