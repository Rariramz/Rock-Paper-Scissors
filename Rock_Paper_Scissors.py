from random import choice

# Write your code here

winning_cases = {'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
                 'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
                 'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
                 'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
                 'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
                 'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
                 'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
                 'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
                 'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
                 'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
                 'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
                 'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
                 'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
                 'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
                 'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']}

name = input("Enter your name: ")
print(f"Hello, {name}")

queue = []
str_ = input()
if str_ == "":
    queue = ["rock", "paper", "scissors"]
else:
    queue = str_.split()
print("Okay, let's start")    


rating = 0
f = open("rating.txt", 'r')
for line in f:
    name_, rating_ = line.split()
    if name_ == name:
        rating = int(rating_)
f.close()
    
while True:
    user_inp = input()
    option = choice(queue)
    
    if user_inp in winning_cases.keys():
        if option == user_inp:
            res = "Draw"
        elif option in winning_cases.get(user_inp):
            res = "Win"
        elif option not in winning_cases.get(user_inp):
            res = "Lose"
    elif user_inp == "!exit":
        print("Bye!")
        break
    elif user_inp == "!rating":
        print(f"Your rating: {rating}")
        break
    else:
        print("Invalid input")

    if res == "Lose":        
        print(f"Sorry, but computer chose {option}")
    elif res == "Draw":
        rating += 50
        print(f"There is a draw ({option})")
    elif res == "Win":
        rating += 100
        print(f"Well done. Computer chose {option} and failed")
