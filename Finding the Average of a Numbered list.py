from itertools import count
height=input("Enter Height : ")
height_spilt=height.split()
count = 0
for i in height_spilt:
    count+=1
print(count)
for y in range(count):
    height_spilt[y]= int(height_spilt[y])
total = 0
for z in height_spilt:
    total += z
avg= total/count
print("The average height is",round(avg))