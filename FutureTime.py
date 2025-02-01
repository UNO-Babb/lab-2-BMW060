#FutureTime.py
#Name: Brennan Wood
#Date: 1/29/25
#Assignment: Lab 2 (FutureTime)

def main():
  print("\033[34mFutureTime\033[0m")
if __name__ == '__main__':
    main()


# importing date and time
import datetime

# storing to variable and showing the current time

now = datetime.datetime.now()
currentHour = str(now.hour)
currentMinute = str(now.minute)

print("\033[31mThe current time is "+currentHour.zfill(2)+":"+currentMinute.zfill(2), "\033[0m")

# asking the user for hour and minute input

print("How far in the future would you like to know the time?")
plusHour = input("Number of hours: ")
plusMinute = input("Number of minutes: ")

# Math and printing the result

futureHour = str(((int(currentHour) + int(plusHour))+int(plusMinute)//60)%24)
futureMinute = str((int(currentMinute) + int(plusMinute))%60)
print("\033[92mThe time in "+plusHour+" hours and "+plusMinute+" minutes will be "+futureHour.zfill(2)+":"+futureMinute.zfill(2)+"\033[0m")
print("**All times shown are in 24 hour style time**")
