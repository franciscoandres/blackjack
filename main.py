import random, time, functions

print("*************")
print("* Blackjack *")
print("*************\n")

deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards_crupier = []
cards_user    = []

while True:

	print("Repartiendo cartas...")
	time.sleep(1)

	card_crupier, card_user = functions.random_card(deck), functions.random_card(deck)

	cards_crupier.append(card_crupier)
	cards_user.append(card_user)

	print("Crupier: {}".format(card_crupier))
	print("Tu: {}".format(card_user))