import serial
import time
from directKeys import PressKey, ReleaseKey
from threading import Thread

A = 0x1E
B = 0x30
Z = 0x2C
S = 0x1F
ZERO = 0x0B
ONE = 0x02
TWO = 0x03


def controller(key):
    if chr(key) == 'D':
        PressKey(A)
        print("D")
        time.sleep(0.10)
        ReleaseKey(A)
    if chr(key) == 'E':
        PressKey(B)
        print("E")
        time.sleep(0.10)
        ReleaseKey(B)
    if chr(key) == 'C':
        PressKey(Z)
        print("C")
        time.sleep(0.10)
        ReleaseKey(Z)
    if chr(key) == 'B':
        PressKey(S)
        print("B")
        time.sleep(0.10)
        ReleaseKey(S)
    if chr(key) == '0':
        PressKey(ZERO)
        print("ZERO")
        time.sleep(0.10)
        ReleaseKey(ZERO)
    if chr(key) == '1':
        PressKey(ONE)
        print("ONE")
        time.sleep(0.10)
        ReleaseKey(ONE)
    if chr(key) == '2':
        PressKey(TWO)
        print("TWO")
        time.sleep(0.10)
        ReleaseKey(TWO)


def joystick():
    ser = serial.Serial(
        port='COM3',
        baudrate=115200,
        timeout=0)

    print("connected to: " + ser.portstr)

    while True:
        for line in ser.read():
            controller(line)


thread = Thread(target=joystick)
thread.start()
