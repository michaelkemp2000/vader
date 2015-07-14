# Gorgon's Attack!

prompt = "-->"

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass

class Scene(object):

	def enter(self):
		pass

class Being(object):
	def __init__(self, HP, AP):
		pass

class Hero(Being):
	def __init__(self, health):
		pass

class Alien(Being):
	def __init__(self, health):
		pass

class Engine(object):

	def __init__(self, scene_map):
		print '''\nGorthons have invaded your ship and its completly incapacitated.\n
You have learned of their plans to nuke your home planet below!\n
You must stop the Gorthons!\n'''


	def play(self):
		print "Are your ready to play (y / n)?"
		start = raw_input(prompt)
		if start == 'Y' or 'y':
			CentralCorridor.enter
		elif start == 'N' or 'n':
			quit
		else:
			print "I'm not sure what that is, please enter y or n"

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

class Death(Scene):

	def enter(self):
		pass

class EscapePod(Scene):
	
	def enter(self):
		pass

class Planet(Scene):

	def enter(self):
		pass

class CentralCorridor(Scene):

	def enter(self):
		print "OK"

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
