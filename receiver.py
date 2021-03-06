import time
import datetime
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=57600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

# serial open
ser.isOpen()

# sys get version
out = ''
ser.write("sys get ver\r\n")
time.sleep(1)
ts = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S ')
while ser.inWaiting() > 0:
	out += ser.read(1)
if out != '':
	print ts + "sys get ver: " + out,

# set watchdog timer to 0 = infinite
out = ''
ser.write("radio set wdt 0\r\n")
time.sleep(1)
ts = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S ')
while ser.inWaiting() > 0:
	out += ser.read(1)
if out != '':
	print ts + "radio set wtd: " + out,

# set power
out = ''
ser.write("radio set pwr 14\r\n")
time.sleep(1)
ts = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S ')
while ser.inWaiting() > 0:
	out += ser.read(1)
if out != '':
	print ts + "radio set power: " + out,

while 1:
	out = ''
	ser.write("mac pause\r\n")
	time.sleep(1)
	while ser.inWaiting() > 0:
		ser.read(1)

	time.sleep(2)

	ser.write("radio rx 0\r\n")
	time.sleep(1)
	while ser.inWaiting() > 0:
		ser.read(1)

	while 1:	
		time.sleep(1)
		timestamp_formated = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S ')
		while ser.inWaiting() > 0:
			out += ser.read(1)
		if out != '':
			print timestamp_formated + out,
			break

# exiting
print "exiting\r\n"
ser.close()
exit()