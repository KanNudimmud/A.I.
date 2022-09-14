### Monty Hall Simulation
## Import libraries
import random
import matplotlib.pyplot as plt

## Create a function for the host to reveal a door that
## does not contain the prize and a door that is not
## the contestants original choice
def get_non_prize_door(host, num_doors, player_choice):
    i=1
    while(i==host or i==player_choice):
        i=(i+1)%(num_doors)
    return i

## Create a function to have the player switch to the other unopened door
def switch_function(shown_door, num_doors, player_choice):
    i=1
    while(i==shown_door or i==player_choice):
        i=(i+1)%(num_doors)
        return i
 
## Create a function to simulate the game
def monty_hall_game(switch, num_tests):
    win_switch_cnt=0
    win_no_switch_cnt=0
    lose_switch_cnt=0
    lose_no_switch_cnt=0
    
    doors = [0,1,2]
    num_doors=len(doors)
    
    #Loop through the number of times the player can play the game
    for i in range(0, num_tests):
        door_with_prize=random.randint(0,num_doors-1) # choosing a door
        host=door_with_prize
        player_choice=random.randint(0,num_doors-1)
        original_player_choice=player_choice
        shown_door= get_non_prize_door(host, num_doors, player_choice)
        
        #If the player picks to always switch, then allow the player
        #to switch their original chosen door to the other unopened door
        if switch==True:
            player_choice=switch_function(shown_door,num_doors,player_choice)
            
        if player_choice==door_with_prize and switch==False:
            #Then the player wins from not switching
            print('Player Wins (No switch) - The player choose door #:', 
                  player_choice, 'Original door choice:',
                  original_player_choice, 'Door with prize:',
                  door_with_prize,'Shown Door:', shown_door)
            win_no_switch_cnt=win_no_switch_cnt+1
            
        elif player_choice==door_with_prize and switch==True:
            #Then the player wins from switching
            print('Player Wins (switch) - The player choose door #:', 
                  player_choice, 'Original door choice:',
                  original_player_choice, 'Door with prize:',
                  door_with_prize,'Shown Door:', shown_door)
            win_switch_cnt=win_switch_cnt+1
        elif player_choice!=door_with_prize and switch==False:
            #Then the player lost from not switching
            print('Player Lost (No switch) - The player choose door #:', 
                  player_choice, 'Original door choice:',
                  original_player_choice, 'Door with prize:',
                  door_with_prize,'Shown Door:', shown_door)
            lose_no_switch_cnt=lose_no_switch_cnt+1  
        elif player_choice!=door_with_prize and switch==True:
            #Then the player lost from switching
            print('Player Lost (switch) - The player choose door #:', 
                  player_choice, 'Original door choice:',
                  original_player_choice, 'Door with prize:',
                  door_with_prize,'Shown Door:', shown_door)
            lose_switch_cnt=lose_switch_cnt+1
        else:
            print('Warning !!!')
    return win_no_switch_cnt, win_switch_cnt, lose_no_switch_cnt, lose_switch_cnt, num_tests

## Play the game
x = monty_hall_game(True,10)

## Get the win&lost percentage for switching or not switching
print('Win switch %: ', x[1]/x[4])
print('Lose switch %: ', x[3]/x[4])
print('Win No switch %: ', x[0]/x[4])
print('Lose No switch %: ', x[2]/x[4])

## Get the data to create a visualization of the number of simulated
## games played and the percentage of wins from always switching
num_tests = []
win_percentage = []
switch = True

# Simulate 1000 games
for i in range(1,1001):
    num_tests.append(i)
    y=monty_hall_game(switch,i)
    win_percentage.append(y[1]/y[4])
    
# Visualize
plt.plot(num_tests, win_percentage)
plt.title('Monty Hall Problem')
plt.xlabel('Number of tests')
plt.ylabel('Win percentage')
plt.show()

           
        
        