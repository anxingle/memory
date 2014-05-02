



# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui 
import random

# helper function to initialize globals
def new_game():
    card_deck()

def card_deck():
    global deck
    set1 = [x for x in xrange(9)]
    set2 = [x for x in xrange(9)]
    deck = set1 + set2
    random.shuffle(deck)

# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    index = 0
    canvas.draw_polygon([(0, 0), (900, 0), (900, 100), (0, 100)], 5, 'Black', 'Red')
    for x in xrange(0, 900, 50):
        canvas.draw_line((x, 0), (x, 100), 5, 'Black')
        canvas.draw_text(str(deck[index]), [x + 15, 60], 36, 'Black', 'monospace')
        index += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 900, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()

frame.start()


# Always remember to review the grading rubric