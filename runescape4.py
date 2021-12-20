import time
from random import randint
from random import choice

#Things to do - stackable items

class Skill:
	def __init__(self, xp, level):
		self.xp = xp
		self.level = level

class Player:
	def __init__(self, hitpoints, location):
		self.hitpoints = hitpoints
		self.location = location

class Monster:
	def __init__(self, identifier, hitpoints, attack, defence, loot):
		self.identifier = identifier
		self.hitpoints = hitpoints
		self.attack = attack
		self.defence = defence
		self.loot = loot

class Equipment:
	def __init__(self, name, slot, offensivebonus, defensivebonus, defencerequirement, offencerequirement):
		self.name = name
		self.slot = slot
		self.offensivebonus = offensivebonus
		self.defensivebonus = defensivebonus
		self.defencerequirement = defencerequirement
		self.offencerequirement = offencerequirement

#Equipment
#index: 0 head, 1 chest, 2 legs, 3 feet, 4 gloves, 5 mainhand, 6 offhand
bronzehelmet = Equipment('bronze helmet', 0, 0, 2, 10, 0)
bronzebreastplate = Equipment('bronze breastplate',1, 0, 4, 10, 0)
bronzelegguards = Equipment('bronze legguards',2, 0, 3, 10, 0)
bronzeboots = Equipment('bronze boots', 3, 0, 2, 10, 0)
bronzegloves = Equipment('bronze gloves', 4, 0, 2, 10, 0)
bronzesword = Equipment('bronze sword', 5, 2, 0, 0, 10)
bronzeshield = Equipment('bronze shield', 6, 0, 2, 10, 0)

equipmentlist = [bronzehelmet,bronzebreastplate,bronzelegguards,bronzeboots,bronzegloves,bronzesword,bronzeshield]

#Skills
attack = Skill(0, 1)
defence = Skill(0, 1)
hitpoints = Skill (0, 1)
fishing = Skill(0, 1)
mining = Skill(0, 1)
smithing = Skill(0, 1)
cooking = Skill(0, 1)

#Monsters
goblin = Monster(1, 5, 1, 1, 1)
farmer = Monster(2, 20, 2, 2, 1)
dragon = Monster(3, 100, 10, 10, 2)

#Player
player = Player(10, "Lumbridge")

#Inventory
inventory = ['fishing rod', 'sword', 'bronze helmet']

#Equipment
playerequipment = ["rugged hat", "rugged vest", "rugged pants", "rugged boots", "rugged gloves", "rusty sword", "wooden shield"]
playerequipmentstats = [0, 0]

#Loot tables
def gettable(tier):
	loot1 = ['pickaxe', 'fishing rod', 'axe', 'tinderbox', 'hammer', 'lobster pot']
	loot2 = ['sword', 'shield', 'harpoon']
	if tier == 1:
		return loot1
	elif tier == 2:
		return loot2
	else:
		return []

def getloot(tier):
	table = gettable(tier)
	item = choice(table)
	if item in inventory:
		print ("You already have " + str(item))
	else:	
		noloot = randint(0, 3)
		if noloot == 1:
			print ("You recieve no loot.")
		else:
			if len(inventory) >= 8:
				print("Your inventory is full.")
			else:
				inventory.append(item)
			if str(item).startswith("a"):
				print ("You recieve an " + str(item))
			else:
				print ("You recieve a " + str(item))

def home():
	home_input = input("What do you want to do? 1=Combat 2=Gathering 3=Artisan 4=Inventory management 5=See levels 6=Equipment\n")
	if home_input == "1":
		combat_home()
	elif home_input == "2":
		gathering_home()
	elif home_input == "3":
		artisan_home()
	elif home_input == "4":
		inventory_home()
	elif home_input == "5":
		display_levels()
	elif home_input == "6":
		equipment_home()
	else:
		print ("Invalid input, please try again.")
		home()

#Refresh Equipmentstats
def refreshequipmentstats():
	offbonus = 0
	defbonus = 0
	for i in playerequipment:
		for j in equipmentlist:
			if j.name == i:
				offbonus += j.offensivebonus
				defbonus += j.defensivebonus
	playerequipmentstats = [offbonus, defbonus]
	print(playerequipmentstats)


def equipment_home():
	print("Head:" + playerequipment[0])
	print("Chest:" + playerequipment[1])
	print("Legs:" + playerequipment[2])
	print("Feet:" + playerequipment[3])
	print("Gloves:" + playerequipment[4])
	print("Main hand:" + playerequipment[5])
	print("Off hand:" + playerequipment[6] + "\n")
	print(playerequipmentstats)
	equipment_home_input = input("What do you want to do? 1=See stats 2=Equip an item 3=Cancel\n")
	if equipment_home_input == "1":
		print("Defensive bonus: " + str(playerequipmentstats[0]))
		print("Offensive bonus: " + str(playerequipmentstats[1]))
	
	elif equipment_home_input == "2":
		print("Inventory: " + str(inventory))
		equipment_equipitem_input = input("Which item do you want to equip? (1-8) 9=Cancel\n")
		if equipment_equipitem_input == "9":
			home()
		elif int(equipment_equipitem_input) > len(inventory):
			print("There's nothing in that slot.")
			time.sleep(1)
			equipment_home()
		else:
			#Selection is 0-indexed integer. The item to be equipped is represented as a string. Cycle all items in the game. Compare full item list to selected item
			selected_item_number = int(equipment_equipitem_input) - 1
			selected_item = inventory[selected_item_number]
			for i in equipmentlist:
				if selected_item == i.name:
					equipment_slot = i.slot
					removed_item = playerequipment[equipment_slot]
					playerequipment[equipment_slot] = selected_item
					inventory.remove(selected_item)
					inventory.append(removed_item)
					print("You equip " + selected_item)
					refreshequipmentstats()
					print(playerequipmentstats)


		
	elif equipment_home_input == "3":
		home()

	else:
		print("Invalid input")
		equipment_home()

	home()



def display_levels():
	print ("Attack: " + str(attack.level) + " Defence: " + str(defence.level) + " Hitpoints " + str(hitpoints.level) + "\nFishing: " + str(fishing.level) + " Cooking: " + str(cooking.level) + " Mining: " + str(mining.level) + "\nSmithing: " + str(smithing.level))
	home()

def combat_home():
	combat_home_input = input("What do you want to fight? 1=Goblin 2=Farmer 3=Dragon\n")
	if combat_home_input == "1":
		fight(goblin)
	elif combat_home_input == "2":
		fight(farmer)
	elif combat_home_input == "3":
		fight(dragon)
	else:
		print("Invalid input, please try again.")
		home()



def inventory_home():
	selected_item = 1
	selected_item_number = 1
	print("Current inventory:\n" + str(inventory))
	inventory_home_input = input("Please select an item to remove (1-8) 9=Cancel 10=Delete all\n")
	if inventory_home_input == "9":
		home()
	elif inventory_home_input == "10":
		inventory.clear()
		home()
	else:
		selected_item_number = int(inventory_home_input) - 1
		if (len(inventory) < int(inventory_home_input)) or (int(inventory_home_input) <= 0):
			print("There is no item in that slot")
			home()
		else:
			selected_item = inventory[selected_item_number]
			response_sure = input ("Are you sure you want to delete " + str(selected_item) + "? 1=Yes 2=No\n")
			if response_sure == "1":
				inventory.pop(selected_item_number)
				print("You have deleted " + str(selected_item))
				inventory_home()
			else:
				home()

def artisan_home():
	artisan_home_input = input("What do you want to do? 1=Cooking 2=Smithing\n")
	if artisan_home_input == "1":
		cooking_home()
	elif artisan_home_input == "2":
		smithing_home()
	else:
		print ("Invalid input.")
		home()

def smithing_home():
	smithing_home_input = input("What do you want to do? 1=Smith bronze 2=Smith iron\n")
	if smithing_home_input == "1":
			while (('copper ore' in inventory) and ('tin ore' in inventory)):
				inventory.remove('copper ore')
				inventory.remove('tin ore')
				inventory.append('bronze bar')
				time.sleep(1)
				print("You smelt a bronze bar")
	home()

def cooking_home():
	level = cooking.level
	print ("You start cooking...")
	if 'salmon' in inventory:
		while 'salmon' in inventory:
			time.sleep(1)
			skillscheck = randint (0,10)
			skillschance = (1 + level)
			if (skillscheck + skillschance) >= 5:
				inventory.remove('salmon')
				inventory.append('cooked salmon')
				time.sleep(1)
				print ("You cook the salmon")
				cooking.xp += 100
			else:
				inventory.remove('salmon')
				print ("You burn the salmon")

	elif 'trout' in inventory:
		while 'trout' in inventory:
			time.sleep(1)
			skillscheck = randint (0,10)
			skillschance = (1 + level)
			if (skillscheck + skillschance) >= 5:
				inventory.remove('trout')
				inventory.append('cooked trout')
				time.sleep(1)
				print ("You cook the trout")

				
				cooking.xp += 100
			else:
				inventory.remove('trout')
				print ("You burn the trout")

	else:
		print('You have nothing to cook')

	if level < getlevel(cooking.xp):
		refreshlevel()
		newlevel = cooking.level
		print ("Congratulations! Your cooking level is now " + str(newlevel) + "!")

	else:
		refreshlevel()

	home()



def gathering_home():
	gathering_home_input = input("What do you want to do? 1=Fishing 2=Mining\n")
	if gathering_home_input == "1":
		gathering_fish(player.location)
	elif gathering_home_input == "2":
		gathering_ore(player.location)
	else:
		print("Invalid input")
		home()

def gathering_ore(location):
	level = mining.level
	if location == "Lumbridge":
		print ("You swing your pick at the rock...")
		stillmining = 0
		while stillmining == 0:
			time.sleep(0.5)
			print ("Swinging away...")
			skillscheck = randint (0,10)
			skillchance = (1 + level)
			if (skillscheck + skillchance) >= 10:
				oretype = randint(0,1)
				if oretype == 0:
					if len(inventory) <= 8:
						inventory.append('tin ore')
						print('You mine some tin ore')
						mining.xp += 30
					else:
						print("Your inventory is full")
						mining.xp += 30
				else:
					if len(inventory) <= 8:
						inventory.append('copper ore')
						print ('You mine some copper ore')
						mining.xp += 30
					else:
						print("Your inventory is full")
						mining.xp +=30
				stillmining = 1
				home()

def gathering_fish(location):
	level = fishing.level
	gathering_fish_response = input("What type of fishing do you want to try for 1=Rod 2=Lobster pot 4=Home\n")
	if gathering_fish_response == "1":
		if 'fishing rod' in inventory:
			print ("You cast out your rod...")
			stillfishing = 0
			while stillfishing == 0:
				time.sleep(0.5)
				print ("Nothing yet...")
				skillscheck = randint(0,10)
				skillchance = (1 + level)
				if (skillscheck + skillchance) >= 10:
					fishtype = randint(0,1)
					if fishtype == 0:
						if len(inventory) <= 8:
							inventory.append('trout')
							print ("You manage to catch a trout!")
							fishing.xp += 20
						else:
							print("Your inventory is full")
							fishing.xp += 20
					else:
						if len(inventory) <= 8:
							inventory.append('salmon')
							print ("You manage to catch a salmon!")
							fishing.xp += 30
						else:
							print("Your inventory is full")
							fishing.xp += 30
					stillfishing = 1
					if level < getlevel(fishing.xp):
						print ("Congratulations! Your fishing level is now " + str(getlevel(fishing.xp)) + "!")
						refreshlevel()
				else:
					refreshlevel()
					gathering_fish(player.location)
			if level < getlevel(fishing.xp):
				refreshlevel()
				print ("Congratulations! Your fishing level is now " + str(fishing.level) + "!")
			else:
				refreshlevel()
		else:
			print ("You need a fishing rod to do that.")

	elif gathering_fish_response == "2":
		if ('lobster pot' in inventory) and (fishing.level >= 5):
			print ("You cast out your lobster pot...")
			stillfishing = 0
			while stillfishing == 0:
				time.sleep(0.5)
				print ("Nothing yet...")
				skillscheck = randint(0,10)
				skillchance = (1 + level)
				if (skillscheck + skillchance) >= 15:
					fishtype = randint(0,3)
					if (fishtype >= 0) and (fishtype < 3):
						if len(inventory) <= 8:
							inventory.append('lobster')
							print ("You manage to catch a lobster.")
							fishing.xp += 50
						else:
							print("Your inventory is full.")
							fishing.xp += 50
					else:
						if len(inventory) <= 8:
							inventory.append('casket')
							print ("You catch a casket in your lobster pot.")
							fishing.xp += 70
						else:
							print ("Your inventory is full.")
							fishing.xp += 70
					if level < getlevel(fishing.xp):
						print ("Congratulations! Your fishing level is now " + str(getlevel(fishing.xp)) + "!")
						refreshlevel()
					else:
						refreshlevel()
					stillfishing = 1	
					gathering_fish(player.location)
		elif (fishing.level < 5):
			print("You need to be fishing level 5 to do that.")
		else:
			print("You need a lobster pot to do that.")


		

	home()



def fight(fightmonster):
	player_hp = player.hitpoints
	player_attack = attack.level
	player_defence = defence.level
	player_hitpoints = hitpoints.level

	monster_hp = fightmonster.hitpoints
	monster_attack = fightmonster.attack
	monster_defence = fightmonster.defence
	monster_loot = fightmonster.loot
	monster_identifier = fightmonster.identifier

	getASCII(monster_identifier)

	while ((player_hp) > 0) and ((monster_hp) > 0 ):

		#Player damage
		player_damage = ((monster_attack - player_defence + 1) * randint(0,1))
		if player_damage <= 0:
			player_damage = randint(0,1)
		player_hp -= player_damage

		#Player death
		if player_hp <= 0:
			print ("Oh dear, you are dead.")
			inventory.clear()
			home()
		else:
			print ("You have " + str(player_hp) + "hp left.")
			time.sleep(1)

		#Monster damage
		monster_damage = (2 + (player_attack - monster_defence) * randint(0,1))
		if monster_damage <= 0:
			monster_damage = randint(0,1)
		monster_hp -= monster_damage

		#Monster death
		if monster_hp <= 0: 
			print ("The monster is dead.")
			attack.xp += fightmonster.hitpoints * randint (1,3) * 10
			defence.xp += fightmonster.hitpoints * randint (1,3) * 10
			hitpoints.xp += fightmonster.hitpoints * randint (1,3) * 10

			checklevel_attack = getlevel(attack.xp)
			checklevel_defence = getlevel(defence.xp)
			checklevel_hitpoints = getlevel(hitpoints.xp)

			if checklevel_attack > player_attack:
				print ("Congratulations! You are now attack level " + str(attack.level + 1) + "!")
			if checklevel_defence > player_defence:
				print ("Congratulations! You are now defence level " + str(defence.level + 1) + "!")
			if checklevel_hitpoints > player_hitpoints:
				print ("Congratulations! You are now hitpoints level " + str(hitpoints.level + 1) + "!")

			refreshlevel()
			getloot(monster_loot)
			home()
		else:
			print ("The monster has " + str(monster_hp) + "hp left.")
			time.sleep(1)

def getlevel(skillxp):
	if skillxp >= 3523:
		return 20
	elif skillxp >= 3115:
		return 19
	elif skillxp >= 2746:
		return 18
	elif skillxp >= 3115:
		return 17
	elif skillxp >= 2746:
		return 16
	elif skillxp >= 2411:
		return 15
	elif skillxp >= 2107:
		return 14
	elif skillxp >= 1833:
		return 13
	elif skillxp >= 1584:
		return 12
	elif skillxp >= 1358:
		return 11
	elif skillxp >= 1154:
		return 10
	elif skillxp >= 969:
		return 9
	elif skillxp >= 801:
		return 8
	elif skillxp >= 650:
		return 7
	elif skillxp >= 512:
		return 6
	elif skillxp >= 388:
		return 5
	elif skillxp >= 276:
		return 4
	elif skillxp >= 174:
		return 3
	elif skillxp >= 83:
		return 2
	else:
		return 1

def refreshlevel():
	attack.level = getlevel(attack.xp)
	defence.level = getlevel(defence.xp)
	hitpoints.level = getlevel(hitpoints.xp)
	fishing.level = getlevel(fishing.xp)
	cooking.level = getlevel(cooking.xp)
	mining.level = getlevel(mining.xp)
	smithing.level = getlevel(smithing.xp)

def getASCII(identifier):
	if identifier == 1:
		print ("""
		             ,      ,
		            /(.-""-.)|
		        |\  \/      \/  /|
		        | \ / =.  .= \ / |
		        \( \   o\/o   / )/
		         \_, '-/  \-' ,_/
		           /   \__/   |
		           \ \__/\__/ /
		         ___\ \|--|/ /___
		       /`    \      /    `|
		      /       '----'       |
		""")
	elif identifier == 2:
		print ("""
		   .------\ /------.
		   |       -       |
		   |               |
		   |               |
		   |               |
		_______________________
		===========.===========
		  / ~~~~~     ~~~~~ |
		 /|     |     ||
		 W   ---  / \  ---   W
		 \.      |o o|      ./
		  |                 |
		  \    #########    /
		   \  ## ----- ##  /
		    \##         ##/
		     \_____v_____/
			""")

	elif identifier == 3:
		print("""
          ,  ,
          \\ \\           
          ) \\ \\    _p_ 
          )^\))\))  /  *\ 
           \_|| || / /^`-' 
  __       -\ \\--/ / 
<'  \\___/   ___. )'
     `====\ )___/\\ 
          //     `"
          \\    /  |
          `"
          """)


home()