from lolapikey import lolapikey
from riotwatcher import RiotWatcher
import time
import pymongo

loldb = pymongo.MongoClient().local.loldata

print "loaded mongodb"

lol = RiotWatcher(lolapikey)

print "loaded lolapi key"

comrade = lol.get_summoner(name='wray')

print "gotchu wraywray"

time.sleep(1)

thedata = []

index = 0

while len(thedata)<800:
	try:
		thedata.append(lol.get_match_history(comrade['id']+index))
		c+=1
	except:
		pass
	time.sleep(1)
	index+=1
	print comrade['id']+index,"\t\t"+str(len(thedata))

for i in thedata:
	loldb.insert(i)