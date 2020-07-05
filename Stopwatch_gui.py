#Stopwatch second attempt

from guizero import*

window = App(title = 'Stopwatch', width = '600', height = '200', bg = 'black')

def button ():
    if startbutton.text == 'START':
        startbutton.text = 'STOP'
        startbutton.text_color = 'red'
    elif startbutton.text == 'STOP':
         startbutton.text = 'START'
         startbutton.text_color = 'green'
        
def counter():
    if startbutton.text == 'STOP':
        mseconds1.value = int(mseconds1.value) + 1
    if mseconds1.value == '10':
        mseconds1.value = int(mseconds1.value) - 10
        mseconds10.value = int(mseconds10.value) + 1
    if mseconds10.value == '10':
        mseconds10.value = int(mseconds10.value) - 10
        seconds1.value = int(seconds1.value) + 1
    if seconds1.value == '10':
        seconds1.value = int(seconds1.value) - 10
        seconds10.value = int(seconds10.value) + 1
    if seconds10.value == '6':
        seconds10.value = int(seconds10.value) - 6
        minutes1.value = int(minutes1.value) + 1
    if minutes1.value == '10':
        minutes1.value = int(minutes1.value) - 10
        minutes10.value = int(minutes10.value) + 1
    if minutes10.value == '6':
        minutes10.value = int(minutes10.value) - 6

        
def resetcounter():
    startbutton.text = 'START'
    mseconds1.value = '0'
    mseconds10.value = '0'
    seconds1.value = '0'
    seconds10.value = '0'
    minutes1.value = '0'
    minutes10.value = '0'



#Buttons
startbutton = PushButton (window, text = 'START', align = 'left', command = button)
startbutton.text_color = 'green'
reset = PushButton (window, text = 'RESET', align = 'left', command = resetcounter)
reset.text_color = 'cyan'


#Milliseconds

mseconds1 = Text (window, text = '0', size = '80', align = 'right', color = 'dim grey')
mseconds1.repeat (10, counter)
mseconds10 = Text (window, text = '0', size = '80', align = 'right', color = 'dim grey')

#Seconds

colon = Text (window, text = ':', size = '80', align = 'right', color = 'silver')
seconds1 = Text (window, text = '0', size = '80', align = 'right', color = 'white')
seconds10 = Text (window, text = '0', size = '80', align = 'right', color = 'white')

#Minutes

colon2 = Text (window, text = ':', size = '80', align = 'right', color = 'silver')
minutes1 = Text (window, text = '0', size = '80', align = 'right', color = 'white')
minutes10 = Text (window, text = '0', size = '80', align = 'right', color = 'white')

window.display()
