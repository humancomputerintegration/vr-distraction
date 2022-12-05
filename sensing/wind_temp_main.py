import serial
import numpy as np
from datetime import datetime

PORT = "/dev/cu.usbserial-130"

board = serial.Serial(PORT)


def main():
    wind_start = False
    temp_start = False
    vib_start = False

    last_temp = 0

    while True:
        reading = str(board.readline())[2:-5]

        serReading = reading.split(" ")
        serReading = np.asarray([float(i) for i in serReading])
        print(serReading)

        if len(serReading) == 3:
            temp, wind, vib = serReading
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

            if wind >= 10 and wind_start == False:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                f = open("detection.txt", "a")
                f.write(time_now)
                f.write(" ")
                f.write("wind")
                f.write("\n")
                f.close()

                wind_start = True

            if wind < 10 and wind_start == True:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                f = open("detection.txt", "a")
                f.write(time_now)
                f.write(" ")
                f.write("wind ends")
                f.write("\n")
                f.close()
                wind_start = False

            if last_temp - temp >= 0.05:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                f = open("detection.txt", "a")
                f.write(time_now)
                f.write(" ")
                f.write("temp drops")
                f.write("\n")
                f.close()

            if temp - last_temp >= 0.05:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                f = open("detection.txt", "a")
                f.write(time_now)
                f.write(" ")
                f.write("temp ups")
                f.write("\n")
                f.close()

                temp_start = True

            last_temp = temp


if __name__ == "__main__":
    main()
