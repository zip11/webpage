import time
import smbus
import logx
import logging

import host_status as host


BUS = smbus.SMBus(1)
LCD_ADDR = 0x27
BLEN = 1 #turn on/off background light

def turn_light(key):
	global BLEN
	BLEN = key
	if key ==1 :
		BUS.write_byte(LCD_ADDR ,0x08)
		logging.info('LCD executed turn on BLight')
	else:
		BUS.write_byte(LCD_ADDR ,0x00)
		logging.info('LCD executed turn off BLight')

def write_word(addr, data):
	global BLEN
	temp = data
	if BLEN == 1:
		temp |= 0x08
	else:
		temp &= 0xF7
	BUS.write_byte(addr ,temp)

def send_command(comm):
	# Send bit7-4 firstly
	buf = comm & 0xF0
	buf |= 0x04               # RS = 0, RW = 0, EN = 1
	write_word(LCD_ADDR ,buf)
	time.sleep(0.002)
	buf &= 0xFB               # Make EN = 0
	write_word(LCD_ADDR ,buf)
	
	# Send bit3-0 secondly
	buf = (comm & 0x0F) << 4
	buf |= 0x04               # RS = 0, RW = 0, EN = 1
	write_word(LCD_ADDR ,buf)
	time.sleep(0.002)
	buf &= 0xFB               # Make EN = 0
	write_word(LCD_ADDR ,buf)

def send_data(data):
	# Send bit7-4 firstly
	buf = data & 0xF0
	buf |= 0x05               # RS = 1, RW = 0, EN = 1
	write_word(LCD_ADDR ,buf)
	time.sleep(0.002)
	buf &= 0xFB               # Make EN = 0
	write_word(LCD_ADDR ,buf)
	
	# Send bit3-0 secondly
	buf = (data & 0x0F) << 4
	buf |= 0x05               # RS = 1, RW = 0, EN = 1
	write_word(LCD_ADDR ,buf)
	time.sleep(0.002)
	buf &= 0xFB               # Make EN = 0
	write_word(LCD_ADDR ,buf)

def init_lcd():
	try:
		send_command(0x33) # Must initialize to 8-line mode at first
		time.sleep(0.005)
		send_command(0x32) # Then initialize to 4-line mode
		time.sleep(0.005)
		send_command(0x28) # 2 Lines & 5*7 dots
		time.sleep(0.005)
		send_command(0x0C) # Enable display without cursor
		time.sleep(0.005)
		send_command(0x01) # Clear Screen
		logging.info('LCD init over')
		BUS.write_byte(LCD_ADDR ,0x08)
		logging.info('LCD turning on BLight')
	except:
		return False
	else:
		return True

def clear_lcd():
	send_command(0x01) # Clear Screen

def print_lcd(x, y, str):
	if x < 0:
		x = 0
	if x > 15:
		x = 15
	if y <0:
		y = 0
	if y > 1:
		y = 1

	# Move cursor
	addr = 0x80 + 0x40 * y + x
	send_command(addr)
	
	for chr in str:
		send_data(ord(chr))

if __name__ == '__main__':
	
	init_lcd()

	ipaddr = host.get_ip_address('192.168')
	ipaddr = "IP:" + ipaddr

	uptime = host.get_up_time()

	

	# print_lcd(0, 0, ipaddr)
	# print_lcd(0, 1, uptime)

	# turn_light(0)
	yd = 0

	while True:

		# speed

		nowtime , speednow = host.getNet()

		

		# change 1601 text
		yd =  yd + 1 

		if(yd==1):
			dyh = ipaddr + '  '

		elif(yd==2):
			dyh = host.cpuper()
		
		elif(yd==3):
			dyh = 'CPU TEMP:' + host.cputemp() +'C '
			yd = 0

		speednow = speednow + ' '

		print_lcd(0, 0, dyh)
		print_lcd(0, 1, speednow)

		time.sleep(1)
		

