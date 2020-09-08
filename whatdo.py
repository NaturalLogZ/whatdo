import random
import argparse
import json

DICT_PATH = '/home/lcgrout/FunProjects/whatdo/.activityDictionary'
INITIAL_WEIGHT = 1

def update(dictionary, key):
	dictionary[key] = dictionary[key]-1

	return dictionary[key]

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
		# If there are no activities we can't randomly choose one
		if (0 == len(activities)):
			print("You don't have any activities yet!")
			return 2
	
		randomAct = random.choices(list(activities.keys()), list(activities.values()))[0]
		print(randomAct)
	
		# Wait for user to hit enter to be sure the activity was completed
	
		# Update weights
		update(activities, randomAct)

	# Adding Activites
	if (args.add is not None):
		# Check if we are adding something already in the dictionary
		# Actually this check isn't needed by use of the setdefault method		

		avgWeight = 0
		for weight in activities.values():
			avgWeight += weight
		try:
			avgWeight = avgWeight / len(activities)
		except:
			avgWeight = INITIAL_WEIGHT

		activities.setdefault(args.add, avgWeight)



	# Write updated dictionary	
	oFile = open(DICT_PATH, 'w+')
	json.dump(activities, oFile)
	oFile.close()
	
	return 0

if "__main__" == __name__:
	main()
