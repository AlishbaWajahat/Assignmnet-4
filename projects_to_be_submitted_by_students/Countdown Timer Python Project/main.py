import time

def timer(t):
    while t>=0:
        mins,secs=divmod(t,60)
        timer=f'{mins:02d}:{secs:02d}'
        print(timer,end='\r')
        time.sleep(1)
        t-=1
    print()
    print('Timer up!')
    
t=input('Enter the time in seconds. ')
timer(int(t))

# def timer(mins):
#     total_sec=mins*60
#     while total_sec:
#         mins,secs=divmod(total_sec,60)
#         timer=f'{mins:02d}:{secs:02d}'
#         print(timer,end='\r')
#         time.sleep(1)
#         total_sec-=1
#     print()
#     print('Timer up!')
    
# t=input('Enter the time in mins. ')
# timer(int(t))
