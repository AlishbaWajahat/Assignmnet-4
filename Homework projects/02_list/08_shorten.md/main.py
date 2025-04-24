MAX_LENGTH:int=3

def remove_items(lst):
  if len(lst)>MAX_LENGTH:
    while len(lst)>MAX_LENGTH:
        Deleted_item:str=lst.pop()
        print(f'Deleted item --> {Deleted_item}')
    print('Now your list has desired max length')
  elif len(lst)==MAX_LENGTH:
      print('No need to remove items,Your list has desired max length')
  else:
       print('No need to remove items,Your list has suitable length')
       
def main():
    lst=[]
    user_input:str=input('Please enter an element of the list or press enter to stop. ')
    while user_input != "":
        lst.append(user_input)
        user_input:str=input('Please enter an element of the list or press enter to stop. ') 
        
    remove_items(lst)
    
    
    
if __name__ == '__main__':
    main()