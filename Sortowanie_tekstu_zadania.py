def bubble_sort(string):
    li = []
    n = len(string)
    for i in range(0, n):
        li.append(string[i])
    
    for i in range(0, n):
        for j in range(0, n):
            if li[i] < li[j]:
                temp = li[i]
                li[i] = li[j]
                li[j] = temp

    string_return = ""
    for i in range(0, n):
        string_return += li[i]
    
    return string_return

# Test the function
string = "9870345621"
print("Sorted string using bubble sort:", bubble_sort(string))
def insertion_sort(string):
    li = []
    n = len(string)
    
    for i in range(n):
        li.append(string[i])
    
    for i in range(1,n):
        temp = li[i]
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j+1] = temp
    
    string_return = ""
    for i in range(n):
        string_return += li[i]
    
    return string_return


# Test the function

print("Sorted string using insertion sort:", insertion_sort(string))

'''
2. Napisz program sortujący alfabetycznie listę napisów (łańcuchów znaków) składających się z samych cyfr
9876 123 76547 4343 898 2345

'''

def zad_2(string):
    string = string.replace(" ","").lower()
    li = []
    n = len(string)
    
    for i in range(n):
        li.append(string[i])
    
    for i in range(1,n):
        temp = li[i]
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j+1] = temp
    
    string_return = ""
    for i in range(n):
        string_return += li[i]
    
    return string_return

zad2string = "9876 123 76547 4343 898 2345"
print(zad_2(zad2string))