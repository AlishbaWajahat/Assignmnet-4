def main():
    while True:
     user_input=(input('Enter you height'))
     if user_input == '':
        print("Exiting the program.")
        break
     try:
      user_input=int(user_input)
     except ValueError:
        print("Please enter a valid number.")
        continue
    
     if user_input>=50:
        print('You\'re tall enough to ride!')
     else:
        print('You\'re not tall enough to ride, but maybe next year!')
     
     
if __name__ == '__main__':
    main()     
        