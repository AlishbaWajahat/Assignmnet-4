from hashlib import sha256

        
def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    reverse_lookup={v:k for k,v in stored_logins.items()}
    while True:
     user_input=input('Enter password: ')
     if user_input=='':
         break
     hashed=hash_password(user_input)
     if hashed in reverse_lookup:
            print(f'This password is of {reverse_lookup[hashed]}')
            break
     else:
        print('Your password is incorrect')

if __name__ == '__main__':
    main()
        
        
        

    
    