#Display art 
from art import logo, vs
from game_data import data
import random

print(logo)

def get_record(data):
    return random.choice(data)

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."

#write a function to compare results
def avoid_same_record(record_a, record_b):
    against_b = print(f"Against B: {format_data(record_b)}.")
     # make sure there are no duplicate records
    if record_a==record_b:
        record_b = get_record(data)  
        against_b
    else:
        against_b

current_score=0
final_score=0
next_record_a=None
next_record_b=None


while True:
    if next_record_a is not None:
        record_a=next_record_a
        next_record_a=None
    elif next_record_b is not None:
        record_a=next_record_b
        next_record_b=None
    else:
        record_a = get_record(data)  
        #print(record_a)
    print(f"Compare A: {format_data(record_a)}.")
    print(vs)
    record_b = get_record(data)  
    avoid_same_record(record_a, record_b)
    
    answer=input("Who has more followers? Type 'A' or 'B': ")
    
    if answer.upper()=="A":
        if record_a["follower_count"] > record_b["follower_count"]:
            current_score+=1
            print(f"Congratulations! You are correct. {record_a['name']} has more followers than {record_b['name']}.  Current score: {current_score}")
            #set record_a to be the next record to be compared
            next_record_a=record_a
        else:
            print(logo)
            final_score=current_score
            print(f"Sorry, that's wrong. Final score: {final_score}")
            break 
    elif answer.upper()=="B":
        if record_a["follower_count"] < record_b["follower_count"]:
            current_score+=1
            #print new line to clear the previous output
            print("\n")
            print(f"Congratulations! You are correct. {record_b['name']} has more followers than {record_a['name']}.  Current score: {current_score}")
            print("\n")
            #set record_b to be the next record to be compared
            next_record_b=record_b
        else:
            print(logo)
            final_score=current_score
            print(f"Sorry, that's wrong. Final score: {final_score}")
            break 
    else:
        print(logo)
        print("Invalid input. Please try again.")
        break 


    
   
        

    
        



