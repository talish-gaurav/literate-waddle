com = False
while not com:
  try:
    num= int(input("Enter any number"))
    while num%2==0:

        print("Bye!")
    com=True
  except ValueError:
    print("Invalid Input! Command Failed!")