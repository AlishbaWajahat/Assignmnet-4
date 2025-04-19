# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.
def main():
    anton : int =21
    beth :int =anton +6
    chen :int =beth+20
    drew : int =chen+anton
    ethan : int = chen
    
    print(f'Anton is {anton}')
    print(f'Beth is {beth}')
    print(f'Chen is {chen}')
    print(f'Drew is {drew}')
    print(f'Ethan is {ethan}')
    
if __name__ == '__main__':
    main()