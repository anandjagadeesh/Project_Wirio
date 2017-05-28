# To be converted to a GUI

import WirioSupportAPIKit as wirio

# Authored on 20th March '17

option=4
while(option!=3):
	print " User Interface "
	print " Enter "
	print " [1] Start data collection - Mouse "
	print " [2] Hotspot Detection and Plots "
	print " [3] Exit "
	option=int(raw_input(" Enter option: "))
	if option==2:
		hda=wirio.HotspotDataAcquire()
		hda.recordHotspots()
	elif option==1:
		mda=wirio.MouseDataAcquire()
		mda.mainfunct()
	elif option==3:
		print ' Quit '

