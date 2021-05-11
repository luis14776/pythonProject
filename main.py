# Let's Lose Fat! program main code

print('''Lets Lose Fat!

Welcome ;) This is Jen, I am gonna ask you some questions to make you achieve your goals.
Type the letter K and hit enter to continue
''')
ok = input()
if ok != 'k':
    print("Sorry I can't read that. Type k to continue")
    ok = input()
if ok.lower() == 'k':
    measure = input('''We are going to ask you some questions about you,
    but first please type up the type of measurement you prefer = M (metric) or F (Feet)''')
    if measure.upper() == 'M':
        height = input("What's your height in cm? = ")
        weight = input("What's your weight in kilos? = ")
        con_height = int(height) / 100     # convertion of cm to m for the formula
        ibm = int(weight) / (con_height)**2
    elif measure.upper() == 'F':
        print("What's your height? (first type feet and then inches) = ")
        height = input('How many feet? = ')
        inches = input('How many inches? = ')
        weight = input("What's your weight in pounds? = ")
        con_height = (int(height) * 12) + int(inches)  # convertion of feet to inches for the ibm formula
        ibm = (703 * int(weight)) / (con_height) ** 2
    elif measure != 'F' or measure != 'M':
        print('sorry I cannot read that')
        measure = input('Choose M or F')
if ibm >= 25 and ibm < 30:
    print('''Apparently you have been eating a lot, but do not worry, we got you ;).
            Just follow the following routine, and you will se instant changes in the next three weeks:
            Eat a high protein breakfast. ...
            1) Avoid sugary drinks and fruit juice. ...
            2) Drink water before meals. ...
            3) Choose weight-loss-friendly foods. ...
            4) Eat soluble fiber. ...
            5) Drink coffee or tea. ...
            6)Base your diet on whole foods. ...
            7)Eat slowly.

            Good luck!''')
elif ibm < 25 and ibm >0:
    print('''Keep your habits. You are doing an excellent job ;)''')
elif ibm >= 30:
    print('You need to see an doctor and nutritionist. You are obese')













