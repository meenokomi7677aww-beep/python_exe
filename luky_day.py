import random
import datetime

def lucky_day_picker():
    print("💓lucky day picker!")
    print("=" * 30)
    day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","sunday"]

    to_do = {"Monday", "eating"
             "Tuesday","sleeping"
             "Wednesday","playing"
             "Thursday","talking"
             "Friday","hang out"
             "Saturday","family time"
             "sunday" "do nothing"}



    lucky_day = random.choice(day)

    print(f"Your lucky day is: {lucky_day}!")
    print(f"Suggest activity is {to_do[lucky_day]}")
    
    today = datetime.datetime.now().strftime("%A")
    print(f"Today is : {today}")

    if (today == lucky_day):
        print ("Wow! Today is your lucky day!💢")
    else:
        print(f"your lucky day is:{lucky_day}!")

        
    lucky_day_picker()




