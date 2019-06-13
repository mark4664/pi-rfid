#!/usr/bin/python3
from time import gmtime, strftime
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        reader.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
