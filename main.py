#Display art 
from art import logo, vs
from game_data import data
import random

print(logo)

def get_record(data):
    return random.choice(data)


#write a function to compare results
def avoid_same_record(record_a, record_b):
     # make sure there are no duplicate records
    if record_a==record_b:
        record_b = get_record(data)  
        print(f"Against B: {record_b['name']}, a {record_b['description']}, from {record_b['country']}.")

    else:
         print(f"Against B: {record_b['name']}, a {record_b['description']}, from {record_b['country']}.")

current_score=0
final_score=0

while True:
    record_a = get_record(data)  
    #print(record_a)
    print(f"Compare A: {record_a['name']}, a {record_a['description']}, from {record_a['country']}.")
    print(vs)
    record_b = get_record(data)  
    avoid_same_record(record_a, record_b)
    
    answer=input("Who has more followers? Type 'A' or 'B': ")
    
    if answer.upper()=="A":
        if record_a["follower_count"] > record_b["follower_count"]:
            current_score+=1
            print(f"Congratulations! You are correct. {record_a['name']} has more followers than {record_b['name']}.  Current score: {current_score}")
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
        else:
            print(logo)
            final_score=current_score
            print(f"Sorry, that's wrong. Final score: {final_score}")
            break 
    else:
        print(logo)
        print("Invalid input. Please try again.")
        break 


    
   
        

    
        



