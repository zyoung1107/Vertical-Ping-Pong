WIDTH = 500
HEIGHT = 500

ball = Rect((400, 150), (20, 20))
paddle = Rect((480, 200), (20, 60))
vx = 4
vy = 4

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, "red")
    screen.draw.filled_rect(paddle, "white")

def update():
    global vx, vy
    ball.x += vx
    ball.y += vy
    if ball.top < 0 or ball.bottom > HEIGHT:
        vy = -vy
    if ball.colliderect(paddle) or ball.left < 0:
        vx = -vx
    if ball.left > HEIGHT:
        exit()
    if(keyboard.down):
        paddle.y += 2
    elif(keyboard.up):
        paddle.y -= 2


ball.