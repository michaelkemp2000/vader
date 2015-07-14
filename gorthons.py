# Gorgon's Attack!
from sys import exit
from randow import randint

prompt = "-->"

#<--------------------MAP-------------------------------------->

class Map(object):

	scenes = {'central_corridor': CentralCorridor(), 'Lasew...'}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		

#<-------------------SCENES-------------------------------------->

class Scene(object):

	def enter(self):
		print "This scene is noy yet configured.  Subclass it and implement enter()."

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
		pass

class Planet(Scene):

	def enter(self):
		pass

class CentralCorridor(Scene):

	def enter(self):
		print '''\nGorthons have invaded your ship and its completly incapacitated.\n
You are the last surviving crew member and ou have learned of their plans to nuke your home planet below!\n
You must stop the Gorthons!\n
Your mission is to get the neutron destruct bomb from the weo'''
		print "Are your ready to play (y / n)?"
		start = raw_input(prompt)
		if start == 'N' or 'n':
			exit(1)
		elif start == 'Y' or 'y':
			print '''You find yourself in a central corridor, the door on the right is to the Armory has a gorthon guarding.
		The door on the left to the escape pod room is not guard and the door at the end of the corridor which is to the Bridge
		is guarded by an extremly large Gorthon.  Type \'A\' for Armory, \'B\' for Bridge or \'E\' for Escape Pod.'''
		cc_opt = raw_input(prompt)
		else:
			print "I'm not sure what that is, please enter y or n"
		

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

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

#<---------------------ENGINE--------------------------------------->

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		curent_scene = self.scene_map.opening_scene()

		while True:
			print "\n-------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

	def quit(self):
		pass

	def die(self):
		pass

	def battle(self):
		pass

	def escape(self):
		pass

	def move(self):
		pass

	def collect(self):
		pass

	def use(self):
		pass

	def save(self):
		pass

#<----------------MAIN------------------------>

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.opening_scene()
a_game.play()
