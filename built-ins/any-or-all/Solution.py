# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = list(map(int, input().split()))
print(all(x > 0 for x in lst) and any(str(x) == str(x)[::-1] for x in lst))
