import random

score = 0

while score !=10 and score !=-10 :


  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)

  print(f"waht is {num1} times {num2}?")

  user_unswer = int(input("enter your answer:"))

  correct_number = num1 * num2

  if user_unswer == correct_number : 
   score += 1
   print("good job")
   print(f"you score is : {score}")
  else : 
   score -=1
   print("wrong")
   print(f"this is the correct answer: {correct_number}")
   print(f"you score is : {score}")
  if score ==10 :
    print("good job")