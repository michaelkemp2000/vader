# Gorgon's Attack!
from sys import exit
from random import randint

#<-------------------SCENE-------------------------------------->

class Scene(object):


	def enter(self):
		print "This scene is not yet configured.  Subclass it and implement enter()."
		exit(1)

#<---------------------ENGINE--------------------------------------->

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map # this is now the Map instance a_map that contains start_scene in a.map (central_corridor was passed #194)

	def play(self):
		
		curent_scene = self.scene_map.opening_scene()  #4 & 7. this calles a.map opening scene function and puts the return in current_scene
		
		while True:
			print "\n-----------------------------------------------"  #8. Ok, we are getting this far
			next_scene_name = curent_scene.enter()  #9. FIX - was a typo in current scene... This seems to be the problem! calling current scene (centralCorridtor().enter) function
			curent_scene = self.scene_map.next_scene(next_scene_name)

#<-------------------ACTION-------------------------------------->
class Battle(object):

	def __init__(self, alien, hero):
		self.alien = alien
		self.hero = hero

	def attack(self):
		
		weapon = Hero.items.get('weapon')
		print weapon
		if self.alien.health > 0:
			print "\nThe Alien shouts ggrazadbog!"
			print "You pull out your laser gun and shoot the Gorthon."
			while self.alien.health > 0:
				if weapon == 'laser gun':
					a_damage = randint(1,4)
					print "zap: [-%d] hit point!" % a_damage 
					self.alien.reduce_health(a_damage)
					print self.alien.health
					if self.alien.health > 0:
						print "He is not dead!"
						self.defend()
						return 'hero'
				else:
					a_damage = randint(5,10)
					print "zap: [-%d] hit point!" % a_damage 
					self.alien.reduce_health(a_damage)
					print self.alien.health
					if self.alien.health > 0:
						print "He is not dead!"
						self.defend()
						return 'hero'

			if self.alien.health < 0:
				print "You killed the Gorthon"
				print "You pickup a passcode from his dead corpse"
				self.hero.add_item('passcode', '1234')
				return 'hero'

		else:
			print "\nThe Gorthon is already dead"
			return 'hero'

	def defend(self):

		print "\nThe Gortham starts shooting at you!"
		while self.hero.health > 0 and self.alien.health >0:
			h_damage = randint(1,4)
			print "zap: [-%d] damage!" % h_damage
			self.hero.reduce_health(h_damage)
			print "Health remaining: [%d]" % self.hero.health
			if self.hero.health > 0:
				print "Shoot or Run (S or R)"
				atk = raw_input("-->")
				if atk == 's' or atk == 'S':
					self.attack()

				elif atk == 'r' or atk == 'R':
					print "You flee like a coward and get shot."
					return 'alien'

				else:
					print "DOES NOT COMPUTE: You fumble around and get shot."
					return 'alien'

			else:
				print "You sustain a fatal wound."
				return 'alien'


#<-------------------SCENE-------------------------------------->

class Death(Scene):

	quips = ["\nYou Died.  You kinda suck at this.", "\nYou Died.  Your mom would be proud if you were smarter",
			"\nYou Died. Such a luser.", 
			"\nYou Died. I have a small puppy thats better than this."
	]

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)

class EscapePod(Scene):
	
	def enter(self):
		print "You rush through the ship desperatly trying to make it to the escape pod before the whole ship explodes."
		print "It seems like hardly any Gorthons are on the ship, so you run clear of interference."
		print "You the escape pod room and see a large Gorthon with advanced battle armor.  He must be the invasion party leader."
		print "There are also five escape pods that he has been tampering with to retrofit with bombs."
		print "Do you take an escape pod or fight (E or F)?"
		ans2 = raw_input("-->")
		if ans2 == 'e' or ans2 =='E':
			print "The Gorthon general start to laughing in your mind.  Is this some kind of telepathic abillity?"
			print "You hear a voice in your head, \'Stupid HUMAN, The majority of those pods are not functioning! good luck!\'"
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
		
		elif ans2 == 'f' or ans2 == 'F':
			print "You hear a voice in your mind, could this be from the Gorthon general.  Does he have some kind of telepathic ability."
			print "You cannon defeat me!"
			weapon = Hero.items.get('weapon1')
			if weapon == 'plasma cannon':
				print "you pull out your plasma cannon"
				print "The Gorthon looks concerned and backs up"
				b_alien = Alien(4)
				b_battle = Battle(b_alien, a_hero)
				winner = b_battle.attack()
				if winner == 'hero':
					print "You fall to the ground you head is hurting."
					print "All of a sudden you feel very different."
					print "You aquire the general\'s telepathic abilities."
					print "You have to get off the ship.  You look at the 5 pods."
					print "Somehow, you know pod 2 is functioning well."
					print "You jump in pod 2 and hit the eject."
					print "The pod easierly slides out into space, heading to the planet below."
					print "As it flies to the planet, you look back and see your ship explode like a bright star, taking out the Gorthon ship also."
					return 'planet'
				else:
					return 'death'
			else:
				print "This Gorthon is much bigger than you are with some serious armor.  This may not go well"
				b_alien = Alien(4)
				b_battle = Battle(b_alien, a_hero)
				winner = b_battle.attack()
				if winner == 'hero':
					print "You fall to the ground you head is hurting."
					print "All of a sudden you feel very different."
					print "You aquire the general\'s telepathic abilities."
					print "You have to get off the ship.  You look at the 5 pods."
					print "Somehow, you know pod 2 is functioning well."
					print "You jump in pod 2 and hit the eject."
					print "The pod easierly slides out into space, heading to the planet below."
					print "As it flies to the planet, you look back and see your ship explode like a bright star, taking out the Gorthon ship also."
					return 'planet'
				else:
					return 'death'

class Planet(Scene):

	def enter(self):
		print "\nYou land saftly on your planet only to find that its now inhabited by Gorthons #!?#."  
		print "What happened?"
		print "Enjoy the next chapter in this space adventure Gortham #2 - What happened to my planet?"
		exit(1)

class CentralCorridor(Scene):

	def enter(self):

			a_hero = Hero(4)
			a_alien = Alien(2)
			a_battle = Battle(a_alien, a_hero)
			Hero.items['weapon1'] = "laser gun"

			print "\nYou find yourself in a central corridor with three door labeled Armory, Bridge and Escape Pod."
			print "There is a Gorthon guarding.  Do you:"
			print "Attack the Gorthon (A)"
			print "Go to the Laser Weapons Armory (L)"
			print "Go to the Bridge (B)"
			print "Go to the escape pod (E)"
			cc_opt = raw_input("-->")

			if cc_opt == 'a' or cc_opt == 'A':
				winner = a_battle.attack()
				if winner == 'hero':
					print "Go to the Laser Weapons Armory (L)"
					print "Go to the Bridge (B)"
					print "Go to the escape pod (E)"
					cc_opt = raw_input("-->")
					if cc_opt == 'b' or cc_opt == 'B':
						return 'the_bridge'
					elif cc_opt == 'e' or cc_opt == 'E':
						return 'escape_pod'
					elif cc_opt == 'l' or cc_opt == 'L':
						return 'lwa'
					else:
						print "DOES NOT COMPUTE!: The Gorthon resurects itself"
						return 'central_corridor'
				else:
					return 'death'
				

			elif cc_opt == 'b' or cc_opt == 'B':
				return 'the_bridge'
			elif cc_opt == 'e' or cc_opt == 'E':
				return 'escape_pod'
			elif cc_opt == 'l' or cc_opt == 'L':
				return 'lwa'
			else:
				print "DOES NOT COMPUTE!"
				return 'central_corridor'

class LaserWeaponArmory(Scene):
	
	def enter(self):
		print "You do a dive roll into the Weapons Armory, crouch and scan the room for more Gorthons"
		print "that might be hiding.  It\'s dead quite, too quite.\n"
		print "You stand up and run to the far side of the room and find the neutron bomb container."  
		print "There is a keypad lock on the box and you need the code to get thebomb out."
		print "If you get the code wrong 10 timesthen the lock closes forever and you can't get the bomb."  
		print "The code is 3 digits.\n"
		ans1 = 'Null'
		while ans1 != 'm' or ans1 != 'M':
			print "Do you enter the code manually, check your inventory first or go back to the central corridor? (M, I, C)"
			ans1 = raw_input("-->")
			if ans1 == 'M' or ans1 == 'm':
				code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
				guess = raw_input("[keypad]>")
				guesses = 0
				if guess == Hero.items.get('passcode'):
					print "The container clicks open and the seal breaks, letting gas out."
					print "You grab the neutron bomb and head to the bridge."
					Hero.items['bomb'] = "neutron"
					return 'the_bridge'

				while guess != code and guesses < 10:
					print "BZZZZZEDDD!"
					guesses += 1
					guess = raw_input("[keypad]>")

				if guess == code:
					print "The container clicks open and the seal breaks, letting gas out."
					print "You grab the neutron bomb and head to the bridge."
					return 'the_bridge'

				
				else:
					print "The lock buzzes one last time and then you hear a sickening melting sound"
					print "as the mechanism is fused together.\n"
					print "You decide to sit there for a while, and finally Gorthans blow up you home planet below"
					print "and your ship.\n"
					return 'death'

			elif ans1 == 'C' or ans1 == 'c':
				pc = Hero.items.get('passcode')
				if pc != '1':
					print "You need the Neutron Bomb! You're not in time to save the ship and planet."
					return 'death'
				else:
					return 'central_corridor'

			elif ans1 == 'I' or ans1 == 'i':
				print "you look in you pocket and find: ", Hero.items['passcode']

			elif ans1 == 'L' or ans1 == 'l':
				print "You examine the room and find a plasma cannon hidden under some large"
				print "containers that must have falled due to the attach on your ship."
				Hero.items['weapon1'] = "plasma cannon"

			else:
				print "DOES NOT COMPUTE!"
				return "lwa" 


class TheBridge(Scene):
	def enter(self):

		bomb = Hero.items.get('bomb')
		if bomb == 'neutron':
			print "\nYou burst into the Bridge with the neutron destruction bomb under your arm" 
			print "and surprise 5 Gorthons who are trying to take control of the ship.\n"
			print "They haven\'t taken thier weapons out yet, and they see the active bomb under your arm"
			print "and don't want to set it off.\n"
			print "Do you throw the bomb or slowly place the bomb (T or P)?"
			action = raw_input("-->")

			if action == 't' or action == 'T':
				print "In a panic you throw the bomb and the group of Gorthons and make a leap for the door."
				print "Right as you drop it a Gorthon shoots you right in the back, killing you."
				print "As you die, you see another Gorthon frantically trying to disarm the bomb."
				print "You die knowing that they will probably blow up when it goes off."
				return 'death'

			elif action == 'p' or action == 'P':
				print "You point your blaster at the bomb under your arm and the Gorthons put thier hands up and start to sweat"
				print "You inch backwards to the door, open it, and then carefully place the bomb on the floor."
				print "You then jump back through the door, punch the close button abd blast the lock so the Gorthons cant get out."
				print "Now the bomb is placed, you run to the escape pod to get off this tin."
				return 'escape_pod'
			else:
				print "DOES NOT COMPUTE! You get shot!"
				return "death"

		else:
			print "You burst into the Bridge and surprise 5 Gorthons who are trying to take control of the ship.\n"
			print "They turn and look at you.  You\'re toast, the show you mercy with a quick death!"
			return 'death'


#<-------------------------OTHER THINGS---------------------------->


class Being(object):
	def __init__(self, alive):
		self.alive = alive

class Hero(Being):

	items = {}

	def __init__(self, health):
		self.health = health


	def reduce_health(self, hit):
		self.hit = hit
		self.health = self.health - self.hit

	def add_item(self, iname, ivalue):
		self.iname = iname
		self.ivalue = ivalue
		self.ivalue = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		Hero.items[self.iname] = self.ivalue


class Alien(Being):
	def __init__(self, health):
		self.health = health

	def reduce_health(self, hit):
		self.hit = hit
		self.health = self.health - self.hit
		


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
		return Map.scenes.get(scene_name) # 6.this looks up scene name in dict, originally central corridor and returns CentralCorridor()

	def opening_scene(self):
		print "\nYou wake up from hyper-sleep and Gorthons have invaded your ship and its completly incapacitated."
		print "You are the last surviving crew member and ou have learned of their plans to nuke your home planet below!"
		print "You must stop the Gorthons!\n"
		print "1. Your mission is to get the neutron destruct bomb from the Weapons Armory put it in the Bridge"
		print "2. Blow up the ship, after you have accessed the escape pod and launched to the plannet below\n"

		print "Are your ready to proceed (y / n)?"
		start = raw_input("-->")
		if start == 'N' or start == 'n':
			print "Your trapped on the ship you fool!  Ok you jetty yourself into space and die"
			self.start_scene = 'death'
			return self.next_scene(self.start_scene)
		elif start == 'Y' or start == 'y':
			return self.next_scene(self.start_scene) #5. this calles a.map next scene function and puts the return to output to current scene in play function (#186)
		else:
			print "DOES NOT COMPUTE!, your planet is destroyed below by a neutron bombs."
			print "The shockwave takes out you and your ship"
			self.start_scene = 'death'
			return self.next_scene(self.start_scene)


#<----------------MAIN------------------------>

a_map = Map('central_corridor') #1.This creates an object a_map from Map and passes 'central corridor' to start_scene
a_game = Engine(a_map) #2.This creates an object a_game from Engine while passing in the instance of Map class (a_map)
a_game.play()  #3. run play function from Enginer object instance
