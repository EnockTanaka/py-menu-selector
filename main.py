# This is a program which presents the user with a menu to select one of two options. The program stops after the selected option has finished executing.

# Option A: Ask the user to input the amount remaining battery level for an electric car.

#Option B: Ask the user to enter the mark they received for the Semester Test and the total possible marksfor the Semester Test. Calculate the mark percentage (%). If the mark is less than 50%, output “You need to invest more time in your schoolwork.” Else, output “Keep it up.”
def option_A():

  battery_level = float(input("What is your current battery level:  "))
  
  if battery_level in range( 0 , 16 ):
    print('Charging required! You may get stuck on the road.')
    
  elif battery_level in range(15 , 36):
    print('Barely enough power remaining. Use the shortest route.')
    
  elif battery_level in range(35 , 76):
    print('There should be enough battery power to last you the entire trip.')
    
  elif battery_level in range(75 , 101):
    print('The battery is sufficiently charged. Happy driving!')

def option_B():
  
    mark = float(input("Enter your mark for the semester test: "))
    total_marks = float(input("Enter the total possible marks for the semester test: "))

    percentage = (mark / total_marks) * 100

    if percentage < 50:
        print(f"You need to invest more time in your schoolwork.You have {percentage}%")
    else:
        print(f"Keep it up.You have {percentage}%")
      
def main():
  
    while True:
        print("Select an option:\n")
        print("1. Option A")
        print("2. Option B\n")
        choice = int(input("Enter your choice (1 or 2): "))

      
        if choice == 1:
            option_A()            
            break
          
        elif choice == 2:
            option_B()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")
main()