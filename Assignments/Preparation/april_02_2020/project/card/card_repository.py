from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    def add(self, card: Card):
        if any(c.name == card.name for c in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card_name: str):
        if card_name == "":
            raise ValueError("Card cannot be an empty string!")
        card_to_remove = self.find(card_name)
        self.cards.remove(card_to_remove)

    def find(self, name: str):
        found_card = [card for card in self.cards if card.name == name][0]
        return found_card

    @property
    def count(self):
        return len(self.cards)
