
# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui 
import random

print "HELLO WORLD"

HEIGHT = 100
clicked = []


# helper function to initialize globals
def new_game():
    global state, counter
    state = 0
    counter = 0
    card_deck()
    exposed_card()

def card_deck():
    global deck
    set1 = [x for x in xrange(9)]
    set2 = [x for x in xrange(9)]
    deck = set1 + set2
    random.shuffle(deck)
    
def exposed_card():
    global exposed
    exposed = [False] * 18

# define event handlers
def click(pos):
    global exposed, state, deck, clicked, counter
    print pos[0]
    index = pos[0] // 50
    if state == 0:
        if exposed[index] != True:
            exposed[index] = True
            clicked.append(index)
            state = 1
            counter += 1
    elif state == 1:
        if exposed[index] != True:
            exposed[index] = True
            clicked.append(index)
            state = 2
            counter += 1
    else:
        state = 1
        if deck[clicked[0]] != deck[clicked[1]]:
            exposed[clicked[0]], exposed[clicked[1]] = False, False        
        if exposed[index] != True:
            counter += 1
            clicked = []
            clicked.append(index)
            exposed[index] = True


                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    global exposed
    i = 0
    canvas.draw_polygon([(0, 0), (900, 0), (900, HEIGHT), (0, HEIGHT)], 5, 'Black', 'Red')
    for x in xrange(0, 900, 50):
        canvas.draw_line((x, 0), (x, 100), 5, 'Black')
        canvas.draw_text(str(deck[i]), [x + 15, 60], 36, 'Black', 'monospace')
        card_left_side = i * 50
        card_right_side = (i + 1) * 50
        if exposed[i] == False:
#            print exposed[i]
            canvas.draw_polygon([(card_left_side, 0), (card_right_side, 0), (card_right_side, HEIGHT), (card_left_side, HEIGHT)], 5, 'Green', 'Green')
        i += 1
#        print i


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 900, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)


# get things rolling
new_game()

frame.start()


# Always remember to review the grading rubric