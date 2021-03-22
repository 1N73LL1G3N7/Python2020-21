# HEALTHY PROGRAMMER

from time import time
from datetime import datetime
from pygame import mixer


def alarm(musicfile, stopmsg):
    mixer.init()
    mixer.music.load(musicfile)
    mixer.music.set_volume(0.2)
    mixer.music.play()
    while True:
        reminder_stopper = input()
        if reminder_stopper == stopmsg:
            mixer.music.stop()
            break


def logs(log_message):
    with open("Healthy Programmer Log.txt", "a") as f:
        f.write(f"{datetime.now()} : {log_message} \n")


if __name__ == '__main__':
    water_init = time()
    eyes_init = time()
    exercise_init = time()
    water_timer = 3600
    eyes_timer = 1800
    physical_activity_timer = 2700
    while True:
        if time() - water_init > water_timer:
            print("Water Drinking Reminder... Enter \"Drank Water\" to stop the alarm.")
            alarm("water.mp3", "Drank Water")
            water_init = time()
            logs("Drank water")
        elif time() - eyes_init > eyes_timer:
            print("Eyes Exercise Reminder... Enter \"Done\" to stop the alarm.")
            alarm("eyes_exe.mp3", "Done")
            eyes_init = time()
            logs("Eyes Relaxed")
        elif time() - exercise_init > physical_activity_timer:
            print("Physical Activity Reminder... Enter \"Exercised\" to stop the alarm.")
            alarm("physical_exe.mp3", "Exercised")
            exercise_init = time()
            logs("Did Physical Activity")
