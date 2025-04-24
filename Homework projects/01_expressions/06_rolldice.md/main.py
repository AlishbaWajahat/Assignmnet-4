import random

SIDES_DICE:int = 6

def main():
    dice1 : int=random.randint(1,SIDES_DICE)
    dice2 : int=random.randint(1,SIDES_DICE)
    
    print(f'''
    first dice = {dice1}
    Second Dice = {dice2}
    Total of 2 dices = {dice1+dice2}''')
    
if __name__ == '__main__':
    main()    