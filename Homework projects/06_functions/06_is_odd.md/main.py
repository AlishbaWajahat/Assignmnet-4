def even_odd(num):
    
    remainder=num%2
    return remainder ==1

def main():
    for i in range(10,21):
        if even_odd(i):
            print(f'{i} odd')
            
        else:
             print(f'{i} even')
             
if __name__ == '__main__':
    main()

            
    