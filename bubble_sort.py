#Bubble Sort Implementation and Visualization using 
array = []
iterations = 0
input_array = input("Please type your list seperated by commas:\n")
array = input_array.split(sep= ",")
array = [41,1241,12,412412,12,4124124,12,235,34634,6346,21,126,7,23,1245,235,162,126,2136,1236123,12361236,1263,12367,123,1234,12356,72347,1234,2347,21235,612]
print(array)
l = len(array)
print(l)
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