#Bubble Sort Implementation and Visualization using 

def sorting_algorithm():
    array = []
    n = 0
    global iterations
    iterations = 0
    input_array = input("Please type your list seperated by commas:\n")
    array = input_array.split(sep= ",")
    l = len(array)
    for j in range(l):
        array[j]=int(array[j])
    finished = False
    while finished == False:
        finished = True
        for i in range(l-n-1):
            iterations += 1
            if array[i] > array[i+1]:
                
                array[i], array[i+1] = array[i+1], array[i]
                finished = False
        n +=1
    return array

print("The sorted array is:", sorting_algorithm())
print(f"It took {iterations} iterations.")
end = input()