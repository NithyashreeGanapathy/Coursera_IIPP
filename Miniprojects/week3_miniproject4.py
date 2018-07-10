# template for "Stopwatch: The Game"
import simplegui
# define global variables
millisecs = 0
no_of_wins =0
attempts_made =0
    

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    millisec = t % 10
    sec = int(t/10)%60
    minutes = int(t/10)/60
    if(sec<10):
        sec_output_string="0"+str(sec);
    else:
        sec_output_string=str(sec);
    return str(minutes)+":"+sec_output_string+"."+str(millisec);  
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_stopwatch():
    timer.start()
    
def stop_stopwatch():
    timer.stop()
    global no_of_wins , attempts_made
    if millisecs%10==0:
        no_of_wins+=1
    attempts_made+=1
    
def reset_stopwatch():
    timer.stop()
    global no_of_wins,attempts_made,millisecs
    no_of_wins = 0
    attempts_made = 0
    millisecs = 0
    

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global millisecs;
    millisecs +=1;
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(millisecs), (150,300), 200, "Green");
    canvas.draw_text(str(no_of_wins)+"/"+str(attempts_made),(340,50),50,"Yellow");
    
# create frame
frame = simplegui.create_frame("STOPWATCH",700,500)

# register event handlers
frame.add_button("START",start_stopwatch,200)
frame.add_button("STOP",stop_stopwatch,200)
frame.add_button("RESET",reset_stopwatch,200)
timer = simplegui.create_timer(100,timer_handler)
frame.set_draw_handler(draw_handler);

# start frame
frame.start()

# Please remember to review the grading rubric
