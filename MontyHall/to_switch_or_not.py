
import numpy as np

number_to_door_configuration = {
1: {
0: 0, 
1: 0, 
2: 1
},

2: {
0: 0,
1: 1,
2: 0
},

3: {
0: 1,
1: 0,
2: 0}

}

sample_size = 1000000
occurrences = np.random.choice([1, 2, 3], size=(sample_size))
count_1 = len([x for x in occurrences if x == 1])
count_2 = len([x for x in occurrences if x == 2])
count_3 = len([x for x in occurrences if x == 3])

percent_1 = count_1*100/sample_size
percent_2 = count_2*100/sample_size
percent_3 = count_3*100/sample_size

description = """

Monty hall postulates:
If I select a door out of 3 and one of them has a reward. Should I switch doors and how will it affect probability?
Given that after I select a door, I am given new information by opening one of the remaining two doors.
Now I am given a choice - Stick to my selection or switch doors.

Here is this program's decision making logic.
When I'm given a choice - use the strategy - select one of the remaining two doors with 50-50 probability.
Eenie meenie miney mo strategy.

Now count the probability I win the prize. It should be 50%.

"""

def eenie_meenie_miney_mo(choices):
  return np.random.choice(list(sorted(choices)))

def choose_strategy(config_number, strategy):
  doors = number_to_door_configuration[config_number]
  #print(f"{doors=}")
  my_selection = np.random.choice([0, 1, 2])
  #print(f"{my_selection=}")
  not_selected = [door for door in [0, 1, 2] if door!=my_selection]
  #print(f"{not_selected=}")
  eliminated = np.random.choice([door for door in not_selected if doors[door]==0])
  #print(f"{eliminated=}")
  not_eliminated = np.random.choice([door for door in not_selected if door!=eliminated])
  #print(f"{not_eliminated=}")
  remaining = [my_selection, not_eliminated]
  #print(f"{remaining=}")
  final_selection = strategy(remaining)
  #print(f"{final_selection=}")
  return doors[final_selection]
  
outcome_eenie = [choose_strategy(config_number, eenie_meenie_miney_mo) for config_number in occurrences]
count_win_eenie = len([x for x in outcome_eenie if x==1])
count_lose_eenie = len([x for x in outcome_eenie if x==0])
percent_win_eenie = count_win_eenie * 100 / sample_size
percent_lose_eenie = count_lose_eenie * 100 / sample_size

optimal_solution = """

Now the strategy for Eenie Meenie Miney Mo are 50% as visible.

Let's try out two new strategies.
Instead of 50-50 on the two remaining doors we will

1. Switch - Always switch the door strategy from the one initially chosen. And count the wins. And percent it for conditional probability.
2. Stick - Always stick with the door initially chosen. And count the wins. And percent it for the conditional probability.

"""

def switch(choices):
  return choices[1]

def stick(choices):
  return choices[0]

outcome_switch = [choose_strategy(config_number, switch) for config_number in occurrences]
count_win_switch = len([x for x in outcome_switch if x==1])
count_lose_switch = len([x for x in outcome_switch if x==0])
percent_win_switch = count_win_switch * 100 / sample_size
percent_lose_switch = count_lose_switch * 100 / sample_size

outcome_stick = [choose_strategy(config_number, stick) for config_number in occurrences]
count_win_stick = len([x for x in outcome_stick if x==1])
count_lose_stick = len([x for x in outcome_stick if x==0])
percent_win_stick = count_win_stick * 100 / sample_size
percent_lose_stick = count_lose_stick * 100 / sample_size

explanation = """

So why does this work? 
Why is the win probability 66.66% for switch which is the best solution?
And stick which has win probability 33.33% which is the worst solution?

There are 3 approaches to explain this

1. Counting down from N doors

If there were 10 doors, I selected a door. That is 1/10 win probability and 9/10 lose probability.
Out of the remaining 9 doors, 8 were opened. Now it is clear I might have to switch to the other door.





2. If I picked a door out of 3, the lose probability is 2/3. If one door is opened of the remaining two. 
The probability of the other door remaining unopened being the incorrect one is 1/3.
This is using the negative/complementary probability(1-p) to give a more intuitive explanation.





3. Using condition probability tables

Let's say the reward location is random

Door configuration probability

Door 1 - 1/3 chance reward

Door 2 - 1/3 chance reward

Door 3 - 1/3 chance reward

Now for Door 1 configuration(Door 1 has the reward) conditional probability

Selection probability
Door 1 - (1/3 * 1/3) chance reward = 1/9
Door 2 - 0 chance reward
Door 3 - 0 chance reward

But if we factor in the one wrong door reveal into this where the person MUST open a wrong door.

Now he has to open Door 2 or Door 3
Door 2 - 1/2 chance to open
Door 3 - 1/2 chance to open

If opened Door 2 given Door 1 is reward
Door 1 and Door 3 are unopened.
The probability I selected Door 1 - 1/3
The probability I selected Door 3 - 1/3

If I switch -
The probability I switched to Door 1 - 2/3
The probability I switched to Door 3 - 2/3

Reward probability for if I switched to other door
Door 1 - 1/2 * 2/3 * 1/3 chance reward = 1/9
Door 3 - 1/2 * 2/3 * 0 chance reward = 0

Now I repeat for if opened Door 3 given Door 1 is reward

Reward probability
Door 1 - 1/2 * 2/3 * 1/3 chance reward = 1/9
Door 3 - 1/2 * 2/3 * 0 chance reward = 0

Now for summing up the cases 1/9 + 1/9 = 2/9 total probability for the case Door 1 configuration.

Similarly repeating for Door 2 and 3 configuration = 2/9, 2/9

Total probability = 2/9 + 2/9 + 2/9 = 6/9 = 2/3 = 66.66% winrate for switching doors.





4. Obviously true by symmetry solution

The Bayes ratios for the three doors move from

1 : 1 : 1 to 1 : 2 : 0

Thus switching is better.



"""

quantum_note = """

If you notice, choices is not a sorted array at all times. 
Feel free to interpret this as 100% certainity of winning by having access to this data.
Also refactor the code to observe the result differently to eliminate Observer bias for quantum mechanical testing.
:D

This concludes the solution by simulation. 
Alternate approaches to solve are Bayes theorem, Condition probability approach, Intuitive direct approach.
The problem can be increased to N doors from 3 doors.
It gives (1/N)*(N-1)/(N-p-1) for switching which is an advantage. p here is how many losing doors were opened.

"""

clarity_and_reverse_psychology = """




Here are some things that need clarity about the host, system, problem statement and reverse psychology that gives the wrong answer intuitively because the question has been phrased poorly(which is why Monty hall is a poorly phrased question and gives wrong intuitive answer)


1. In real life, the conditional probability starts at 0 doors opened. It is not clear that the host MUST open one wrong door because it sounds like a figure of speech or matter of phrasing.
If the host could choose 50-50 whether to open a door after knowing the selection of door I made, it would affect the probability and my intuition.



2. If I added the conditional probability of reverse psychology combined with survival instincts/intuition in a zero-sum game
The probability of winning for switch is 2/3
The probability of winning for stick is 1/3

Now assume before the final selection is made the reward can be swapped between the two doors.
So there is 2/3 percent chance that the door for switch is rigged to fail.
1/3 percent chance that door for stick is still rigged to fail.
This is layer 1 double reverse psychology.

For layer 2 - I expect the host to understand that I understand the rigging so he rigged again/deeper.
There is an additional 1/2 * 1/3 = 1/6 percent chance door for switch is rigged to fail.
There is an additional 1/2 * 2/3 = 2/6 percent chance door for stick is rigged to fail.

Adding this to infinity we get 50-50 is optimal choice. 
Stopping the conditional probability chains before infinity, there are many scenarios where it is better probability to stick to the initially selected door than to switch based on the coefficient multipliers on the switch and stick scenarios. 


If there was only one time I could run the trial- it is better to choose randomly to switch or stick.
Even if the trial has to run a million times - it is better to choose randomly to switch or stick if foul play is expected.
Eenie meenie miney mo is the best option with 50% win/lose chance.
In fact there is no guarantee of best option in case of foul play as trial results and counts will deviate significantly from expectations.
50-50 chance here is the punishment probability to inflict maximum damage on the foul play going on over many trials which comes naturally coded in humans for survival given that once I make the final selection, all 3 doors are opened immediately.
Even better if my choice is on a paper, all 3 doors are opened and then the answer on the paper I wrote in past is shown.
But if after my choice is declared publically, there is a long delay in opening the doors, I would prefer to switch, to show a pattern of foul play if it exists over a period of time or to detect a shifting behind doors.


3. The clarity that the configuration and choices are truly random is not clear. 
The condition of foul play is explained here.
Foul play involves -
a. Knowing the choice of initial selection(incentive).
b. Knowing the location of reward(violation of independence/randomness of events).
c. Having the choice to open 0 or more losing door(suggestion).
d. Having incentive/want/desire to give/not give reward(violation of independence).


The biggest problem with the Monty Hall problem is not about 66.66% for switch win probability instead of 50% winrate.
The biggest problem with the Monty Hall problem is convincing people of true randomness and independence of effects outside external influence without factors like foul play, reverse psychology and zero sum games for just a 16.66% increase.
For this natural defense mechanism, people will have trouble being explained the problem correctly, trouble with cooperation, trouble with validation through speech, trouble with denial and acceptance even when shown results and simulations. 


I myself do not agree with the result of the simulation I created because it does not mirror the real world accurately practically.


If I had to say theoretically only, I would still prefer simulation to calculate probability over theoretical calculation.
The Monty hall problem is a proponent of The Simulation Theory of the origin of our universe and the rise of Black-box Deep Neural Networks.
This is a menace because it is not necessarily an accurate representation of reality, in fact it might and is probably is even further to the ideal/accurate representation of reality.
I find it necessary to include this note because most people do not like sharing personal views, which in the case of Monty hall problem constitutes implicit agreement to the implied views and conclusions drawn through silence.



Here is what the Monty Hall problem looks like without deceptive wordplay.
1. There are 3 doors behind which there is one prize and two empty doors.
2. Other people are walking behind the doors and can see/touch what is inside.
3. The event is being livestreamed with no delay and many trusted people can confirm the same.
4. I am behind a soundproof glass without any electronic devices to see the live stream or get a hint.
5. I select a door to open initially.
6. I am given a choice to open one of the other two doors which I did not select.
7. The instant I make a choice, either of the two doors which I did not select initially open.
8. I am allowed to choose an open door for the reward as well.
9. I am given a choice to switch doors or stick with my selection.
10. What will be the best strategy here for the reward?
11. I choose to switch doors from my initial selection. What is the probability I win the reward?


"""

if __name__ == "__main__":
  print(f"Occurrences of configuration 1 are {count_1}. Percentage: {percent_1:.2f}% ")
  print(f"Occurrences of configuration 2 are {count_2}. Percentage: {percent_2:.2f}% ")
  print(f"Occurrences of configuration 3 are {count_3}. Percentage: {percent_3:.2f}% ")
  print(f"The error variance is the deviation of these values from 33.33%.\nThe sample size is {sample_size}.\nIncreasing sample size will reduce standard deviation.")
  print(description)
  print("And the results are:")
  print(f"EenieMMM wins: {count_win_eenie}. Percentage: {percent_win_eenie}%")
  print(f"EenieMMM lose: {count_lose_eenie}. Percentage: {percent_lose_eenie}%")
  print(optimal_solution)
  print("And the results are:")
  print(f"Stick with selection wins: {count_win_stick}. Percentage: {percent_win_stick}%")
  print(f"Stick with selection lose: {count_lose_stick}. Percentage: {percent_lose_stick}%")
  print("\n\n")
  print(f"Switch to other door wins: {count_win_switch}. Percentage: {percent_win_switch}%")
  print(f"Switch to other door lose: {count_lose_switch}. Percentage: {percent_lose_switch}%")
  print(explanation)
  print(clarity_and_reverse_psychology)




