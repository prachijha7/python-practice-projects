from game_data import data
from art import logo,vs
import random
import os

def get_random_choice():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
def correct(ans, a, b):
    if(a["follower_count"] > b["follower_count"]):
        if ans == "a":
            return True
        else:
            return False
    else:
        if ans == "b":
            return True
        else:
            return False
        
def right(result, sc):
    if result:
        sc += 1
        print(f"You're right! Current score: {sc}.")
        return sc
    else:
        print(f"Sorry, that's wrong. Final score: {sc}")
        return sc

is_correct = True 
score = 0

account_a = get_random_choice()
account_b = get_random_choice()
while account_a == account_b:
    account_b = get_random_choice()

while is_correct:
    print(logo)
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = correct(answer, account_a, account_b)
    score = right(is_correct, score)
    if is_correct:
        account_a = account_b
        account_b = get_random_choice()
        os.system("clear")
        while account_a == account_b:
            account_b = get_random_choice()