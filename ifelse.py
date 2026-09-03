#if else conditions
#below example will print if the condition matches

number = 15
if number > 0:
  print("The number is positive")

#asking user to print a number
a = int(input("enter a number between 0 to 10"))
if a >= 5:
    print("you are above 50%")
else:
    print("you are below 50%")


#multiple else if
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
