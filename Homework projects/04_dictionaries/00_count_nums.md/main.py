def user_input():
    nums=[]
    num=(input('Enter a number '))
    while num!='':
        nums.append(int(num))
        num=(input('Enter a number '))
    return nums

def making_dictionary(num_lst):
    num_dict={}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num]=1
        else:
            num_dict[num]+=1
    return num_dict

def print_count(num_dict):
    for num in num_dict:
        print(f'{num} appears {num_dict[num]} times.')
        
def main():
    num_lst=user_input()
    num_dict= making_dictionary(num_lst)
    print_count(num_dict)
    
if __name__ == '__main__':
    main()
            
    
    
        
        
    