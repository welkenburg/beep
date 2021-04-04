import winsound as w
import time

message = input("message : ").lower()
# message = "hello world".lower()
noteDuration = 160

for l in message:
	print(l, end="")
	try:
		w.Beep((ord(l) - 96) * 100, noteDuration)
	except:
		time.sleep(noteDuration/200)