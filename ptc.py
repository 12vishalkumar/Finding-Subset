# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    N1 = int(input())
    S1 = set(map(int, input().split()))
    N1 = int(input())
    S2 = set(map(int, input().split()))
    print(S1.issubset(S2))
