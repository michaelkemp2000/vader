class Scene(object):

	def enter(self):
		print "This scene is noy yet configured.  Subclass it and implement enter()."
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print '''\nYou wake up from hyper-sleep and Gorthons have invaded your ship and its completly incapacitated.\n
You are the last surviving crew member and ou have learned of their plans to nuke your home planet below!\n
You must stop the Gorthons!\n
Your mission is to get the neutron destruct bomb from the Weapons Armory put it in the Bridge
and blow up the ship, after you have accessed the escape pod and launched to the plannet below\n'''

		print "Are your ready to play (y / n)?"
		start = raw_input(prompt)
		if start == 'N' or 'n':
			exit(1)
		elif start == 'Y' or 'y':
			print '''\nYou find yourself in a central corridor, the door on the right is to the Armory has a gorthon guarding.
		The door on the left to the escape pod room is not guard and the door at the end of the corridor which is to the Bridge
		is guarded by an extremly large Gorthon.  Type \'A\' for Armory, \'B\' for Bridge or \'E\' for Escape Pod.'''
			cc_opt = raw_input(prompt)
			if cc_opt == 'a' or cc_opt == 'A':
				return 'lwa'
			elif cc_opt == 'b' or cc_opt == 'B':
				return 'bridge'
			elif cc_opt == 'e' or cc_opt == 'E':
				return 'escape_pod'
			else:
				print "DOES NOT COMPUTE!"
				return 'central_corridor'

