"""
In Flight Repairs V0.6 By D10d3
A Text Adventure

Version History:
V0.5 traversable map, inventory, and trigger-able events
V0.6 Bug Fixing, discreet inventory

This is a very simple text adventure. Each room in the map is a function that can call the functions for adjacent rooms.
All events and inventory are carried from room to room in a list called Status. Events in the
list will be a series of 1's and 0's, 1 if the event has been triggered, 0 if not. 

Plot: player wakes up from cold sleep and his ship is crippled, he needs to repair it and save the rest of his 
crew in cold sleep.

Solution: Player needs the suit to get in cargo hold, needs to get the tools in cargo hold to fix leak. needs to 
fix the engine (via a small puzzle) and get keycard to access flightdeck, and needs all of these event complete and
have possession of the keycard to access the flight deck and reset flight computer. Finally return to the cryo pod.

Reactor puzzle:
the main reactor needs to be restarted in order, first unlock the deuturium valves, then charge 
magnetic constrictors, then activate ionization lasers.

Items: 
key-card
toolbox
spacesuit

events:
hull breach repaired
engine fixed
flight computer reset.
"""

status = [100,0,0,0]	#default status: Health 100, Hull breached, Engine damaged, Flight Computer off, no inventory
						#Note: Health isn't actually used in this version, it's included for future implementation
inventory = ["uniform"]

#def room(status):					#This is the template for each room
	#room = """description"""		#This description is read now and can be printed at will later
	#print room
	#valid = False
	#while not valid:				#This is the command loop, player can keep entering commands at will
		#choice = raw_input ('> ')
		#choice = choice.lower()
		#if "statdebug" in choice:	#A debug routine that let's me see what is in Status while testing
			#print status
		#elif "look" in choice:		#Allows player ro redisplay the description
			#print room
		#elif input:				#Room specific commands
			#bla bla bla
		#else:						#General error trap for unrecognised commands
			#print "Command not recognized"
	#return status
	
def error():
	print "Your code sucks D10d3, try again"
	quit()

def statdebug(status,inventory):
			print"Status:"
			print status
			print " "
			print "Inventory:"
			print inventory
	
def crewquarters(status):
	room = """
	Crew Quarters
	This room has several bunks, a set of lockers, cryotubes set against one 
	wall and a small bathroom at the back.
	Exits: 
	<1> Common Room """
	print room
	while True:
		choice = raw_input ('> ')
		choice = choice.lower()
		if "bunk" in choice:
			print "This is no time for sleeping"
		elif "statdebug" in choice:
			statdebug(status,inventory)
		elif "compdebug" in choice:
			computer(status)
		elif "cryo" in choice and status[3] == 0:
			print "There is still work to be done before you can return to your cryotube"
		elif "cryo" in choice and status[3] == 1:
			win()
		elif "locker" in choice:
			print "Looking through the lockers reveals a space suit in one"
		elif "suit" in choice:
			print "you pull out the suit and put it on."
			inventory.append("suit")
		elif "bathroom" in choice:
			print "You don't need to go right now"
		elif choice == "1":
			commonroom(status)
		elif "look" in choice:
			print room
		elif "quit" in choice:
			print "Thank you for playing."
			quit()
		else:
			print "Command not recognized"

def commonroom(status):
	room = """
	Common Room
	This is the central living area of the ship. There is a small kitchen with
	a table and chairs securely bolted to the floor as well as several work 
	stations. Doors here lead fore and aft as well as laterally.
	The door leading aft is an airlock
	Exits: 
	<1> Starboard - Crew Quarters 
	<2> Fore - Flight Deck 
	<3> Port - Medical Bay 
	<4> Aft - Cargo Hold
	"""
	print room
	while True:
		choice = raw_input ('> ')
		choice = choice.lower()
		if choice == "1":
			crewquarters(status)
		elif "look" in choice:
			print room
		elif "quit" in choice:
			print "Thank you for playing."
			quit()
		elif "statdebug" in choice:
			statdebug(status,inventory)
		elif choice == "2":
			if "keycard" in inventory:
				print "The door lock beeps when you wave you keycard over it"
				flightdeck(status)
			elif "keycard" not in inventory:
				print 'The door will not open. The small panel next to it reads "LOCKED"'
			else:
				error()
		elif choice == "3":
			medbay(status)
		elif choice == "4":
			if "suit" in inventory and status[1]==0:
				print "You enter the airlock and cycle it. "
				print "There is a hiss and then silence as the air is pumped out"
				cargohold(status)
			elif "suit" not in inventory and status[1]==0:
				print "As the air is sucked from the airlock you regret not wearing a space suit"
				print "You asphyxiate and die"
				quit()
			elif status[1]==1:
				print "The airlock registers normal pressure and allows you to pass"
				cargohold(status)
			else:
				error()
		#...
		else:
			print "Command not recognized"

def cargohold(status):
	room = """
	Cargo Hold
	This cavernous space connects the front and back of the ship. Large crates
	are secured to the deck.	There is a rack of tools here and airlock doors 
	leading fore and aft.
	Exits:
	<1> Fore - Common Room
	<2> Aft - Engine Room """
	print room
	if status[1] == 0:
		print "There is a small hole in the hull where an asteroid has struck the ship"
	else:
		print "The repair patch is holding nicely, keeping the air where it's supposed to be"
		
	while True:
		choice = raw_input ('> ')
		choice = choice.lower()
		if choice == "1":
			print "You step into the forward airlock and cycle it"
			commonroom(status)
		elif "look" in choice:
			print room
		elif "quit" in choice:
			print "Thank you for playing."
			quit()
		elif "statdebug" in choice:
			statdebug(status,inventory)
		elif choice == "2":
			print "You step into the forward airlock and cycle it"
			engineroom(status)
		elif "repair" in choice and "tools" not in inventory:
			print "You will need tools to repair this hole"
		elif "hole" in choice and "tools" in inventory:
			if status[1]==0:
				print "Using your toolkit you apply a patch to the hole and seal it"
				print "With a hiss the life support systems pump air back into the room"
				status[1] = 1
			else:
				print"You've repaired this as well as you can at the moment"
		elif "tools" in choice and "tools" not in inventory:
			print "These tools could be useful, you get a toolbox from the rack"
			inventory.append("tools")
		elif "tools" in choice and "tools" in inventory:
			print"You're tool box should be able to repair some of the ship's damage"
		
		else:
			print "Command not recognized"

def medbay(status):
	room = """
	Med-Bay
	This is a small infirmary. There is a bed with an auto-doc built into it.
	The only door leads back into the Common Room
	Exits:
	<1> Port - Common Room"""
	print room
	while True:
		choice = raw_input ('> ')
		choice = choice.lower()
		if "statdebug" in choice:
			statdebug(status,inventory)
		elif "look" in choice:
			print room
		elif "quit" in choice:
			print "Thank you for playing."
			quit()
		elif choice == "1":
			commonroom(status)
		else:
			print "Command not recognized"
	
def flightdeck(status):
	room = """
	Flight Deck
	The main navigational and manoeuvring console is in this room. 
	A door leads aft.
	Exits:
	<1> Aft - Common Room"""
	print room
	if status[3] == 0:
		print "The navigational computer is in standby mode, it will need to be reset to continue to your destination"
	elif status[3] == 1:
		print "The navigational console is in cruise mode, the ship is under way"
	else:
		error()
	while True:
		choice = raw_input ('> ')
		choice = choice.lower()
		if "statdebug" in choice:
			statdebug(status,inventory)
		elif "look" in choice:
			print room
		elif "quit" in choice:
			print "Thank you for playing."
			quit()
		elif choice == "1":
			commonroom(status)
		#check hull breach
		elif "computer" in choice and status[3] == 0 and status[1] == 0:
			print "As you try to reset the navigational computer it gives you an error 'Hull Breach Detected'"
			print "It is still in standby mode"
		elif "reset" in choice and status[3] == 0 and status[1] == 0:
			print "As you try to reset the navigational computer it gives you an error 'Hull Breach Detected'"
			print "It is still in standby mode"
		#check engine on
		elif "computer" in choice and status[3] == 0 and status[2] == 0:
			print "As you try to reset the navigational computer it gives you an error 'Drive Currently Offline'"
			print "It is still in standby mode"
		elif "reset" in choice and status[3] == 0 and status[2] == 0:
			print "As you try to reset the navigational computer it gives you an error 'Drive Currently Offline'"
			print "It is still in standby mode"
		#all systems go
		elif "computer" in choice and status[3] == 0 and status[2] == 1 and status[1] == 1:
			print "You reset the navicomputer and reactivate the autopilot"
			status[3] = 1
		elif "reset" in choice and status[3] == 0 and status[2] == 1 and status[1] == 1:
			print "You reset the navicomputer and reactivate the autopilot"
			status[3] = 1
		#Navi already on
		elif "computer" in choice and status[3] == 1:
			print "The navicomputer is functioning correctly, there is no need to mess with it"
		elif "reset" in choice and status[3] == 1:
			print "The navicomputer is functioning correctly, there is no need to mess with it"
		else:
			print "Command not recognized"

def engineroom(status):
	room = """
	Engine Room
	This large room is filled almost entirely with machinery. Dominating the 
	center of the room is	the primary fusion reactor. The engineering control
	computer screens show a variety of metrics and updates on the engines 
	and ship systems. An airlock leads forward to the cargo hold.
	Exits:
	<1> Fore - Cargo Hold
	"""
	print room
	if status[2] == 0:
		print "There is a red flashing light on the Engineering Computer"
	else:
		print "The reactor is humming steadily."
	if "keycard" not in inventory:
		print "There is a keycard sitting on the Engineering Computer."
	else:
		print ""
	while True:
		choice = raw_input ('> ')
		choice = choice.lower()
		if "statdebug" in choice:
			statdebug(status,inventory)
		elif "look" in choice:
			print room
		elif "quit" in choice:
			print "Thank you for playing."
			quit()
		elif choice == "1":
			cargohold(status)
		elif "computer" in choice and status[2] == 0:
			computer(status)
		elif "computer" in choice and status[2] == 1:
			print "The computer is in standby mode awaiting commands from the flight computer"
		elif "keycard" in choice and "keycard" not in inventory:
			inventory.append("keycard")
			print "You pick up the keycard and slip it in a pocket"
		else:
			print "Command not recognized"

def computer(status):
	room = """
	Engineering Computer
	This computer controls the fusion drive of the ship.
	"""
	print room
	compstat = [0,0,0]
	while True:
		#Engineering Status Displays
		print " "
		print "________________________________________"
		print "|	-=SYSTEMS DISPLAY=-		|"
		if compstat[0] == 0:
			print"|  Magnetic Constrictors: OFF		|"
		elif compstat[0] ==1:
			print"|  Magnetic Constrictors: ENGAGED	|"
		else:
			error()
		if compstat[1] == 0:
			print"|  Deuterium Valves: LOCKED		|"
		elif compstat[1] ==1:
			print"|  Deuterium Valves: OPEN		|"
		else:
			error()
		if compstat[2] == 0:
			print"|  Ionization Lasers: OFF		|"
		elif compstat[2] ==1:
			print"|  Ionization Lasers: ACTIVE	|"
		else:
			error()
		print"|  System Commands:			|"
		print "|  <1> Engage Magnetic Constrictors	|"
		print "|  <2> Open Deuterium Valves		|"
		print "|  <3> Activate Ionization Lasers	|"
		print "|  <4> Log Off				|"
		print "----------------------------------------"
		print " "
		print " "
		#begin command loop and logic testing
		choice = raw_input ('ENTER COMMAND: ')
		choice = choice.lower()
		#Constrictors
		if choice == "1" and compstat[1] == 0:
			print "ERROR BAD STARTUP SEQUENCE"
			print "RESETTING SYSTEM"
			compstat = [0,0,0]
		elif choice == "1" and compstat[0] == 1:
			print "MAGNETIC CONSTRICTORS ALREADY ENGAGED"
		elif choice == "1" and compstat[1] == 1:
			print "ENGAGING MAGNETIC CONSTRICTORS"
			print "(a deep hum emanates from the machinery behind you)"
			compstat[0] = 1
		#Valves
		elif choice == "2" and compstat[1] == 0:
			print "OPENING DEUTERIUM VALVES"
			print "(you hear a series of clacks in the machinery overhead)"
			compstat[1] = 1
		elif choice == "2" and compstat[1] == 1:
			print "DEUTERIUM VALVES ALREADY OPEN"
		#Lasers
		elif choice == "3" and compstat[0] == 1 and compstat[1] == 1:
			print "IONIZATION LASERS ACTIVE"
			print "START-UP SEQUENCE COMPLETE"
			print "SYSTEMS NOMINAL AND RUNNING"
			print "DRIVE SYSTEMS READY FOR COMMANDS FROM NAVIGATION"
			status[2] = 1
			engineroom(status)
		else:
			print "ERROR BAD STARTUP SEQUENCE"
			print "RESETTING SYSTEM"
			print " "
			
			compstat = [0,0,0]

def win():
	print"""
	Having repaired the ship and set it back on it's path you return to your
	cryopod to continue your long journey. As the lights dim and the stasis 
	drugs take effect you drift off to sleep knowing the job was well done.
	
	You Win!
	Thank you for playing In Flight Repairs
	

	"""
	quit()
	
#***Game starts running here with initial description and calls the commonroom function***	
print"""
***
In Flight Repairs V0.6 by D10d3
A small text adventure
Use keywords when interacting with objects
Use <exit> numbers to change rooms
Type "look" to see the room description again
Type "quit" to leave this game
***

You awaken to a beeping sound in your cryopod. The small screen in the pod 
informs you that the ship has sustained some damage from an asteroid strike.
The main drive is offline and the navicomputer is currently in standby mode.
The computer has awakened you from cold-sleep to render repairs. 

After taking a moment to absorb this you open the cryopod and step out"""
crewquarters(status)


