#temp min like in normal ch4 and above algorithms 
int_min = -32000

def cut(price, n):
    #initalize array 
    val = [0 for x in range(n+1)]
    val[0] = 0

    #bottom up manner with focus on last entry from the array
    #the two for loops needed in all dynamic algorithms I know 
    for i in range (1, n+1):
        max_val = int_min
        for j in range (i):
            #finding/updating max/OPT
            max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
    return val[n]

#global test values 
arr = [1,5,8,8,10,17,17,20]
size = len(arr)
print ("Maximum Obtainable Value is " + str(cut(arr, size)))

#idea from http://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/
