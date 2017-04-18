import Xlib
import Xlib.display
def findresolution():
	resolution = Xlib.display.Display().screen().root.get_geometry()
	return str(resolution.width)+"x"+str(resolution.height)
