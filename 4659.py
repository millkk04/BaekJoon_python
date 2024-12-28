


#####
def case1(List):
    for i in range(len(List)):
        if List[i] in ['a', 'e', 'i', 'o', 'u']:
            return True #True가 통과
    return False
    
def case2(List):
    for i in range(len(List) - 2):
        if List[i] in ['a', 'e', 'i', 'o', 'u'] and List[i+1] in ['a', 'e', 'i', 'o', 'u'] and  List[i+2] in ['a', 'e', 'i', 'o', 'u']:
            return False
        if List[i] not in ['a', 'e', 'i', 'o', 'u'] and List[i+1] not in ['a', 'e', 'i', 'o', 'u'] and List[i+2] not in ['a', 'e', 'i', 'o', 'u']:
            return False
    return True

def case3(List):
    for i in range(len(List) - 1):
        if List[i] == List[i + 1] and List[i] not in ['e', 'o']:
            return False
    return True
 

while True:
    s = input()
    if s == 'end': break

    flags = [case1(s), case2(s), case3(s)]

    print(f"<{s}> is not acceptable." if False in flags else f"<{s}> is acceptable.")        
    
    
