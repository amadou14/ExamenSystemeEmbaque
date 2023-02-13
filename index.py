import sched
import time
import datetime


# -*- coding: utf-8 -*-

# Definir le fichier qui contient les taches :
fichier = open("nom du fichier ", "a")

# defining the scheduler
s = sched.scheduler(time.time, time.sleep)

nb_wheels = 4
nb_engines = 3
# definir nombre de wheels 
nb_roues = 4
nb_moteurs = 1

# definir les deux pompes 

def pump1(sc):
    # plein :
    if nb_wheels >= nb_engines * 4:
        priority = 0
    else:
        priority = 2
    time.sleep(5)
    print(datetime.datetime.now().strftime(
        "%H:%M:%S") + " : pump1")
    fichier.write(datetime.datetime.now().strftime(
        "%H:%M:%S") + " : pump1" + "\n")
    s.enter(5, priority, 10, pump1, (sc,))
    time.sleep(2)
    print(datetime.datetime.now().strftime(
        "%H:%M:%S") + " : pum1")
    fichier.write(datetime.datetime.now().strftime(
        "%H:%M:%S") + " : pump1" + "\n")


def pump2(sc):
    # plein :
    if nb_wheels >= nb_engines * 4:
        priority = 0
    else:
        priority = 2
    time.sleep(15)
    print(datetime.datetime.now().strftime("%H:%M:%S") +
          " : pump2")
    fichier.write(datetime.datetime.now().strftime(
        "%H:%M:%S") + " : pump2" + "\n")
    s.enter(15, priority, 20, pump2, (sc,))
    time.sleep(3)
    print(datetime.datetime.now().strftime(
        "%H:%M:%S") + " : pump2")
    fichier.write(datetime.datetime.now().strftime(
        "%H:%M:%S") + " : pump2" + "\n")


# definir  les taches   de la machine  il exite deux machines 
def machine1(sc):
    time.sleep(5)
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : machine 1")
    fichier.write(datetime.datetime.now().strftime("%H:%M:%S") + " : machine 1" + "\n")
    if nb_roues/4 > nb_moteurs:
        s.enter(5, 1, 25, machine1, (sc,))
    else:
        s.enter(5, 2, 25, machine1, (sc,))
    time.sleep(5)
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : machine 1")
    fichier.write(datetime.datetime.now().strftime("%H:%M:%S") + " : machine 1" + "\n")

def machine2(sc):
    time.sleep(5)
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : machine 2")
    fichier.write(datetime.datetime.now().strftime("%H:%M:%S") + " : machine 2" + "\n")
    if nb_roues/4 < nb_moteurs:
        s.enter(5, 1, 5, machine2, (sc,))
    else:
        s.enter(5, 2, 5, machine2, (sc,))
    time.sleep(5)
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : machine 2")
    fichier.write(datetime.datetime.now().strftime("%H:%M:%S") + " : machine 2" + "\n")


def main():
    s.enter(0, 1, pump1, (s,))
    s.enter(0, 1, pump2, (s,))
    s.enter(0, 1, machine1, (s,))
    s.enter(0, 1, machine2, (s,))
    s.run()


# calling the main function
if __name__ == "__main__":
    main()
