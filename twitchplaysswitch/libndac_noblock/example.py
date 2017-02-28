import time
import switch_ctrl

def sleep_ms(delay_ms):
    time.sleep(float(delay_ms)/1000)

"""
buttons:
arg       meaning
-----------------------
a       A button
b       B button
x       X button
y       Y button
du      d-pad up
dd      d-pad down
dl      d-pad left
dr      d-pad right
ls      left shoulder
rs      right shoulder
zl		ZL button
zr		ZR button
sl 		SL button
sr 		SR button		
sbl 	left joycon stick button
sbr		right joycon stick button
syncl	left joycon sync button
syncr	right joycon sync button
+		plus button
-		minus button
h 		home button
cap 	capture button

analog sticks:
X: 0 Right, 127 Neutral, 255 Left
Y: 0 Down, 127 Neutral, 255 Up
"""

switch = switch_ctrl.switch_ctrl("COM4")
switch.connect()
count = 0
try:
	while 1:
		count += 1
		if switch.cmd_available():
			switch.button_click(33, "dd")
			# sleep_ms(0.5)
except KeyboardInterrupt:
	switch.release_all()

"""
usb_recv_buf.last_recv
last reset should clear it as well
"""