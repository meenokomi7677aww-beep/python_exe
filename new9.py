import random
import datetime

num = random.randint(1,5)

print(f"Your number is {num}")

students = ["may thae","yamone","min khan","wanna","ethan"]
ran_std = random.choice(students)

print(f"Your name is {ran_std}.")
today = datetime.datetime.now().strftime("%A")
print(f"Today is {today}")
