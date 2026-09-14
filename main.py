
import os
import math

sum = 0
leader = 0
leader_path = ""
drive_path = r"G:\My Drive"

for root, dirs, files in os.walk(drive_path):
    for file in files:
        currentSize = os.path.getsize(os.path.join(root, file))
        sum += currentSize
        if(leader < currentSize): 
            leader = currentSize
            leader_path = os.path.join(root, file)

print("Sum in bytes:", sum)
print("Sum in gb:", sum/10**9)

print("Leader: ", leader_path )
print("Size: ", leader)


