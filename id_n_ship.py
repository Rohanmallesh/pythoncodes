# Write a program that takes in a letterclass ID of a ship and display the 
# equivalent string class description of the given ID. Use the table below.

# Class ID	Ship Class
# B or b	BattleShip
# C or c	Cruiser
# D or d	Destroyer
# F or f	Frigate

# Input Format
# The first line contains an integer T, the total number of testcases.
# Then T lines follow, each line contains a character.
dic = {'b':'BattleShip','c':'Cruiser','d':'Destroyer','f':'Frigate'}
for i in range(int(input())):
    s = input().lower()
    print(dic[s])




