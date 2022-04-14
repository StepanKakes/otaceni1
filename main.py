stred=[2,2]
A=[2,1]
B=[0,2]
C=[3,2]
def on_forever():
    display()
    
basic.forever(on_forever)
def display():
    global stred,A,B,C
    basic.clear_screen()
    led.plot_brightness(stred[0], stred[1], 100)
    led.plot(A[0],A[1])
    led.plot(B[0],B[1])
    led.plot(C[0],C[1])
def on_button_pressed_a():
    otaceni(0)
def on_button_pressed_b():
    otaceni(1)
input.on_button_pressed(Button.B, on_button_pressed_b)
def otaceni(y):
    global A, B, C
    A.reverse()
    A[y]= abs(A[y]-4)
    B.reverse()
    B[y]= abs(B[y]-4)
    C.reverse()
    C[y]= abs(C[y]-4)
    
    
    #B.reverse()
    #C.reverse()
input.on_button_pressed(Button.A, on_button_pressed_a)