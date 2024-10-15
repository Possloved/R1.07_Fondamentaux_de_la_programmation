admin_username_list = ["useradmin"]
admin_password_list = ["Admin123"]
z = 0
login_loop = 0
choice_loop = 0
student_list = []
choice_2_lock = 0

def add_name(x):
  loop = 0
  add_name_loop = int(input("How many names do you want to add: "))
  while loop < add_name_loop:
    x.append(input("Enter the name please: "))
    loop = loop + 1

def add_grade(x):
  loop = 0
  add_grade_loop = len(student_list)
  while loop < add_grade_loop:
    x.append(input("Enter the grade please: "))
    loop = loop + 1



while login_loop < 1:
  admin_username_check = input("Enter username: ")

  UsernameLoc = len(admin_username_list)
  for a in range(UsernameLoc) :
    if admin_username_check == admin_username_list[a] :
      z = a 
    
  admin_password_check = input("Enter password : ")

  if admin_password_check == admin_password_list[z]:
    print("\nYou are now logged in")
    login_loop = 1
    choice_loop = 1


while choice_loop == 1:
  choice_select = int(input("\n1: Be able to add administrators\n2. Complete the list of students\n3: Fill in the notes according to subject (Math, French, Physics, Science, Arabic)\n4: Add new students\nPlease enter the number you chose: "))

  if choice_select == 1:
    add_name(admin_username_list)
    print("The admins are: ",admin_username_list)
  elif choice_select == 2:
    if choice_2_lock == 0:
      add_name(student_list)
      print("\nThe students are: ",student_list)
      choice_2_lock = 1
    else:
      print("\nThis choice was already used, please select 4 to add new students")

  elif choice_select == 3:
    choice_3_choice = int(input("\n1: Math\n2: French\n3: Physics\n4:      Science\n5: Arabic\nEnter the number you choose: "))
    if choice_3_choice == 1:
      print("choice 3 small 1")


  elif choice_select == 4:
    print("choice 4")
