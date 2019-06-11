from datetime import datetime
c= input('enter your name')
timee=datetime.now().hour
print("hello!  "+c)
if timee in range (4,12) :
    print("good morning!")
elif timee==12:
    print("good noon!")
elif timee in range(12,17):
    print("good afternoon!")
elif timee in range(17,21):
    print(" good evening!")
else:
    print(" good night!")
