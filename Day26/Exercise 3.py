'''Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.'''


ques = ["Who is the captain of England Men's cricket team of 2023 ICC Worldcup? ", 
       "Who is the captain of Australia Men's cricket team of 2023 ICC Worldcup?",
       "Who is the captain of India Men's cricket team of 2023 ICC Worldcup?",
       "Who is the captain of Bangladesh Men's cricket team of 2023 ICC Worldcup?"]


ans1 = ['1. Josh Butler', '2. Moin Ali', '3. Joe Root', '4. Bean Stokes']
ans2 = ['1. Maxwell', '2. Steve Smith', '3. Pet Cummins', '4. David Warner']
ans3 = ['1. Virat Kohli', '2. Rohit Sharma', '3. KL Rahul', '4. Hardik Pandya']
ans4 = ['1. Mehedi Miraz', '2. Liton Das', '3. Nazmul Shanto', '4. Shakib Al Hasan']


point = 0



####################### First Round ###############################

print("Ready for the 1st Round? press YES for 1 or NO for 0")

key1 = int(input("Enter here: "))



if key1 == 0:
    print("Round 1 is Over")

else:
    print(ques[0])
    print(ans1)
    user_ans = int(input("\nEnter your answer --->> Option 1 or Option 2 or Option 3 or Option 4: "))
    
    if user_ans == 1:
        point += 10
        print(f"Correct Answer..!! You get {point} points")

    elif user_ans != 0:
        print("Wrong Answer...!")
        print(f"Your Current Points is {point}")

print("\nRound 1 is Over")
    

####################### Second Round ###############################


print("\nReady for the 2nd Round? press YES for 1 or NO for 0")

key1 = int(input("Enter here: "))



if key1 == 0:
    print("Round 2 is Over")

else:
    print(ques[1])
    print(ans2)
    user_ans = int(input("\nEnter your answer --->> Option 1 or Option 2 or Option 3 or Option 4: "))
    
    if user_ans == 3:
        point += 10
        print(f"Correct Answer..!! You get {point} points")

    elif user_ans != 3:
        print("Wrong Answer...!")
        print(f"Your Current Points is {point}")

print("\nRound 2 is Over")   


####################### Third Round ###############################


print("\nReady for the 3rd Round? press YES for 1 or NO for 0")

key1 = int(input("Enter here: "))



if key1 == 0:
    print("Round 3 is Over")

else:
    print(ques[2])
    print(ans3)
    user_ans = int(input("\nEnter your answer --->> Option 1 or Option 2 or Option 3 or Option 4: "))
    
    if user_ans == 2:
        point += 10
        print(f"Correct Answer..!! You get {point} points")

    elif user_ans != 2:
        print("Wrong Answer...!")
        print(f"Your Current Points is {point}")

print("\nRound 3 is Over")   


####################### Fourth Round ###############################


print("\nReady for the 4th Round? press YES for 1 or NO for 0")

key1 = int(input("Enter here: "))



if key1 == 0:
    print("Round 4 is Over")

else:
    print(ques[3])
    print(ans4)
    user_ans = int(input("\nEnter your answer --->> Option 1 or Option 2 or Option 3 or Option 4: "))
    
    if user_ans == 4:
        point += 10
        print(f"Correct Answer..!! You get {point} points")

    elif user_ans != 4:
        print("Wrong Answer...!")
        print(f"Your Current Points is {point}")
    
print("\nRound 4 is Over")
    
    
print(f"\n\nYour total points is {point}")

if point == 40:
    print("Congress..! You win 1 Crore Rupee")

elif point == 30:
    print("Congress..! You win 50 Lakh Rupee")

elif point == 20:
    print("Congress..! You win 25 Lakh Rupee")

elif point == 10:
    print("Congress..! You win 10 Lakh Rupee")

elif point == 0:
    print("Sorry..! You win nothing. Better Luck Next Time")


print("KBC Game Is Over")