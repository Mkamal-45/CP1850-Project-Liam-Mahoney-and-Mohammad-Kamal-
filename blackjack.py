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
def get_deck_list():
    suit= ["Hearts", "Diamonds", "Clubs", "Spades"]
    rank=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    point_value=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    """suit_choice=random.choice(suit)
    rank_choice=random.choice(rank)
    print(f"{rank_choice} of {suit_choice}")"""
    deck=[]
    for suits in suit:
        for ranks in rank:
            point=point_value
            deck.append([ranks, suits, point])
        random.shuffle(deck)


    print(deck)






def main():
    get_deck_list()

if __name__=="__main__":
    main()










