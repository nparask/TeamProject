#Bubble Sort Implementation and Visualization using 
import random
import turtle
iterations = 0
array = []
while True:
    choice = input("To generate a random array of random lenght press 1 and to give a certain array press 2: ")
    if choice == "1":
        try:
            input_array_lenght = int(input("Please type the lenght of the array you want to generate"))
            random_array(input_array_lenght)
            break
        except:
            print("Please input a corrent upper end for the array")
    elif choice == "2":
        try:
            input_array = input("Please type your list seperated by commas:\n")
            array = input_array.split(sep= ",")
        except:
            print("Please do as told ffs")
        break
    elif choice == "":
        break
    else:
        print("Please type 1,2 or press Enter")






def random_array(l):
    global array
    for i in range(0, l):
        array.append(random.randint(0,9999))
    print(array)
    return array

def sorting_algorithm():
    n = 0
    l = len(array)
    for j in range(l):
        array[j]=int(array[j])
    finished = False
    global iterations
    iterations = 0
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