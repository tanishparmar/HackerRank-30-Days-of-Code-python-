# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
pbook = {}
for i in range(n):
    name,contact = input().split()
    pbook[name] = contact
    
try:
    while(1):
        check = input()
        if(check in pbook):
            print(check+"="+pbook[check])
        else :
            print("Not found")
except(EOFError):
    pass

