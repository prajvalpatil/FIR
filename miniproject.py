class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class FIR:
    def __init__(self, fir_id, victim_name, description, date):
        self.fir_id = fir_id
        self.victim_name = victim_name
        self.description = description
        self.date = date


class FIRManagementSystem:
    def __init__(self):
        self.users = []
        self.firs = []
        self.current_user = None

    def create_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = User(username, password)
        self.users.append(user)
        print("\nUser created successfully........!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print("\nLogin successful.")
                return
        print("Invalid username or password.")

    def create_fir(self):
        if not self.current_user:
            print("Please login first.")
            return
        fir_id = input("Enter FIR ID: ")
        victim_name = input("Enter Victim's Name: ")
        description = input("Enter Description of the Crime: ")
        date = input("Enter Date (YYYY-MM-DD): ")
        fir = FIR(fir_id, victim_name, description, date)
        self.firs.append(fir)
        print("FIR created successfully.")

    def display_firs(self):
        if not self.current_user:
            print("Please login first.")
            return
        if self.firs:
            print("FIRs in the System:")
            for fir in self.firs:
                print(f"FIR ID: {fir.fir_id}")
                print(f"Victim's Name: {fir.victim_name}")
                print(f"Description: {fir.description}")
                print(f"Date: {fir.date}")
                print("-----------------------------------------------------------")
        else:
            print("\nNo FIRs in the system................!")

    def search_firs(self):
        if not self.current_user:
            print("\nPlease login first...................!")
            return
        search_term = input("Enter search term: ")
        results = []
        for fir in self.firs:
            if search_term in fir.fir_id or search_term in fir.description:
                results.append(fir)
        if results:
            print("Search Results:")
            for result in results:
                print(f"FIR ID: {result.fir_id}")
                print(f"Victim's Name: {result.victim_name}")
                print(f"Description: {result.description}")
                print(f"Date: {result.date}")
                print("--------------------")
        else:
            print("\nNo matching FIRs found.")

    def update_fir(self):
        if not self.current_user:
            print("Please login first..............!")
            return
        fir_id = input("Enter FIR ID to update: ")
        
        for fir in self.firs:
            if fir.fir_id == fir_id:
                print("Current FIR Details:")
                print(f"FIR ID: {fir.fir_id}")
                print(f"Victim's Name: {fir.victim_name}")
                print(f"Description: {fir.description}")
                print(f"Date: {fir.date}")
                print("--------------------")

                new_description = input("Enter new description: ")
                new_date = input("Enter new date (YYYY-MM-DD): ")

                fir.description = new_description
                fir.date = new_date

                print("FIR updated successfully.")
                return
        print("FIR not found.")

    def logout(self):
        self.current_user = None
        print("Logged out successfully.")


# Usage example
fir_system = FIRManagementSystem()

while True:
    print("FIR Management System")
    print("1. Create User")
    print("2. Login")
    print("3. Create FIR")
    print("4. Display FIRs")
    print("5. Search FIRs")
    print("6. Update FIR")
    print("7. Logout")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        fir_system.create_user()
    elif choice == "2":
        fir_system.login()
    elif choice == "3":
        fir_system.create_fir()
    elif choice == "4":
        fir_system.display_firs()
    elif choice == "5":
        fir_system.search_firs()
    elif choice == "6":
        fir_system.update_fir()
    elif choice == "7":
        fir_system.logout()
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")
