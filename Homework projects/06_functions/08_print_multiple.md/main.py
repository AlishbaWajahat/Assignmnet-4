def print_message(message,repeats):
    print((message + " ") * repeats)
    
def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_message(message,repeats)
    
if __name__ == '__main__': main()