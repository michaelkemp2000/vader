# Gorgon's Attack!
from sys import exit
from random import randint

#<-------------------SCENE-------------------------------------->

class Scene(object):


	def enter(self):
		print "This scene is noy yet configured.  Subclass it and implement enter()."
		exit(1)

#<---------------------ENGINE--------------------------------------->

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map # this is now the Map instance a_map that contains start_scene in a.map (central_corridor was passed #194)

	def play(self):
		print self.scene_map.start_scene #debug to see whats in in map instance start scene variable
		curent_scene = self.scene_map.opening_scene()  #4 & 7. this calles a.map opening scene function and puts the return in current_scene
		print curent_scene  #whats in current scene (think this is an instance of CentralCorridor())

		while True:
			print "\n-------------------------------BUGGER"  #8. Ok, we are getting this far
			next_scene_name = curent_scene.enter()  #9. FIX - was a typo in current scene... This seems to be the problem! calling current scene (centralCorridtor().enter) function
			print next_scene_name + ' check 1' #check whats in here! ---> getting this far.
			current_scene = self.scene_map.next_scene(next_scene_name)
			print current_scene #This seems to work up to here now with lwa object passed ....

#<-------------------SCENE-------------------------------------->

class Death(Scene):

	quips = ["You Died.  You kinda suck at this.", "Your mom would be proud if you were smarter",
			"such a luser.", 
			"I have a small puppy thats better than this."
	]

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)

class EscapePod(Scene):
	
	def enter(self):
		print "You rush through the ship desperatly trying to make it to the escape pod before the whole ship explodes."
		print "It seems like hardly any Gorthons are on the ship, so you run clear of interference."
		print "You get the the escape pod room and see five escape pods, some could be damaged but you don't have time to look."
		print "which one do you take?"

		good_pod = randint(1,5)
		guess = raw_input("[pod #]>")

		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod exscapes out into the void of space, then implodes as the hull ruptures, crushing your body."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easierly slides out into space, heading to the planet below."
			print "As it flies to the planet, you look back and see your ship explode like a bright star, taking out the Gorthon ship also."
			return 'planet'


class Planet(Scene):

	def enter(self):
		print " You land saftly on your planet only to find that its now inhabited by Gorthons #!?#.  What happened?"
		return 'finished'

class CentralCorridor(Scene):

	def enter(self):
		print '''\nYou wake up from hyper-sleep and Gorthons have invaded your ship and its completly incapacitated.\n
You are the last surviving crew member and ou have learned of their plans to nuke your home planet below!\n
You must stop the Gorthons!\n
Your mission is to get the neutron destruct bomb from the Weapons Armory put it in the Bridge
and blow up the ship, after you have accessed the escape pod and launched to the plannet below\n'''

		print "Are your ready to play (y / n)?"
		start = raw_input("-->")
		if start == 'N' or start == 'n':
			print "Your trapped on the ship you fool!  Ok you jetty yourself into space and die"
			return 'death'
		elif start == 'Y' or start == 'y':
			print '''\nYou find yourself in a central corridor, the door on the right is to the Armory has a gorthon guarding.
		The door on the left to the escape pod room is not guard and the door at the end of the corridor which is to the Bridge
		is guarded by an extremly large Gorthon.  Type \'A\' for Armory, \'B\' for Bridge or \'E\' for Escape Pod.'''
			cc_opt = raw_input("-->")
			if cc_opt == 'a' or cc_opt == 'A':
				return 'lwa'
			elif cc_opt == 'b' or cc_opt == 'B':
				return 'bridge'
			elif cc_opt == 'e' or cc_opt == 'E':
				return 'escape_pod'
			else:
				print "DOES NOT COMPUTE!"
				return 'central_corridor'
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print '''You do a dive roll into the Weapons Armory, crouch and scan the room for more Gorthons that might be hiding.
It's dead quite, too quite.\n
You stand up and run to the far side of the room and find the neutron bomb container.  There is a keypad lock on the box
any you need the code to get thebomb out\n
If you get the code wrong 10 timesthen the lock closes forever and you can't get the bomb.  The code is 3 digits.\n'''

		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]>")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]>")

		if guess == code:
			print '''The container clicks open and the seal breaks, letting gas out.\n
You grab the neutron bomb and run as fast as you can to the bridge, where you must plance it in the right spot.\n'''
			return 'the_bridge'

		else:
			print '''The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together.\n
You decide to sit there for a while, and finally Gorthans blow up you home planet below and your ship, you die.\n'''
			return 'death'


class TheBridge(Scene):
	def enter(self):
		print '''You burst into the Bridge with the neutron destruction bomb under your arm and surprise 5 Gorthons who are trying to
take control of the ship.\n
They haven\'t taken thier weapons out yet, and they see the active bomb under your arm and don't want to set it off.\n
Do you \'a\',throw the bomb or \'b\', slowly place the bomb'''
		action = raw_input(prompt)

		if action == 'a' or 'A':
			print "In a panic you throw the bomb and the group of Gorthons and make a leap for the door."
			print "Right as you drop it a Gorthon shoots you right in the back, killing you."
			print "As you die, you see another Gorthon frantically trying to disarm the bomb."
			print "You die knowing that they will probably blow up when it goes off."
			return 'death'

		elif action == 'b' or 'B':
			print "You point your blaster at the bomb under your arm and the Gorthons put thier hands up and start to sweat"
			print "You inch backwards to the door, open it, and then carefully place the bomb on the floor."
			print "You then jump back through the door, punch the close button abd blast the lock so the Gorthons cant get out."
			print "Now the bomb is placed, you run to the escape pod to get off this tin."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"


#<-------------------------OTHER THINGS---------------------------->


class Being(object):
	def __init__(self, HP, AP):
		pass

class Hero(Being):
	def __init__(self, health):
		pass

class Alien(Being):
	def __init__(self, health):
		pass


#<--------------------MAP-------------------------------------->

class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'lwa': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'planet': Planet(),
		'death': Death()
		}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		print scene_name + ' check 2'
		return Map.scenes.get(scene_name) # 6.this looks up scene name in dict, originally central corridor and returns CentralCorridor()

	def opening_scene(self):
		print self.start_scene  # debug to show me whats in amap start_scene (should be central corridor)
		return self.next_scene(self.start_scene) #5. this calles a.map next scene function and puts the return to output to current scene in play function (#186)


#<----------------MAIN------------------------>

a_map = Map('central_corridor') #1.This creates an object a_map from Map and passes 'central corridor' to start_scene
a_game = Engine(a_map) #2.This creates an object a_game from Engine while passing in the instance of Map class (a_map)
a_game.play()  #3. run play function from Enginer object instance
