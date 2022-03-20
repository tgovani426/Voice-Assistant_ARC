import winsound
import datefinder
import datetime

def alarm(text):
    global t
    date_time = datefinder.find_dates(text)
    for t in date_time:
        print(t)
    stringA = str(t)
    timeA = stringA[11:]
    hourA = int(timeA[:-6])
    minA = int(timeA[3:-3])
    print(hourA,minA)

    while True:

        print("your alarm is set.")
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound("C:\\Users\\Tirth\\Desktop\\HTML\\Nmimsmpstme_anthem.ogg",winsound.SND_LOOP,)
            elif minA <datetime.datetime.now().minute:
                break



alarm("set alarm for 8:24 pm")
