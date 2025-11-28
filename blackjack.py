import csv
import random

def read_money_file():
    with open("money.csv", newline="") as file:
        reader= csv.reader(file)
        for row in reader:
            current_money=float(row[1])

    return current_money

def write_money_file(current_money):
    with open("money.csv", "w", newline="") as file:
        writer=csv.writer(file)
        new_balance= round(current_money, 2)
        writer.writerow(["Money", new_balance])

#prototype idea of dealer's show card for the time being
#switching the suit, rank and point_value arg to main
def get_deck_list(suit, rank, point_value):

    """suit_choice=random.choice(suit)
    rank_choice=random.choice(rank)
    print(f"{rank_choice} of {suit_choice}")"""
    deck=[]
    for suits in suit:
        for i, ranks in enumerate(rank):
            point=point_value[i]
            card=[suits, ranks, point]
            deck.append(card)
        random.shuffle(deck)


    print(deck)






def main():
    suit= ["Hearts", "Diamonds", "Clubs", "Spades"]
    rank=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    point_value=["2", "3", "4", "5", "6", "7", "8", "9", "10","10","10", "10", "11"]
    get_deck_list(suit,rank,point_value)

if __name__=="__main__":
    main()










