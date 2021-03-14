import time

def loading():
	x = 0
	while x < 4:
	    s = "Loading" + "." * x
	    print (s, end="\r")
	    time.sleep(1)
	    x = x + 1

def progress():
	i = 0
	while i <= 10:
		p = (i / 10) * 100
		print (str(p) + "%", end="\r")
		time.sleep(1)
		i = i + 1

def progress_bar():
	i = 0
	while i <= 10:
		p = (i / 10) * 100
		print("[" + "#" * i + "]" + " " + str(p) + "%", end="\r")
		time.sleep(1)
		i = i + 1

loading()
print('\n')
progress()
print('\n')
progress_bar()