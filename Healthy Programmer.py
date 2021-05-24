from datetime import datetime
from pygame import mixer
from time import time
print("              Welcome to the Initiative of making you a Healthy Programmer")
print("\nYou'll be reminded to:\nDrink Water after every hour\nRelax your Eyes after 30 minutes\nDo Physical activity every 45 minutes")

def music(file,stopper):
     mixer.init()
     mixer.music.load(file)
     mixer.music.play()
     while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def lognow(msg):
    f=open("mylogs.txt","a+")
    f.write(f"{datetime.now()} + {msg}\n")
    f.close()

if __name__ == '__main__':

    watertime=time()
    eyestime=time()
    extime=time()
    waterbreak=5
    eyesbreak=10
    exbreak=15

    while True:
        if time()-watertime>waterbreak:
            print("Time to Drink Water. Enter done to stop the alarm.")
            music('water.mp3', 'done')
            watertime = time()
            lognow("Drank water")
        if time()-eyestime>eyesbreak:
            print("Time to relax eyes. Enter done to stop the alarm.")
            music('eyes.mp3', 'done')
            eyestime = time()
            lognow("Relaxed eyes")
        if time()-extime>exbreak:
            print("Time to do activity. Enter done to stop the alarm.")
            music('physical.mp3', 'done')
            extime = time()
            lognow("Did Physical activity")









