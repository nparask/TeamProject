#Bubble Sort Implementation and Visualization using 
array = []
n = 0
iterations = 0
input_array = input("Please type your list seperated by commas:\n")
array = input_array.split(sep= ",")
print(array)
l = len(array)
for j in range(l):
    array[j]=int(array[j])
print(array)
finished = False
while finished == False:
    finished = True
    for i in range(l-n-1):
        iterations += 1
        if array[i] > array[i+1]:
            
            array[i], array[i+1] = array[i+1], array[i]
            finished = False
    n +=1
    
print(array)
print(iterations)
end = input()