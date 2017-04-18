from pynput import mouse

def move(x,y):
	print('Pointer moved to {0}'.format((x, y)))

def click(x, y, button, pressed):
	print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
	if pressed:
		x=raw_input("Stop? (y/n)")
		if 'y' in x:
			return False

def scroll(x, y, dx, dy):
	print('Scrolled {0}'.format((x, y)))

# Collect events until released
with mouse.Listener(on_move=move,on_click=click,on_scroll=scroll) as listener:
	listener.join()
