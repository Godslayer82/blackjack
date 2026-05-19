import random

# Card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10,
    'K': 10, 'A': 11
}

# Create deck
def create_deck():
    deck = list(card_values.keys()) * 4
    random.shuffle(deck)
    return deck

# Calculate hand value
def calculate_hand(hand):
    total = sum(card_values[card] for card in hand)
    aces = hand.count('A')

    # Adjust aces from 11 to 1 if needed
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

# Display hand
def show_hand(name, hand, hide_first=False):
    if hide_first:
        print(f"{name}'s hand: ['?', '{hand[1]}']")
    else:
        print(f"{name}'s hand: {hand} (Total: {calculate_hand(hand)})")

# Main game
def blackjack():
    print("=== Welcome to Blackjack ===")

    deck = create_deck()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Player turn
    while True:
        show_hand("Dealer", dealer_hand, hide_first=True)
        show_hand("Player", player_hand)

        if calculate_hand(player_hand) == 21:
            print("Blackjack!")
            break

        if calculate_hand(player_hand) > 21:
            print("You busted! Dealer wins.")
            return

        choice = input("Hit or Stand? (h/s): ").lower()

        if choice == 'h':
            player_hand.append(deck.pop())
        elif choice == 's':
            break
        else:
            print("Invalid choice.")

    # Dealer turn
    print("\nDealer's turn...")
    show_hand("Dealer", dealer_hand)

    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        show_hand("Dealer", dealer_hand)

    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    # Determine winner
    print("\n=== Final Results ===")
    show_hand("Player", player_hand)
    show_hand("Dealer", dealer_hand)

    if dealer_total > 21:
        print("Dealer busted! You win!")
    elif player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    blackjack()
