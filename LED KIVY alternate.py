from RPi import GPIO
from firebase import firebase

token='Rkjycs92g1cEzYmtniTtYfNvt8UsSAtovgJv9jGy'
url='https://guiwithkivy-48023.firebaseio.com/'

firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':20, 'red':21}

GPIO.setup(ledcolor.values(), GPIO.OUT)

def set_led(ledno, status):
    # you can use this to set the LED on or off
    GPIO.output(ledno, status)

while True:
    # get firebase data and call setLED
    # states of yellow and red button
    # will be 'normal', 'down', or None (if not assigned yet)
    yellow = firebase.get('/yellow')
    red = firebase.get('/red')
    
    if yellow == 'normal' or yellow == None:
        set_led(ledcolor['yellow'], GPIO.LOW)
    else:
        set_led(ledcolor['yellow'], GPIO.HIGH)
        
    if red == 'normal' or red == None:
        set_led(ledcolor['red'], GPIO.LOW)
    else:
        set_led(ledcolor['red'], GPIO.HIGH)