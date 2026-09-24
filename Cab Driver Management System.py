import json

art1 = """----------- ADD DRIVER -----------"""
art2 = """----------- ALL DRIVERS -----------"""
art3 = """----------- SEARCH DRIVER -----------"""
art4 = """----------- UPDATE AVAILABILITY -----------"""
art5 = """----------- SEARCH BY RATING -----------"""
art6 = """----------- DELETE DRIVER -----------"""
art7 = """----------- AVAILABLE DRIVERS -----------"""

class Driver:
    def __init__(self):
        self.driver_id = []
        self.driver_name = []
        self.mobile_no = []
        self.cab_no = []
        self.cab_type = []
        self.driver_experience = []
        self.rating = []
        self.driver_availability = []
        self.load_data()

    def add_driver(self):
        print(f"\n{art1}\n")

        driver_id = input("Enter Driver ID: ")
        self.driver_id.append(driver_id)
        driver_name = input("Enter Driver Name: ")
        self.driver_name.append(driver_name)
        mobile_no = int(input("Enter Mobile Number: "))
        self.mobile_no.append(mobile_no)
        cab_no = input("Enter Cab Number: ")
        self.cab_no.append(cab_no)
        cab_type = input("Enter Cab Type: ")
        self.cab_type.append(cab_type)
        driver_experience = int(input("Enter Driver Experience: "))
        self.driver_experience.append(driver_experience)
        rating = float(input("Enter Driver Rating: "))
        self.rating.append(rating)
        driver_availability = input("Enter Availability (Yes/No): ")
        self.driver_availability.append(driver_availability)
        self.save_data()
        print("\nDriver data saved successfully\n")

    def save_data(self):
        driver_data = []

        for i in range(len(self.driver_id)):
            driver = {
                "driver_id": self.driver_id[i],
                "driver_name": self.driver_name[i],
                "mobile_number": self.mobile_no[i],
                "cab_number": self.cab_no[i],
                "cab_type": self.cab_type[i],
                "experience": self.driver_experience[i],
                "rating": self.rating[i],
                "availability": self.driver_availability[i]
            }
            driver_data.append(driver)

        with open("Driver Data.json", "w") as file:
            json.dump(driver_data, file, indent=4)

    def load_data(self):
        try:
            with open("Driver Data.json", "r") as file:
                data = json.load(file)
            for driver in data:
                self.driver_id.append(driver["driver_id"])
                self.driver_name.append(driver["driver_name"])
                self.mobile_no.append(driver["mobile_number"])
                self.cab_no.append(driver["cab_number"])
                self.cab_type.append(driver["cab_type"])
                self.driver_experience.append(driver["experience"])
                self.rating.append(driver["rating"])
                self.driver_availability.append(driver["availability"])
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def show_data(self):
        print(f"\n{art2}\n")

        for i in range(len(self.driver_id)):
            print(f"Driver ID       : {self.driver_id[i]}\n"
                  f"Driver Name     : {self.driver_name[i]}\n"
                  f"Mobile Number   : {self.mobile_no[i]}\n"
                  f"Cab Number      : {self.cab_no[i]}\n"
                  f"Cab Type        : {self.cab_type[i]}\n"
                  f"Experience      : {self.driver_experience[i]}\n"
                  f"Rating          : {self.rating[i]}\n"
                  f"Availability    : {self.driver_availability[i]}\n")
            print("----------------------------------------------------------\n")

    def search_driver(self):
        print(f"\n{art3}\n")

        search_id = input("Enter Driver ID: ")
        for i in range(len(self.driver_id)):
            if self.driver_id[i] == search_id:
                print(f"Driver ID       : {self.driver_id[i]}\n"
                      f"Driver Name     : {self.driver_name[i]}\n"
                      f"Mobile Number   : {self.mobile_no[i]}\n"
                      f"Cab Number      : {self.cab_no[i]}\n"
                      f"Cab Type        : {self.cab_type[i]}\n"
                      f"Experience      : {self.driver_experience[i]}\n"
                      f"Rating          : {self.rating[i]}\n"
                      f"Availability    : {self.driver_availability[i]}")
                break
        else:
            print("\nDriver not found\n")

    def update_availability(self):
        print(f"\n{art4}\n")

        update = input("Enter Driver ID: ")
        for i in range(len(self.driver_id)):
            if self.driver_id[i] == update:
                driver_availability = input("Enter Availability (Yes/No): ")
                self.driver_availability[i] = driver_availability
                self.save_data()
                print("\nDriver availability updated successfully!\n")
                break
        else:
            print("\nDriver not found\n")

    def search_by_rating(self):
        print(f"\n{art5}\n")
        
        rating = float(input("Enter minimum rating: "))
        for i in range(len(self.driver_id)):
            if self.rating[i] > rating:
                print(f"Driver ID       : {self.driver_id[i]}\n"
                      f"Driver Name     : {self.driver_name[i]}\n"
                      f"Mobile Number   : {self.mobile_no[i]}\n"
                      f"Rating          : {self.rating[i]}\n"
                      f"Availability    : {self.driver_availability[i]}")
                print("----------------------------------------------------------\n")

    def delete_driver(self):
        print(f"\n{art6}\n")
        
        delete_id = input("Enter Driver ID: ")
        for i in range(len(self.driver_id)):
            if self.driver_id[i] == delete_id:
                print("\nDriver found:")

                confirmation = input("Are you sure you want to delete this driver? (Yes/No): ").lower()
                if confirmation.lower() == "yes":

                    del self.driver_id[i]
                    del self.driver_name[i]
                    del self.mobile_no[i]
                    del self.cab_no[i]
                    del self.cab_type[i]
                    del self.driver_experience[i]
                    del self.rating[i]
                    del self.driver_availability[i]

                    self.save_data()
                    print("\nDriver deleted successfully!\n")
                else:
                    print("\nDeletion cancelled.\n")
                break
        else:
            print("\nDriver ID not found.\n")

    def available_drivers(self):
        print(f"\n{art7}\n")
        found = False

        for i in range(len(self.driver_id)):
            if self.driver_availability[i] == 'Yes':
                print(f"Driver ID       : {self.driver_id[i]}\n"
                      f"Driver Name     : {self.driver_name[i]}\n"
                      f"Mobile Number   : {self.mobile_no[i]}\n"
                      f"Cab Number      : {self.cab_no[i]}\n"
                      f"Cab Type        : {self.cab_type[i]}\n"
                      f"Rating          : {self.rating[i]}\n"
                      f"Availability    : {self.driver_availability[i]}")
                print("----------------------------------------------------------\n")

                found = True
        if not found:
            print("No driver available\n")


menu = """========================================
       CAB DRIVER MANAGEMENT SYSTEM
========================================

1. Add Driver
2. Display All Drivers
3. Search Driver by ID
4. Update Driver Availability
5. Search Drivers by Rating
6. Delete Driver
7. Display Available Drivers
8. Exit"""
continue_program = True
driver = Driver()
while continue_program:

    print(menu)

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        driver.add_driver()
    elif choice == "2":
        driver.show_data()
    elif choice == "3":
        driver.search_driver()
    elif choice == "4":
        driver.update_availability()
    elif choice == "5":
        driver.search_by_rating()
    elif choice == "6":
        driver.delete_driver()
    elif choice == "7":
        driver.available_drivers()
    elif choice == "8":
        print("\nProgram Terminated\n")
        continue_program = False
    else:
        print("\nInvalid choice. Please try again\n")