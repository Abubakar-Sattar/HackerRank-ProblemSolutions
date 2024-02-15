l = int(input("length of the array: "))
array = []

for i in range(l):
    e = input(f"insert the {i + 1}° number of the array: ")
    array.append(int(e))

sum = 0
for e in array:
    sum += e
    
print("The sum of the array is " + str(sum))
