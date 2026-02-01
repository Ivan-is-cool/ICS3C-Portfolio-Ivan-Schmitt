age = int(input("What it is your age?: "))
student_discount = input("Are you a student? (y/n): ")

if age <= 12 and student_discount == "yes":
    print("It costs 8 dollars to watch a  movie")
if age >= 12 and age <=17:
    print ("It cost 10 dollars to watch a movie")
if age >= 18 and age <=64:
    print ("It cost 12 dollars to watch a movie")
if age >= 65:
    print("It cost 6 dollars to watch a movie")
