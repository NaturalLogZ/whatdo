import random
import argparse
import json

DICT_PATH = '/home/lcgrout/FunProjects/whatdo/.activityDictionary'

def main():
	# Set up parser and add various arguments
	parser = argparse.ArgumentParser(prog='whatdo',
	                                 description="A program for helping you decide what to do!")
	
	parser.add_argument('-a', '--add', 
			    help="Add a new activity to the list of possibilites!" \
			         "(The weight of this activity will be the average weight of all activities.)")
	
	args = parser.parse_args()
	
	try:
		iFile = open(DICT_PATH)
	except:
		iFile = open(DICT_PATH, 'w+')
	
	try:
		activities = json.load(iFile)
	except:
		activities = dict()

	iFile.close()
	
	# We only want to select an activity if no arguments were passed
	if not any(vars(args).values()):
		if (0 == len(activities)):
			print("You don't have any activities yet!")
			return 2
	
		choice = random.choices(activities.keys(), activities.values())
	
		# Wait for user to hit enter to be sure the activity was completed
	
		# Update weights
		
	
	oFile = open(DICT_PATH, 'w+')
	json.dump(activities, oFile)
	oFile.close()
	
	return 0

if "__main__" == __name__:
	main()
