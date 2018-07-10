# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [random.randrange(200,400)/60 ,random.randrange(120,180)/60]
    if random.randrange(0,2) == True :
        ball_vel[1] = -ball_vel[1]
    else:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    score1 = score2 = 0
    paddle1_pos = (HEIGHT - PAD_HEIGHT)/2
    paddle2_pos = (HEIGHT - PAD_HEIGHT)/2
    paddle1_vel = paddle2_vel = 0
    global LEFT,RIGHT
    spawn_ball([LEFT,RIGHT][random.randrange(0,2)])
    
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    canvas.draw_text("PONG", (220,40),50, "Pink")
    
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "cyan")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "cyan")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "cyan")
        
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,5,"Cyan", "Purple")
    
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:  
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH , paddle1_pos],[HALF_PAD_WIDTH , paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "CYan")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos],[WIDTH - HALF_PAD_WIDTH , paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "cyan")

    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos <= ball_pos[1] and ball_pos[1]<= (paddle1_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0] 
        else:   
            spawn_ball(RIGHT)   
            score2 += 1  
            
    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos+PAD_HEIGHT): 
            ball_vel[0] = - 1.1 * ball_vel[0] 
        else: 
            spawn_ball(LEFT)
            score1 += 1 
            
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-BALL_RADIUS: 
        ball_vel[1] = -ball_vel[1]
        
    

  # draw scores
    canvas.draw_text(str(score1), (150, 40), 40, "Peachpuff")
    canvas.draw_text(str(score2), (400, 40), 40, "Peachpuff")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 5  
    if key == simplegui.KEY_MAP["s"]: 
        paddle1_vel = vel
    if key == simplegui.KEY_MAP["w"]:  
        paddle1_vel = -vel   
    if key == simplegui.KEY_MAP["down"]:  
        paddle2_vel = vel
    if key == simplegui.KEY_MAP["up"]: 
        paddle2_vel = -vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0   
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
# create frame
frame = simplegui.create_frame("Pong",WIDTH,HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART", new_game,100)


# start frame
new_game()
frame.start()

