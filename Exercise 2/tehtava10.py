# Filename tehtava10.py
# Author: Jenna Laaksovirta
# Description: Alarm clock

import time # Import time

# Create class where set required variables
class Clock:
    clockId = 0 # Clock id
    def __init__(self):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.__alarm = [0, 0, 0] # Alarmtime
        self.__armed = False
        self.id = Clock.clockId # Each time a new clock is created, a new id is created
        Clock.clockId += 1 # Add 1 in id

    # Return the time in a string
    def getTime(self):
        return(f"{self.__hours}:{self.__minutes}:{self.__seconds}")

    # Set time
    def setTime(self, hours: int, minutes: int, seconds: int):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    # Set alarm
    def setAlarm(self, hours, minutes, seconds):
        self.__alarm = [hours, minutes, seconds]

    def arm(self): # Trun alarm off or on
        self.__armed = not self.__armed # not means the opposite, here True
        if self.__armed:
            print("Alarm on")
        else:
            print("Alarm off")

    # Function ring the alarm
    def __ringAlarm(self):
        print("WAKE UP!")

    # Add one second in time
    def tick(self):
        self.__seconds += 1
        if self.__seconds >= 60:
            self.__seconds = 0
            self.__minutes += 1

        if self.__minutes >= 60:
            self.__minutes = 0
            self.__hours += 1

        if self.__hours >= 24:
            self.__hours = 0
            self.__minutes = 0
            self.__seconds = 0

        # If seconds, minutes and hours is same, then call functuon ringAlarm
        if (self.__hours == self.__alarm[0] and
            self.__minutes == self.__alarm[1] and
            self.__seconds == self.__alarm[2] and
            self.__armed):
            self.__ringAlarm()

# Create the Alarmclock
alarmClock = Clock()

# Set alarm and call setTime function.
alarmClock.setTime(23, 59, 55)

# Starts the alarm clock, if called again it will turn off the clock.
alarmClock.arm()

while True: # Stop the program ctrl + c
    print(alarmClock.getTime()) # Print the time
    alarmClock.tick() # Call tick function, which adds one second
    time.sleep(1) # The round lasts one second