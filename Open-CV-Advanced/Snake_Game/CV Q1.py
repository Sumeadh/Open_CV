import cv2
import numpy as np
import random 
from random import choice

class SnakePart:
  def __init__(self, front, x, y):
    self.front = front 
    self.x = x
    self.y = y

  def move(self):
    # Moves by following the part in front of it
    self.x = self.front.x
    self.y = self.front.y


class Head:
  def __init__(self, direction, x, y):
    self.direction = direction
    self.x = x
    self.y = y

  def move(self):
    # Checks what its current direction is and moves accordingly
    if self.direction == 0:
        self.x += 1
    elif self.direction == 1:
        self.y += 1
    elif self.direction == 2:
        self.x -= 1
    elif self.direction == 3:
        self.y -= 1


def display():
  # Create a blank image
  board_orginal = cv2.imread('snakewallpaper.jpg')
  board_orginal = cv2.resize(board_orginal, (BOARD_SIZE*CELL_SIZE,BOARD_SIZE*CELL_SIZE))

# Resize the background image to match the dimensions of the foreground image
  board = np.zeros((BOARD_SIZE,BOARD_SIZE,3),dtype=np.uint8)

  # Color the snake green
  for part in snake:
    if part==head:
      board[part.y, part.x] = [0, 200, 0]
    else:
      board[part.y, part.x] = [0, 255, 0]

  # Color the apple red
  board[apple_y, apple_x] = [0, 0, 255]

  # Create the arrow
  board = np.uint8(board.repeat(CELL_SIZE, 0).repeat(CELL_SIZE, 1))
  #cv2.circle(board, (apple_x*CELL_SIZE,appley*CELL_SIZE), 10, (0, 0, 255), -1)
  cv2.arrowedLine(board, ((BOARD_SIZE-5)*CELL_SIZE, (BOARD_SIZE-5)*CELL_SIZE), ((BOARD_SIZE-3)*CELL_SIZE, (BOARD_SIZE-5)*CELL_SIZE), [255, 255, 255],15,10)
  cv2.arrowedLine(board, ((BOARD_SIZE-5)*CELL_SIZE, (BOARD_SIZE-5)*CELL_SIZE), ((BOARD_SIZE-7)*CELL_SIZE, (BOARD_SIZE-5)*CELL_SIZE), [255, 255, 255],15,10)
  cv2.arrowedLine(board, ((BOARD_SIZE-5)*CELL_SIZE, (BOARD_SIZE-5)*CELL_SIZE), ((BOARD_SIZE-5)*CELL_SIZE, (BOARD_SIZE-3)*CELL_SIZE), [255, 255, 255],15, 10)
  cv2.arrowedLine(board, ((BOARD_SIZE-5)*CELL_SIZE, (BOARD_SIZE-5)*CELL_SIZE), ((BOARD_SIZE-5)*CELL_SIZE, (BOARD_SIZE-7)*CELL_SIZE), [255, 255, 255],15,10)

  text='SCORE:'+str(score)
  cv2.putText(board, text, ((BOARD_SIZE-7)*CELL_SIZE, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, [255,255,255], 2)
  #add board with background image
  blended = cv2.addWeighted(board, 1, board_orginal, 0.8, 0)
  # Display board
  cv2.imshow("Snake Game",blended )
  # np.uint8-->numpy unsigned integer(POSITIVE) within 0 to 256
  key = cv2.waitKey(int(1000/SPEED))
  # Return the key pressed. It is -1 if no key is pressed.
  return key

def win():#Initial Window
  #cv2.namedWindow("Snake Game", cv2.WINDOW_AUTOSIZE)
  board_orginal = cv2.imread('snakewallpaper.jpg')
# Resize the background image to match the dimensions of the foreground image
  board = cv2.resize(board_orginal, (BOARD_SIZE*CELL_SIZE,BOARD_SIZE*CELL_SIZE))
  text='Welcome To The Snake Game'
  cv2.putText(board, text, ((BOARD_SIZE//2-12)*CELL_SIZE, (BOARD_SIZE//2)*CELL_SIZE), cv2.FONT_HERSHEY_DUPLEX, 1.2, [10, 10, 10], 2)
  # Create the arrow
  cv2.imshow("Snake Game", board)
  cv2.waitKey(2000)# waits the screen to load for a while


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if abs(x-(BOARD_SIZE-5)*CELL_SIZE)<5:
          if (BOARD_SIZE-7)*CELL_SIZE < y < (BOARD_SIZE-5)*CELL_SIZE and head.direction != 1:
            head.direction = 3
          elif (BOARD_SIZE-5)*CELL_SIZE < y < (BOARD_SIZE-3)*CELL_SIZE and head.direction != 3:
             head.direction = 1
        if abs(y-(BOARD_SIZE-5)*CELL_SIZE) < 5:
            if (BOARD_SIZE-7)*CELL_SIZE < x < (BOARD_SIZE-5)*CELL_SIZE and head.direction != 0:
              head.direction = 2
            elif (BOARD_SIZE-5)*CELL_SIZE < x < (BOARD_SIZE-3)*CELL_SIZE and head.direction != 2:
              head.direction = 0


# Create a blank image window


if __name__ == '__main__':
  # Size of each cell in the board game
  CELL_SIZE = 20
  # Number of cells along the width in the game
  BOARD_SIZE = 45
  # Change SPEED to make the game go faster
  SPEED = 10
  # After eating an apple the snake grows by GROWTH units
  GROWTH = 2
  # Variable to track if apple is eaten
  eaten = True
  # Variable to check if the game should quit
  quit = False
  # Variable to track growth.
  grow = 0
  # Array for storing snake
  snake = []
  #To calculatee the score of player
  score=0
  # snake's head starts at the center of the board.
  head = Head(0, int((BOARD_SIZE - 1)/2), int((BOARD_SIZE - 1)/2))
  snake.append(head)
  #windows
  win()


  while True:
    # Checks if the apple is eaten and generates a new one
    if eaten:
      # Create a list of all possible locations
      s = list(range(0, BOARD_SIZE ** 2))
      # Delete cells that are part of the snake
      for part in snake:
          s.remove(part.x * BOARD_SIZE + part.y)

      # Randomly pick from one of the remaining cells
      a = random.choice(s)
      apple_x = int(a/BOARD_SIZE)
      apple_y = a % BOARD_SIZE

      eaten = False
    # Makes and displays the board
    key = display()

    if key == 8 or key == 27:
      break
    else:
        cv2.setMouseCallback("Snake Game", mouse_callback)
    # Moving the snake
    for part in snake[::-1]:
      part.move()

    # Collision rules

    if head.x < 0 or head.x > BOARD_SIZE - 1 or head.y < 0 or head.y > BOARD_SIZE - 1:
      break

    for part in snake[1:]:
      if head.x == part.x and head.y == part.y:
        quit = True
        break

    if quit:
      break

    # The snake grows graduallly over multiple frames
    if grow > 0:
      snake.append(SnakePart(snake[-1], subx, suby))
      grow -=GROWTH

    # Grows the snake when it eats an apple
    if apple_x == head.x and apple_y == head.y:
      subx = snake[-1].x
      suby = snake[-1].y
      eaten = True
      grow += GROWTH
      score+=1
