def storing_info():
    phonebook : dict [str,int]={}
    while True:
        Name=input('Enter your name: ')
        if Name=='':
            break
        number=(input('Enter your phone number: '))
        phonebook[Name]=number
        print('Contact created!')
    for name in phonebook:
        print(f'{name}: {phonebook[name]}')
    return phonebook

def look_up(phonebook):
    while True:
        Name=input('Enter name to lookup: ')
        if Name=='':
            break
        if Name not in phonebook:
            print(f'{Name}\'s number is not in phonebook')
        else:
            print(phonebook[Name])
            
def main():
    phonebook=storing_info()
    look_up(phonebook)

if __name__ == '__main__':
    main()
