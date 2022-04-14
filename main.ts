let stred = [2, 2]
let A = [2, 1]
let B = [0, 2]
let C = [3, 2]
basic.forever(function on_forever() {
    display()
})
function display() {
    
    basic.clearScreen()
    led.plotBrightness(stred[0], stred[1], 100)
    led.plot(A[0], A[1])
    led.plot(B[0], B[1])
    led.plot(C[0], C[1])
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    otaceni(1)
})
function otaceni(y: number) {
    
    A.reverse()
    A[y] = Math.abs(A[y] - 4)
    B.reverse()
    B[y] = Math.abs(B[y] - 4)
    C.reverse()
    C[y] = Math.abs(C[y] - 4)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    otaceni(0)
})
