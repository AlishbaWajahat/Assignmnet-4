def main():
    fruits :dict[str,int|float]= {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total:int|float=0
    for fruit in fruits:
        price:int|float=fruits[fruit]
        amount:int=int(input(f'How many {fruit} do you want to buy? '))
        total += (price*amount)
        
    print(f'Your total is ${total}')
    
if __name__ == '__main__':
    main()