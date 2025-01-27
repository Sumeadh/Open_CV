import cv2
import numpy as np
import random
import math
import socket
'''

# Define the server's IP address and port
server_ip = '0.0.0.0'  # Listen on all available network interfaces
server_port = 12345  # Choose a port number (e.g., 12345)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server IP and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)  # Allow one client to connect

print(f"Server is listening on {server_ip}:{server_port}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Provide data to the client
data_to_send = "This is the data from the Raspberry Pi server."
client_socket.send(data_to_send.encode())

# Close the connection
client_socket.close()
server_socket.close()
'''
background = np.zeros((1000, 1000, 3), dtype=np.uint8)

cnt=0
def mouse_callback(event, x, y, flags, param):
    global cnt
    if event == cv2.EVENT_LBUTTONDOWN and cnt<2:
        cv2.circle(background, (x,y), 10, (255,0,0), -1)
        cnt+=1


while True:
    cv2.imshow('Image', background)
    cv2.setMouseCallback("Image", mouse_callback)
    key = cv2.waitKey(30) & 0xFF
    if  key== ord('q') or key==27:
        break
cv2.destroyAllWindows()

#object_height, object_width, _ = object_image.shape