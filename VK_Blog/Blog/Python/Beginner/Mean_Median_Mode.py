# Python3.10

# Project: Calculate Mean, Median and Mode in python3

# function for Mean
def mean(array_int):
    
    result = sum(array_int)/len(array_int)
    return result


# function for Median
def median(array_int):

    array_int.sort()

    if len(array_int) % 2 == 0:
        median = array_int[len(array_int)//2]
        median2 = array_int[len(array_int)//2 -1]
        median = (median + median2)/2
    else:
        median = array_int[len(array_int)//2]
    return median

# function for mode

def mode(array_int):

    freq = {}
    for i in array_int:
        freq.setdefault(i,0)
        freq[i]+=1
    
    frequent = max(freq.values())
    for i, j in freq.items():
        if j == frequent:
            result = i
    return result

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
print(f"Finding Mean, Median and Mode for{ list1}")
print(f"Mean: {mean(list1)} ")
print(f"Median: {median(list1)}")
print(f"Mode: {mode(list1)}")