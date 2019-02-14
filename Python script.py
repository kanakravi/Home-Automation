import json
#import RPi.GPIO as GPIO
import time

from firebase import firebase
i = 0
j = 0
k = 0
#GPIO.setmode(GPIO.BCM)
#pinList = [2, 3, 4, 17]
#for i in pinList:
#	GPIO.setup(i, GPIO.OUT)
#	GPIO.output(i, GPIO.HIGH)
firebase = firebase.FirebaseApplication('https://home-automation-7c9dd.firebaseio.com/', None)
try:
	while(True):
		result = firebase.get('/Users/chyGCK6nsbRjyHYOhh56GrSJuAJ3','appliances')
		for x in xrange(len(result)):
			appliance = json.dumps(result[x]['addappliance'], sort_keys=True, indent=4)[1:-1]
			status = json.dumps(result[x]['status'], sort_keys=True, indent=4)[1:-1]
			count = json.dumps(result[x]['count'], sort_keys=True, indent=4)
			print appliance
			print status
			print count
			if appliance == 'bulb' :
				if status == 'on' :
#					GPIO.output(2, GPIO,LOW)
					print "Bulb On"
					i=int(count)
					i += 1
					print i
					firebase.put('/Users/chyGCK6nsbRjyHYOhh56GrSJuAJ3/appliances/1','count',i)
				else:
					print "Bulb Off"
			if appliance == 'charger' :
				if status == 'on' :
#					GPIO.output(2, GPIO,LOW)
					print "Charger On"
					j=int(count)
					j += 1
					print j
					firebase.put('/Users/chyGCK6nsbRjyHYOhh56GrSJuAJ3/appliances/2','count',j)
				else:
					print "Charger Off"
			if appliance == 'fan' :
				if status == 'on' :
#					GPIO.output(2, GPIO,LOW)
					print "Fan On"
					k=int(count)
					k += 1
					print k
					firebase.put('/Users/chyGCK6nsbRjyHYOhh56GrSJuAJ3/appliances/0','count',k)
				else:
					print "Fan Off"
except KeyboardInterrupt:
	print "  Quit  "
	GPIO.cleanup()
					
