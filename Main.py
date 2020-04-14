import Drone
import time
from sense_hat import SenseHat
sense = SenseHat()

drone1 = Drone.Drone('192.168.10.1',8889)

drone1.connect()

#Info printed
drone1.battery()
drone1.printinfo()

######CONTROLS:#######
#3 gange på enter knappen til at takeoff og lande igen
# up/down key for at komme op/ned 20 cm, left/right key for at rotere 45 deg ccw/cw

countFlying = 0
takeoff = False

while True:
    for event in sense.stick.get_events():
        #print(event.direction, event.action)
        if event.direction == "middle" and event.action == "released" and takeoff == False:
          countFlying += 1
          print("count flying: " + str(countFlying))
          if countFlying == 3:
            drone1.takeOff()
            countFlying = 0
            takeoff = True
            break
            
        if event.direction == "middle" and event.action == "released" and takeoff == True:
          countFlying += 1
          print("count flying: " + str(countFlying))
          if countFlying == 3:
            drone1.land()
            countFlying = 0
            takeoff = False
            
        if event.direction == "up" and event.action == "released" and takeoff == True:
          drone1.up(20)
        
        if event.direction == "down" and event.action == "released" and takeoff == True:
          drone1.down(20)
          
        if event.direction == "left" and event.action == "released" and takeoff == True:
          drone1.rotateCCW(45)
          
        if event.direction == "right" and event.action == "released" and takeoff == True:
          drone1.rotateCW(45)
        
#end program
drone1.end()