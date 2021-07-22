import serial, time

arduino = serial.Serial('COM3', 9600)

onbyte=bytes("1", 'ascii')
offbyte=bytes("0", 'ascii')

while True:
    onoff=input("Type a 1 or a 0. ")

    if onoff == "1":
        arduino.write(onbyte)
        time.sleep(1)
    if onoff == "0":
        arduino.write(offbyte)
        time.sleep(1)
    if onoff == "q":
        quit()