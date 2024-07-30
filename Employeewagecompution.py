import random

def CheckAttendance():
    attendnce =random.choice((0,1))
    print(attendnce)

    if attendnce == 1:
        print(f"the employe is present")
    else:
        print(f"the employe is absent")
    

CheckAttendance()