#Bubble Sort Implementation and Visualization using 
array = []
iterations = 0
input_array = input("Please type your list seperated by commas:\n")
array = input_array.split(sep= ",")
print(array)
l = len(array)
for j in range(l):
    array[j]=int(array[j])
finished = False
while finished == False:
    finished = True
    for i in range(l-1):
        iterations += 1
        if array[i] > array[i+1]:
            
            array[i], array[i+1] = array[i+1], array[i]
            finished = False
    
print(array)
print(iterations)