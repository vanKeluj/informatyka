list = [1,1,1]

def Mon(L):
    if all(L[i] > L[i+1] for i in range(len(L)-1)):
        return "malejący"
    elif all(L[i] < L[i+1] for i in range(len(L)-1)):
        return "rosnący"
    elif all(L[i] == L[i+1] for i in range(len(L)-1)):
        return "stały"
    else:
        return False


print(f"Ciąg jest monotoniczny: {Mon(list)}")