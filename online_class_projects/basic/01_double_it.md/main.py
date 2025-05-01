END_POINT:int=100

def main():
    current_value:int=int(input('Enter a value to double: '))
    while current_value <= END_POINT:
        current_value*=2
        print(current_value)
        
    print('Stopped doubling because value is greater than 100')
    
if __name__ == '__main__':
    main()  