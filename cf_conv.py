user_choice = 0
user_choice2 = 0
ct = 0
ft = 0
def main():
    print("Hello! This is my Celsius to Fahrenheit converter!")
    print("Which operation do you want to do?")
    user_choice = input("Press 1 to do Celsius to Fahrenheit or Press 2 to do Fahrenheit to Celsius, another number will close this program: ")
    if user_choice == "1":
        ct = input("Insert Celsius Temperature: ")
        ft = float(ct) * 1.8 + 32
        print("The result is " + str(ft))
        user_choice2 = input("Wanna try again?")
        if user_choice2 == "Yes" or user_choice2 == "yes":
            main()
        else: return 0    
    elif user_choice == "2":
        ft = input("Insert Fahrenheit Temperature: ")
        ct = (float(ft) - 32) % 1.8
        print("The result is " + str(ct))
        user_choice2 = input("Wanna try again?")
        if user_choice2 == "Yes" or user_choice2 == "yes":
            main()
        else: return 0    
main()   
