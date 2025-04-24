
def main():
    user_age:int=int(input('How old are you? '))
    if user_age>=16 and user_age<25:
        print(f'You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48')
        
    elif user_age>=25 and user_age<48:
          print(f'You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48')
    else:
        print(f'You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You can vote in Mayengua where the voting age is 48')
        
if __name__ == '__main__':
    main()
        
        
    