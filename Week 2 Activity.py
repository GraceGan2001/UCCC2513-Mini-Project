#Question 3
#Propose a way to reassign arr_slice with new value without modifying my_arr

import numpy as np
my_arr = np.arange(10)
print(my_arr)
my_arr[4:7] = 25
print(my_arr)

#Assign arr_slice using copy()
arr_slice = my_arr[4:7].copy() 

#Change the first element of arr_slice to -1
arr_slice[0]= -1

#Check if changes made in arr_slice will affect my_arr
print(arr_slice)
print(my_arr)



#Question 4
#Create an image as shown as the following with the help of Numpy and matplotlib modules. 
#You can arbitrarily set the dimension of the image and white circular spot at the middle. 
import matplotlib.pyplot as plt
import numpy as np

# Create a black grayscale image
image = np.zeros((200, 200), dtype="uint8")

# Calculate the coordinates of the center of the image
center_x = 200 // 2
center_y = 200 // 2

# Set the radius of the circular spot
radius = 50

# Iterate over each pixel and set white to the pixels within the circle 
for x in range(200):
    for y in range(200):
        if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
            image[x, y] = 255

# Display image
plt.imshow(image, cmap = plt.cm.gray)
plt.xticks([]), plt.yticks([])
plt.show()
