'''
CPSC 415 -- Homework #5 support file
Stephen Davies, University of Mary Washington, fall 2023
'''

from clue import CluePlayer, suspects, weapons, rooms, Card
from PropKB import KB

# Throughout this file, you can refer to the global variables "suspects",
# "weapons", and "rooms", which are tuples of "Card" objects telling you what
# cards are in the game, period. You can even try this right now:
#
# >>> print(suspects)
# >>> print(weapons)
# >>> print(rooms)
#
# Each Card object has a name and a category, accessible with the dot (".")
# notation:
# >>> print(f"{suspects[0].name} is a {suspects[0].category}")
# mustard is a SUSPECT


class akeehan_CluePlayer(CluePlayer):

	def __init__(self, hand, player_num):
		#Store final guess before conversion to tuple
		self.final_ans = ["","",""]
		#Final guess in tuple form
		self.ans = ()
		#Keep track of what we have shown other players
		self.shown = []
		#Track if we have set the rotation of players
		self.set_flag = 0
		#Who goes first after us
		self.num1 = 0
		#Who goes second after us
		self.num2 = 0
		#Knowledge Base
		self.kb = KB()
		
		self.pass_flag = 0
		super().__init__(player_num, 'akeehan')
		self.my_num = player_num
		self.hand = hand
		#Call rules to get our KB init
		self.rules()

	def ready_to_accuse(self):  
		#Our KB tells us when to accuse
		if self.kb.ask("accuse") == True:
			#Get other pos
			if self.my_num == 1:
				num1 = 2
				num2 = 3
			elif self.my_num == 2:
				num1 = 3
				num2 = 1
			elif self.my_num == 3:
				num1 = 1
				num2 = 2
			
			#Get our suspect from KB
			if self.kb.ask("{}{}".format(str(self.my_num), "mustard")) == False and self.kb.ask("{}{}".format(str(num1), "mustard")) == False and self.kb.ask("{}{}".format(str(num2), "mustard")) == False:
				self.final_ans[0] = suspects[0]
			elif self.kb.ask("{}{}".format(str(self.my_num), "plum")) == False and self.kb.ask("{}{}".format(str(num1), "plum")) == False and self.kb.ask("{}{}".format(str(num2), "plum")) == False:
				self.final_ans[0] = suspects[1]
			elif self.kb.ask("{}{}".format(str(self.my_num), "green")) == False and self.kb.ask("{}{}".format(str(num1), "green")) == False and self.kb.ask("{}{}".format(str(num2), "green")) == False:
				self.final_ans[0] = suspects[2]
			elif self.kb.ask("{}{}".format(str(self.my_num), "scarlet")) == False and self.kb.ask("{}{}".format(str(num1), "scarlet")) == False and self.kb.ask("{}{}".format(str(num2), "scarlet")) == False:
				self.final_ans[0] = suspects[3]
			elif self.kb.ask("{}{}".format(str(self.my_num), "white")) == False and self.kb.ask("{}{}".format(str(num1), "white")) == False and self.kb.ask("{}{}".format(str(num2), "white")) == False:
				self.final_ans[0] = suspects[4]
			elif self.kb.ask("{}{}".format(str(self.my_num), "peacock")) == False and self.kb.ask("{}{}".format(str(num1), "peacock")) == False and self.kb.ask("{}{}".format(str(num2), "peacock")) == False:
				self.final_ans[0] = suspects[5]
			
			#Get our Weapon from KB
			if self.kb.ask("{}{}".format(str(self.my_num), "knife")) == False and self.kb.ask("{}{}".format(str(num1), "knife")) == False and self.kb.ask("{}{}".format(str(num2), "knife")) == False:
				self.final_ans[1] = weapons[0]
			elif self.kb.ask("{}{}".format(str(self.my_num), "revolver")) == False and self.kb.ask("{}{}".format(str(num1), "revolver")) == False and self.kb.ask("{}{}".format(str(num2), "revolver")) == False:
				self.final_ans[1] = weapons[1]
			elif self.kb.ask("{}{}".format(str(self.my_num), "rope")) == False and self.kb.ask("{}{}".format(str(num1), "rope")) == False and self.kb.ask("{}{}".format(str(num2), "rope")) == False:
				self.final_ans[1] = weapons[2]
			elif self.kb.ask("{}{}".format(str(self.my_num), "candlestick")) == False and self.kb.ask("{}{}".format(str(num1), "candlestick")) == False and self.kb.ask("{}{}".format(str(num2), "candlestick")) == False:
				self.final_ans[1] = weapons[3]
			elif self.kb.ask("{}{}".format(str(self.my_num), "wrench")) == False and self.kb.ask("{}{}".format(str(num1), "wrench")) == False and self.kb.ask("{}{}".format(str(num2), "wrench")) == False:
				self.final_ans[1] = weapons[4]
			elif self.kb.ask("{}{}".format(str(self.my_num), "leadpipe")) == False and self.kb.ask("{}{}".format(str(num1), "leadpipe")) == False and self.kb.ask("{}{}".format(str(num2), "leadpipe")) == False:
				self.final_ans[1] = weapons[5]
				
			#Get our Room from KB
			if self.kb.ask("{}{}".format(str(self.my_num), "diningroom")) == False and self.kb.ask("{}{}".format(str(num1), "diningroom")) == False and self.kb.ask("{}{}".format(str(num2), "diningroom")) == False:
				self.final_ans[2] = rooms[0]
			elif self.kb.ask("{}{}".format(str(self.my_num), "ballroom")) == False and self.kb.ask("{}{}".format(str(num1), "ballroom")) == False and self.kb.ask("{}{}".format(str(num2), "ballroom")) == False:
				self.final_ans[2] = rooms[1]
			elif self.kb.ask("{}{}".format(str(self.my_num), "billiardroom")) == False and self.kb.ask("{}{}".format(str(num1), "billiardroom")) == False and self.kb.ask("{}{}".format(str(num2), "billiardroom")) == False:
				self.final_ans[2] = rooms[2]
			elif self.kb.ask("{}{}".format(str(self.my_num), "study")) == False and self.kb.ask("{}{}".format(str(num1), "study")) == False and self.kb.ask("{}{}".format(str(num2), "study")) == False:
				self.final_ans[2] = rooms[3]
			elif self.kb.ask("{}{}".format(str(self.my_num), "conservatory")) == False and self.kb.ask("{}{}".format(str(num1), "conservatory")) == False and self.kb.ask("{}{}".format(str(num2), "conservatory")) == False:
				self.final_ans[2] = rooms[4]
			elif self.kb.ask("{}{}".format(str(self.my_num), "kitchen")) == False and self.kb.ask("{}{}".format(str(num1), "kitchen")) == False and self.kb.ask("{}{}".format(str(num2), "kitchen")) == False:
				self.final_ans[2] = rooms[5]
			elif self.kb.ask("{}{}".format(str(self.my_num), "hall")) == False and self.kb.ask("{}{}".format(str(num1), "hall")) == False and self.kb.ask("{}{}".format(str(num2), "hall")) == False:
				self.final_ans[2] = rooms[6]
			elif self.kb.ask("{}{}".format(str(self.my_num), "lounge")) == False and self.kb.ask("{}{}".format(str(num1), "lounge")) == False and self.kb.ask("{}{}".format(str(num2), "lounge")) == False:
				self.final_ans[2] = rooms[7]
			elif self.kb.ask("{}{}".format(str(self.my_num), "library")) == False and self.kb.ask("{}{}".format(str(num1), "library")) == False and self.kb.ask("{}{}".format(str(num2), "library")) == False:
				self.final_ans[2] = rooms[8]
				
			#Final ans
			self.ans = (self.final_ans[0], self.final_ans[1], self.final_ans[2])
			return True
		else:
			return False

	def get_accusation(self):
		return self.ans

	def get_suggestion(self):
		#Get other pos
		if self.my_num == 1:
			num1 = 2
			num2 = 3
		elif self.my_num == 2:
			num1 = 1
			num2 = 3
		elif self.my_num == 3:
			num1 = 1
			num2 = 2
			
		#Look for suspect
		for suspect in suspects:
			#If we already know the suspect, then swivel off of it to get other cards
			if self.kb.ask("mu") == True:
				if self.kb.ask("{}{}".format(str(self.my_num),suspect[0])) == False:
					sus = suspect
			elif self.kb.ask("{}{}".format(str(num1),suspect[0])) != True:
				sus = suspect
		#Look for weapon
		for weapon in weapons:
			#If we already know the weapon, then swivel off of it to get other cards
			if self.kb.ask("mw") == True:
				if self.kb.ask("{}{}".format(str(self.my_num),weapon[0])) == False:
					weap = weapon
			elif self.kb.ask("{}{}".format(str(num1),weapon[0])) != True:
				weap = weapon
		for room in rooms:
			#If we already know the room, then swivel off of it to get other cards
			if self.kb.ask("mr") == True:
				if self.kb.ask("{}{}".format(str(self.my_num),room[0])) == False:
					r = room
			elif self.kb.ask("{}{}".format(str(num1),room[0])) != True:
				r = room
		ans = {sus, weap, r}
		return ans
		

	def publicly_observe(self, suggesting_player_num, suggestion,
		responding_player_num, revealed_a_card):
		#Getting the rotation of everyone
		#If we are pos 3
		if suggesting_player_num == self.my_num and responding_player_num == 1 and not revealed_a_card and self.set_flag == 0 and self.my_num == 3:
			self.pass_flag = 1
			if suggesting_player_num == self.my_num and responding_player_num == 1 and  revealed_a_card and self.set_flag == 0 and self.my_num == 3 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 1
				self.num2 = 2
			
			elif suggesting_player_num == self.my_num and responding_player_num == 2 and  revealed_a_card and self.set_flag == 0 and self.my_num == 3 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 2
				self.num2 = 1
		
		elif suggesting_player_num == self.my_num and responding_player_num == 1 and revealed_a_card and self.set_flag == 0 and self.my_num == 3 and self.pass_flag == 0:
			self.set_flag = 1
			self.num1 = 1
			self.num2 = 2
			
		elif suggesting_player_num == self.my_num and responding_player_num == 1 and revealed_a_card and self.set_flag == 0 and self.my_num == 3 and self.pass_flag == 1:
			self.pass_flag = 0
			
		if suggesting_player_num == self.my_num and responding_player_num == 2 and not revealed_a_card and self.set_flag == 0 and self.my_num == 3:
			self.pass_flag = 1
			if suggesting_player_num == self.my_num and responding_player_num == 1 and revealed_a_card and self.set_flag == 0 and self.my_num == 3 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 1
				self.num2 = 2
				
			elif suggesting_player_num == self.my_num and responding_player_num == 2 and revealed_a_card and self.set_flag == 0 and self.my_num == 3 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 2
				self.num2 = 1
				
		elif suggesting_player_num == self.my_num and responding_player_num == 2 and revealed_a_card and self.set_flag == 0 and self.my_num == 3 and self.pass_flag == 0:
			self.set_flag = 1
			self.pass_flag = 0
			self.num1 = 2
			self.num2 = 1

		elif suggesting_player_num == self.my_num and responding_player_num == 2 and revealed_a_card and self.set_flag == 0 and self.my_num == 3 and self.pass_flag == 1:
			self.pass_flag = 0
				
		#If we are pos 2
		if suggesting_player_num == self.my_num and responding_player_num == 1 and not revealed_a_card and self.set_flag == 0 and self.my_num == 2:
			self.pass_flag = 1
			if suggesting_player_num == self.my_num and responding_player_num == 1 and revealed_a_card and self.set_flag == 0 and self.my_num == 2 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 1
				self.num2 = 3
				
			elif suggesting_player_num == self.my_num and responding_player_num == 3 and revealed_a_card and self.set_flag == 0 and self.my_num == 2 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 3
				self.num2 = 1

		elif suggesting_player_num == self.my_num and responding_player_num == 1 and revealed_a_card and self.set_flag == 0 and self.my_num == 2 and self.pass_flag == 0:
			self.set_flag = 1
			self.num1 = 1
			self.num2 = 3
			
		elif suggesting_player_num == self.my_num and responding_player_num == 1 and revealed_a_card and self.set_flag == 0 and self.my_num == 2 and self.pass_flag == 1:
			self.pass_flag = 0

		if suggesting_player_num == self.my_num and responding_player_num == 3 and not revealed_a_card and self.set_flag == 0 and self.my_num == 2:
			self.pass_flag = 1
			if suggesting_player_num == self.my_num and responding_player_num == 1 and revealed_a_card and self.set_flag == 0 and self.my_num == 2 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 1
				self.num2 = 3
				
			elif suggesting_player_num == self.my_num and responding_player_num == 3 and revealed_a_card and self.set_flag == 0 and self.my_num == 2 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 3
				self.num2 = 1

		elif suggesting_player_num == self.my_num and responding_player_num == 3 and revealed_a_card and self.set_flag == 0 and self.my_num == 2 and self.pass_flag == 0:
			self.set_flag = 1
			self.num1 = 3
			self.num2 = 1
				
		elif suggesting_player_num == self.my_num and responding_player_num == 3 and revealed_a_card and self.set_flag == 0 and self.my_num == 2 and self.pass_flag == 1:
			self.pass_flag = 0
		
		#If we are pos 1
		if suggesting_player_num == self.my_num and responding_player_num == 2 and not revealed_a_card and self.set_flag == 0 and self.my_num == 1:
			self.pass_flag = 1
			if suggesting_player_num == self.my_num and responding_player_num == 3 and revealed_a_card and self.set_flag == 0 and self.my_num == 1 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 3
				self.num2 = 2

			elif suggesting_player_num == self.my_num and responding_player_num == 2 and revealed_a_card and self.set_flag == 0 and self.my_num == 1 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 2
				self.num2 = 3

		elif suggesting_player_num == self.my_num and responding_player_num == 2 and revealed_a_card and self.set_flag == 0 and self.my_num == 1 and self.pass_flag == 0:
			self.set_flag = 1
			self.num1 = 2
			self.num2 = 3
				
		elif suggesting_player_num == self.my_num and responding_player_num == 2 and revealed_a_card and self.set_flag == 0 and self.my_num == 1 and self.pass_flag == 1:
			self.pass_flag = 0

		if suggesting_player_num == self.my_num and responding_player_num == 3 and not revealed_a_card and self.set_flag == 0 and self.my_num == 1:
			self.pass_flag = 1
			if suggesting_player_num == self.my_num and responding_player_num == 2 and revealed_a_card and self.set_flag == 0 and self.my_num == 1 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 2
				self.num2 = 3
				
			elif suggesting_player_num == self.my_num and responding_player_num == 3 and revealed_a_card and self.set_flag == 0 and self.my_num == 1 and self.pass_flag == 0:
				self.set_flag = 1
				self.num1 = 3
				self.num2 = 2

		elif suggesting_player_num == self.my_num and responding_player_num == 3 and revealed_a_card and self.set_flag == 0 and self.my_num == 1 and self.pass_flag == 0:
			self.set_flag = 1
			self.num1 = 3
			self.num2 = 2

		elif suggesting_player_num == self.my_num and responding_player_num == 3 and revealed_a_card and self.set_flag == 0 and self.my_num == 1 and self.pass_flag == 1:
			self.pass_flag = 0
			
			
		#Check if our rotation is set
		if self.pass_flag == 0:
			#Using our rotation logic check if both players can't help
			if suggesting_player_num == self.my_num and responding_player_num == self.num2 and not revealed_a_card:
				#Change to list
				suggestion = list(suggestion)
				#We do not pick suggestions from our hand and both players said they don't have it, so this is the answer
				#Tell KB that this is the answer, which will trigger accuse
				self.kb.tell("{}{}{}".format("-",str(self.my_num),suggestion[0][0]))
				self.kb.tell("{}{}{}".format("-",str(self.num1),suggestion[0][0]))
				self.kb.tell("{}{}{}".format("-",str(self.num2),suggestion[0][0]))
				
				self.kb.tell("{}{}{}".format("-",str(self.my_num),suggestion[1][0]))
				self.kb.tell("{}{}{}".format("-",str(self.num1),suggestion[1][0]))
				self.kb.tell("{}{}{}".format("-",str(self.num2),suggestion[1][0]))
				
				self.kb.tell("{}{}{}".format("-",str(self.my_num),suggestion[2][0]))
				self.kb.tell("{}{}{}".format("-",str(self.num1),suggestion[2][0]))
				self.kb.tell("{}{}{}".format("-",str(self.num2),suggestion[2][0]))
		
	def secretly_observe(self, responding_player_num, card):
		#Add card to KB
		self.kb.tell("{}{}".format(str(responding_player_num),card[0]))

	def choose_suggestion(self, cards, num):
		#If only one choice, then just pick it
		if len(cards) == 1:
			return cards[0]
			
		#Logic for figuring out other player's nums
		if num == 3 and self.my_num == 1 or num == 1 and self.my_num == 3:
			other_num = 2
		elif num == 2 and self.my_num == 3 or num == 3 and self.my_num == 2:
			other_num = 1
		elif num == 1 and self.my_num == 2 or num == 2  and self.my_num == 1:
			other_num = 3
			    	
		#If there is some wiggle room for which card to show
		if len(cards) > 1:
			#Show a card that we have already shown if possible
			for card in cards:
				if card in self.shown:
					return card
    	
		return cards[0]
		
	def handle_suggestion(self, suggesting_player_num, suggestion):
		num = -1
		possible = []
		#Check if any of the cards from suggestion is in our hand
		if suggestion[0] in self.hand or suggestion[1] in self.hand or suggestion[2] in self.hand:
			#Add all possible choices to possible and check which is the best to return
			for card in self.hand:
				if suggestion[0] == card and card not in possible:
					possible.append(card)
				elif suggestion[1] == card and card not in possible:
					possible.append(card)
				elif suggestion[2] == card and card not in possible:
					possible.append(card)  		
			#Use choose_suggestion to pick best card to return			
			ans = self.choose_suggestion(possible, suggesting_player_num)
			#Add to shown
			self.shown.append(ans)
			return ans
		else:
			return None
    	
    	
    
	def rules(self):
		#KB init
		
		#Add our hand to KB
		for card in self.hand:
			self.kb.tell("{}{}".format(str(self.my_num),card[0]))
    	
    	#Logic for knowing when we have murderer (mu)
		self.kb.tell("-1scarlet ^ -2scarlet ^ -3scarlet => mu")
		self.kb.tell("-1mustard ^ -2mustard ^ -3mustard => mu")
		self.kb.tell("-1plum ^ -2plum ^ -3plum => mu")
		self.kb.tell("-1white ^ -2white ^ -3white => mu")
		self.kb.tell("-1green ^ -2green ^ -3green => mu")
		self.kb.tell("-1peacock ^ -2peacock ^ -3peacock => mu")
    	
    	#Logic for knowing when we have murder weapon (mw)
		self.kb.tell("-1candlestick ^ -2candlestick ^ -3candlestick => mw")
		self.kb.tell("-1revolver ^ -2revolver ^ -3revolver => mw")
		self.kb.tell("-1leadpipe ^ -2leadpipe ^ -3leadpipe => mw")
		self.kb.tell("-1wrench ^ -2wrench ^ -3wrench => mw")
		self.kb.tell("-1knife ^ -2knife ^ -3knife => mw")
		self.kb.tell("-1rope ^ -2rope ^ -3rope => mw")
    	
    	#Logic for knowing when we have murder room (mr)
		self.kb.tell("-1hall ^ -2hall ^ -3hall => mr")
		self.kb.tell("-1kitchen ^ -2kitchen ^ -3kitchen => mr")
		self.kb.tell("-1library ^ -2library ^ -3library => mr")
		self.kb.tell("-1billiardroom ^ -2billiardroom ^ -3billiardroom => mr")
		self.kb.tell("-1study ^ -2study ^ -3study => mr")
		self.kb.tell("-1diningroom ^ -2diningroom ^ -3diningroom => mr")
		self.kb.tell("-1lounge ^ -2lounge ^ -3lounge => mr")
		self.kb.tell("-1ballroom ^ -2ballroom ^ -3ballroom => mr")
		self.kb.tell("-1conservatory ^ -2conservatory ^ -3conservatory => mr")
    	
    	
    	#If we know all three, then we can accuse
		self.kb.tell("mu ^ mw ^ mr => accuse")
		
		#If one player has a card, then eliminate the card for everyone
		self.kb.tell("1scarlet => 2scarlet ^ 3scarlet")
		self.kb.tell("1mustard => 2mustard ^ 3mustard")
		self.kb.tell("1plum => 2plum ^ 3plum")
		self.kb.tell("1white => 2white ^ 3white")
		self.kb.tell("1green => 2green ^ 3green")
		self.kb.tell("1peacock => 2peacock ^ 3peacock")
		
		self.kb.tell("2scarlet => 1scarlet ^ 3scarlet")
		self.kb.tell("2mustard => 1mustard ^ 3mustard")
		self.kb.tell("2plum => 1plum ^ 3plum")
		self.kb.tell("2white => 1white ^ 3white")
		self.kb.tell("2green => 1green ^ 3green")
		self.kb.tell("2peacock => 1peacock ^ 3peacock")
		
		self.kb.tell("3scarlet => 1scarlet ^ 2scarlet")
		self.kb.tell("3mustard => 1mustard ^ 2mustard")
		self.kb.tell("3plum => 1plum ^ 2plum")
		self.kb.tell("3white => 1white ^ 2white")
		self.kb.tell("3green => 1green ^ 2green")
		self.kb.tell("3peacock => 1peacock ^ 2peacock")
		
		
		self.kb.tell("1candlestick => 2candlestick ^ 3candlestick")
		self.kb.tell("1revolver => 2revolver ^ 3revolver")
		self.kb.tell("1leadpipe => 2leadpipe ^ 3leadpipe")
		self.kb.tell("1wrench => 2wrench ^ 3wrench")
		self.kb.tell("1knife => 2knife ^ 3knife")
		self.kb.tell("1rope => 2rope ^ 3rope")
	
		self.kb.tell("2candlestick => 1candlestick ^ 3candlestick")
		self.kb.tell("2revolver => 1revolver ^ 3revolver")
		self.kb.tell("2leadpipe => 1leadpipe ^ 3leadpipe")
		self.kb.tell("2wrench => 1wrench ^ 3wrench")
		self.kb.tell("2knife => 1knife ^ 3knife")
		self.kb.tell("2rope => 1rope ^ 3rope")
    	
		self.kb.tell("3candlestick => 1candlestick ^ 2candlestick")
		self.kb.tell("3revolver => 1revolver ^ 2revolver")
		self.kb.tell("3leadpipe => 1leadpipe ^ 2leadpipe")
		self.kb.tell("3wrench => 1wrench ^ 2wrench")
		self.kb.tell("3knife => 1knife ^ 2knife")
		self.kb.tell("3rope => 1rope ^ 2rope")
    	
		self.kb.tell("1hall => 2hall ^ 3hall")
		self.kb.tell("1kitchen => 2kitchen ^ 3kitchen")
		self.kb.tell("1library => 2library ^ 3library")
		self.kb.tell("1billiardroom => 2billiardroom ^ 3billiardroom")
		self.kb.tell("1study => 2study ^ 3study")
		self.kb.tell("1diningroom => 2diningroom ^ 3diningroom")
		self.kb.tell("1lounge => 2lounge ^ 3lounge")
		self.kb.tell("1ballroom => 2ballroom ^ 3ballroom")
		self.kb.tell("1conservatory => 2conservatory ^ 3conservatory")
	
		self.kb.tell("2hall => 1hall ^ 3hall")
		self.kb.tell("2kitchen => 1kitchen ^ 3kitchen")
		self.kb.tell("2library => 1library ^ 3library")
		self.kb.tell("2billiardroom => 1billiardroom ^ 3billiardroom")
		self.kb.tell("2study => 1study ^ 3study")
		self.kb.tell("2diningroom => 1diningroom ^ 3diningroom")
		self.kb.tell("2lounge => 1lounge ^ 3lounge")
		self.kb.tell("2ballroom => 1ballroom ^ 3ballroom")
		self.kb.tell("2conservatory => 1conservatory ^ 3conservatory")
   	
		self.kb.tell("3hall => 1hall ^ 2hall")
		self.kb.tell("3kitchen => 1kitchen ^ 2kitchen")
		self.kb.tell("3library => 1library ^ 2library")
		self.kb.tell("3billiardroom => 1billiardroom ^ 2billiardroom")
		self.kb.tell("3study => 1study ^ 2study")
		self.kb.tell("3diningroom => 1diningroom ^ 2diningroom")
		self.kb.tell("3lounge => 1lounge ^ 2lounge")
		self.kb.tell("3ballroom => 1ballroom ^ 2ballroom")
		self.kb.tell("3conservatory => 1conservatory ^ 2conservatory")
    	
    	
    	
