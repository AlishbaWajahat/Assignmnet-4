def in_stock(fruit:str):
    stock:dict[str,int]={
        "banana":1,
        "mango":6,
        "grapes":50,
        "peaches":24,
        "watermelon":7
    }
    
    if fruit in stock:
        print(f'There are {stock[fruit]} {fruit} in sophia\'s stock')
        
    else:
        print("This fruit is not in stock.")
        
def main():
        fruit : str = input("Enter a fruit: ")
        in_stock(fruit)
        
if __name__ == '__main__':
        main()