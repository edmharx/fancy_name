#this is a pseudocode
#importing art module
from art import *

#creating input for the name
name = input("Kindly type your name: ")

#creating input for the dream job
job = input("What is your dream job?: ")

#creating input for age, sex, location

age = input("How old are you?: ")
sex = input("State you sex: ")
loc = input("Where do you live?: ")


#creating the art

name_art = text2art(name, font="bubblehead")
job_art = art("kirby") + decor("wave2") + text2art(job, font="fancy99") + decor("wave2", reverse=True)
age_art = art("kirby") + decor("wave5") + text2art(age, font="fancy132") + decor("wave5", reverse=True)
sex_art = art("kirby") + decor("wave5") + text2art(sex, font="fancy132") + decor("wave5", reverse=True)
loc_art = art("kirby") + decor("wave5") + text2art(loc, font="fancy132") + decor("wave5", reverse=True)

#printing
print(name_art)
print(job_art)
print(age_art)
print(sex_art)
print(loc_art)

