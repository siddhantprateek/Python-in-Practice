import os


class user_login:

    def user_login(self, user_name, user_password):

        if self.user_name == "Siddhant@gmail.com" and self.user_password == "Alpha":
            welcome()
            input()
            self.clear()
            self.user_dashboard()
        elif self.user_name != "Siddhant@gmail.com" and self.user_password != "Alpha":
            print("\nInvalid Username and password")
            response = input(
                "\nPress r to Retry \nPress f for Forgot Password \n>")

            if response.lower() == "r":
                self.clear()
                self.login()

            elif response.lower() == "f":
                print("Redirecting")
                self.clear()
                self.forgot_password()

            else:
                print("Invalid response")
                input()
                self.login()
        else:
            print("Reload")

    # MAIN LOGIN WINDOW

    def forgot_password():

        Email = input("Please Enter your Email:")

        if "@" and "." in Email:
            print("\nPlease check your Email to Change your password.")
            input("Press Enter to Redirect to login Window.")
            login()

        else:
            print("Please enter your valid Email Id")
            forgot_password()

    def login(self):
        clear()

        response = input(
            "Press (L) to Login       Press (C) to Create Account\n>")

        if response.lower() == 'l':
            clear()
            username = input("Username: ")
            password = input("password: ")

            input("Press Enter to Login")
            clear()
            user_login(username, password)

        elif response.lower() == "c":
            self.user_sign_up()

        else:
            print("Invalid Response.")
            input("Press Any Key to redirect too the the Homepage")
            login()

    # There should not be any symbolic character in the Names

    # Create Account For User

    def user_sign_up():

        clear()
        f_name = input("First Name: ")
        s_name = input("Surname: ")
        u_email = input("Email: ")
        u_phone = int(input("Mobile Number:"))
        Dob = int(input("Enter Date of Birth: "))
        u_gender = input("Gender: ")

        user_info = f"First name: {f_name} \nsurname: {s_name}\nEmail:{u_email}\nMobile Number:{u_phone}\nDate of Birth: {Dob}\ngender: {u_gender}"

        if "@" and "." in u_email:
            clear()
            print("User is Registered.")
            # user data been saved in a text file
            user_data = open(f"{f_name}.txt", "w")
            user_data.write(user_info)
            user_data.close()
            input()
            user_dashboard()

        else:
            print("Enter Valid Email ID.")

    def user_dashboard():

        print("(H)Home      (L)Logout       (S)Settings    (F)Chat\n")
        response = input(">")

        if response.lower() == "l":
            print("See You Soon...")
            input()
            login()
        elif response.lower() == "s":
            print("under process")
        else:
            clear()
            user_dashboard()

    # Settings

    def user_settings():
        clear()

        input("1. Account \n 2. Personalize your profile\n 3. Security\n4. Notification  ")

    def account():
        print("\nEdit email \nedit number \nedit ")

    def personalize():
        input("Change Theme \nChange Page layout \nchange Background \n>>")

    def welcome():
        for numbers in reversed(range(10)):
            print(" * "*numbers)

        print("                 Welcome to Wangrove")

        for numbers in range(10):
            print(" * "*numbers)

    # Starts
    #


user = user_login()
user.login()
