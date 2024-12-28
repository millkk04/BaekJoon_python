x=int(input())
output=[input() for _ in range(x)]
output=list(set(output))
output=sorted(output,key=lambda n : [len(n),n])
print('\n'.join(output))   