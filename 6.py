# https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# # Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(0, T):
    S = input()
    print(S[0::2]+" "+S[1::2])
