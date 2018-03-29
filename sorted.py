import random
import collections
import operator
import os
import console

#MULTI DIMENSIONAL SORTER FUNCTIONS

#CLEAR SCREEN
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

#GENERATE THE 9 NUMBERS THAT ENCOMPASS ALL BEING
def get_known_universe():
	ku = list(range(1, 10))
	return ku
	
#MAIN MENU
def choose_delineator():
	clear_screen()
	console.clear()
	print('Great! You can sort based on the presence of a...\n')
		
	for delineator in delineator_dict:
		if delineator_dict[delineator] == None:
			print(delineator)
		else:
			print('{} - SORTED into {} vs {}.'.format(delineator, delineator_dict[delineator][0], delineator_dict[delineator][-1]))
	
	print("\nChose one of the above options (or make up your own) to begin sorting.\n\n** OR **\n\nType 'MATCH' to see similar matches based on your sorting.\n\nType 'QUIT' to exit the universal sorting device.")

	#User Chooses Delineator	
	menu_choice = input('\n> ')
	
	return menu_choice

#GET ELEMENT TO BE SORTED
def get_sortee(ku):
	return ku.pop(random.randrange(len(ku)))

#GET ELEMENTS FOR COMPARISON
def get_options(delineator, ku):

	#See if sorted elements exist for this delineator
	try: len(delineator_dict[delineator])
	
	#If no pre-sorted elements, get options from known universe
	except TypeError:
		a = ku.pop(random.randrange(len(ku)))
		b = ku.pop(random.randrange(len(ku)))
		return a, b
		
	#Otherwise get options from pre-sorted elements
	else:
		# When initial sort created only one list
		if len(delineator_dict[delineator]) == 1:
			sample = random.sample(delineator_dict[delineator][0], 2)
		
		#When initial sort created two lists
		else:
			sample = random.sample(delineator_dict[delineator][0]|delineator_dict[delineator][1], 2)
		a = sample[0]
		b = sample[1]
		return a, b

#PRESENT SORTEE 	
def present_options(a, b, s, delineator, ku):
	clear_screen()
	console.clear()
	print('Unsorted: {}'.format(ku))
	print()
	print('Sorted: {}'.format(delineator_dict[delineator]))
	print()
	print('Delineator: {}.\n'.format(delineator))
	print('Sort: {}'.format(s))
	print('A.{} ----- B.{}?'.format(a,b))
	print('\nOptions:\nLike Both?\nLike A?\nLike B?\nLike Neither?')

#SORT
def choose_option(a, b, s, delineator):
	#ensure valid choice
	while True:
		choice = input("\n'Enter' for Both, A, B, or N)> ").lower()
		if choice != '' and choice != 'a' and choice != 'b' and choice != 'n':
			print("\nThat's an invalid choice. Try Again.\n")
		else:
			break
		
	#check for pre-existing sets
	try: 
		len(delineator_dict[delineator])	
		
		#pre-existing sets! hooray!
		if choice == '':
			if a in delineator_dict[delineator][0]:
				delineator_dict[delineator][0].update([a,b,s])
			else:
				delineator_dict[delineator][1].update([a,b,s])
			
		elif choice == 'n':
			#just one pre-existing set and sortee is unlike that set
			if len(delineator_dict[delineator]) < 2:
				delineator_dict[delineator].append(set((s,s)))
			
			#two pre-existing sets, business as usual
			else:
				if a in delineator_dict[delineator][0]:
					delineator_dict[delineator][1].add(s)
				else:
					delineator_dict[delineator][0].add(s)

		
		elif choice == 'a':
			if a in delineator_dict[delineator][0]:
				delineator_dict[delineator][0].add(s)
			else:
				delineator_dict[delineator][1].add(s)
		
		elif choice == 'b':
			if b in delineator_dict[delineator][0]:
				delineator_dict[delineator][0].add(s)
			else:
				delineator_dict[delineator][1].add(s)
		
		else: 
			print('That is not a valid choice.')
		
		
	#no pre-existing sets! delineator_dict[delineator].pop(cherry)
	except TypeError:
		if choice == '':
			delineator_dict[delineator]=[set((a, b, s))]
		
		elif choice == 'n':
			delineator_dict[delineator]=[set((a, b)), set((s, s))]
		
		elif choice == 'a':
			delineator_dict[delineator]=[set((a, s)), set((b, b))] 
		
		elif choice == 'b':
			delineator_dict[delineator]=[set((a, a)), set((b, s))] 
	
	finally:
		return delineator_dict

#######################LIGHTS ON#######################

while True:
	
	#Initial greeting
	delineator_dict = {'Closed Loop': None, 'Curve': None, 'Diagonal Line': None, 'Horizontal Line': None, 'Vertical Line': None}
	ku = get_known_universe()
	
	print('Welcome to the Universal Sorting Device.\n')
	print('This is the known Universe:\n')
	print(ku)
	print('\n(We do not acknowledge the "Cowboy-Western Universe")\n')
	
	using_app = input('Are you ready to sort? (Y/n)> ').lower()
	
	#We be sorting
	while using_app != 'n':
	
		#Main Menu #######
		menu_choice = choose_delineator()
					
		#Sorting loop for selected delineator 
		while menu_choice != 'MATCH' and menu_choice != '' and menu_choice != 'QUIT':
			
			#reset delineator, known universe
			delineator = menu_choice
			delineator_dict[delineator] = None
			ku = get_known_universe()	
			
			#Sorting Loop
			while len(ku) != 0:
				
				#Get sortee and options
				s = get_sortee(ku)
				options = get_options(delineator, ku)
				
				#Present options to user
				present_options(*options, s, delineator, ku)
				
				#User chooses option
				choose_option(*options, s, delineator)
			
			#Display final Sort
			console.clear()
			clear_screen()	
			print('** All Sorted! **')
			print('\nBased on "{}" ... you sorted the known universe into:\n'.format(delineator))
			print(delineator_dict[delineator])
			
			#Ask if satisfied
			goodjob = input('\n ** Did you do a good job? (Y/n) ** \n').lower()
			if goodjob != 'n':
				menu_choice = ''
			else:
				input("\n** That's ok. Hit 'enter' When you're ready to try again! **")
		
		#SEE MATCHES
		while menu_choice == 'MATCH' and menu_choice != '':
			
			# PROMPT FOR BASE NUMBER
			clear_screen()
			console.clear()
			ku = get_known_universe()
			print(ku)
			try:
				base = int(input("\nEnter a number to see its similar matches\n"))
			except ValueError:
				continue
			
			# GET COMBINED LIST OF SETS WITH BASE NUMBER
			combo_list = []
			for delineator in delineator_dict:
				if delineator_dict[delineator] != None:
					for set in delineator_dict[delineator]:
						if base in set:
							combo_list += set
							
			# COUNT APPEARANCE WITHIN LISTS, CREATE DICTIONARY
			match_dictionary = collections.Counter(combo_list)
			
			# USE SORTED TO GET TUPLES
			sorted_matches = list((sorted(match_dictionary.items(), key=operator.itemgetter(1), reverse=True)[1:]))
					
			for matchcount in sorted_matches:
				if matchcount[0] != base:
					print('\n{} matched on {} dileneators.'.format(*matchcount))
			
			do_more = input("\nEnter 'Exit' to return to the main menu, otherwise hit enter to continue looking at matches").lower()
			
			if do_more == 'exit':
				menu_choice = ''

		while menu_choice == 'QUIT':
			using_app = 'n'
	
	break
