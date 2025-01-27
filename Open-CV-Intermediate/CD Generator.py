import cv2
import numpy as np
import random
import math

# Load the background image and object image
background = np.zeros((500,500,3),dtype=np.uint8)
object_image = cv2.imread('masked_tulip.jpg')
object_image=cv2.resize(object_image,(100,100))
#print(np.shape(object_image))

# Get object dimensions
object_height, object_width, _ = object_image.shape

# Initialize object properties
object_x = random.randint(0, background.shape[1] - object_width)
object_y = random.randint(0, background.shape[0] - object_height)
object_velocity = [10*math.cos(random.uniform(0, 2*math.pi)),10*math.sin(random.uniform(0, 2*math.pi))]  # Initial velocity
object_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
while True:
    # Create a copy of the background
    display = background.copy()
    
    # Update object position
    object_x += object_velocity[0]
    object_y += object_velocity[1]
    
    # Check for collisions with screen boundaries
    if object_x <= 0 or object_x >= background.shape[1] - object_width:
        object_velocity[0] = -object_velocity[0]
        object_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    if object_y <= 0 or object_y >= background.shape[0] - object_height:
        object_velocity[1] = -object_velocity[1]
        object_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Place the object on the display
    
    for y in range(object_height):
        for x in range(object_width):
            if (object_image[y, x, 0] != 0 or object_image[y, x, 1] != 0 or object_image[y, x, 2] != 0 ) and y + object_y<background.shape[0] and x + object_x<background.shape[1]:
                display[y + int(object_y), x + int(object_x)] = object_color
    
    # Display the image
    cv2.imshow('DVD Screensaver', display)
    
    # Exit on 'q' key press
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
