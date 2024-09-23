import serial
import csv
import time

# assigned com port
arduino = 'COM3'

# open CSV file
filename = input("Enter CSV File Name (don't add .csv): ")
csvFile = open(filename, "w", newline='')
writer = csv.writer(csvFile)
writer.writerow(['Unix Timestamp','Analog Read (1023)','Calculated Amperage'])

# initialize serial com
serialPort = serial.Serial(arduino, 115200)

# reset ardino
serialPort.setDTR(False)
time.sleep(1)
serialPort.flushInput()
serialPort.setDTR(True)

# loop for data
testPointsAmount = 100
for i in range(testPointsAmount):
    try:
        read = serialPort.readline()
        decoded_read = read.decocde("utf-8").strip('\r\n')

        writer.writerow(decoded_read)
    except:
        print("Erorr: Line was not recorded.")
