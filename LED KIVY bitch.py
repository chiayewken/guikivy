from RPi import GPIO
from firebase import firebase

token='Rkjycs92g1cEzYmtniTtYfNvt8UsSAtovgJv9jGy'
url='https://guiwithkivy-48023.firebaseio.com/'

firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':23, 'red':24}

GPIO.setup(ledcolor.values(), GPIO.OUT)

def set_led(ledno, status):
    GPIO.output(ledno,status)

while True:
    # get firebase data and call setLED
    # states of yellow and red button (if not assigned yet
    # will be 'normal', 'down', or None
    red = firebase.get('/red')
    yellow = firebase.get('/yellow')
    
    if yellow == 'normal' or yellow == None:
        set_led(23,GPIO.LOW)
    elif yellow == 'down':
        set_led(23,GPIO.HIGH)
    if red == 'normal' or red == None:
        set_led(24,GPIO.LOW)
    elif red == 'down':
        set_led(24,GPIO.HIGH)
        
        
