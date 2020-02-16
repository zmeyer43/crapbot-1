#!/usr/bin/env python3
import time
import signal
import rccomms

done = False
def stopme(sig, _):
  done = True
signal.signal(signal.SIGTERM, stopme)

arduino = rccomms.RCComms()
arduino.connect()
while not done:
  for i in range(40,121):
    steer, speed = i, i
    print(steer,speed)
    arduino.write(steer, speed, throttleHz=100.0)
    time.sleep(0.9)
arduino.disconnect()
time.sleep(1)
