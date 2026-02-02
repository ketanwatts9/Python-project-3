def welcome():
    print(83*'-','CHITKARA UNIVERSITY HELP COUNTER',84*'-')
    print("WELCOME TO CHITKARA UNIVERSITY, RAJPURA")

def ask_details():
    name = input("Enter your name: ").lower()
    age = int(input("Enter your age: "))
    contact = int(input("Enter your contact: "))
    return name

def show_content(name):
    print(f"{name}, How can i help you?")
    print("1. want to know about courses offered by Chitkara University.")
    print("2. want to know about fees structure of courses.")
    print("3. want to know about facilities provided.")
    print("4. want to know about hostel details.")
    print("5. want to know about placement details.")
    print("6. want to know about admission cell details.")

def courses_details():
    print("courses offered are:")
    print("- BE computer science")
    print("- BE computer science in AI-ML")
    print("- BE mechanics")
    print("- BE chemical")
    print("- BBA")
    print("- BCA")

def fees_details():
    print("fees structure is as given:")
    print("1,50,000 per sem")
    print("20,000 as other expenses (only one time pay)")
    print("10,000 as security (only one time pay)")

def facilities_details():
    print("world class infrasturcture is provided by us")
    print("international exposure")
    print("new classrooms and experienced teachers")

def hostel_details():
    print("new built rooms and furniture")
    print("24/7 hot and cold water facilities")
    print("both ac and non ac rooms are available")

def placement_details():
    print("95% placement gurantteed")
    print("highest package: 50 lpa")
    print("average package: 10 lpa")

def admission_cell_details():
    print("contact number: 98558-96020")
    print("EMAIL: chitakara.edu.in")
    print("website: www.chitkara.edu.in")

def thankyou(name):
    print(f"Thankyou {name}! see you again")

def main():
    welcome()
    print(201*"-")

    name = ask_details()
    print(201*"-")

    show_content(name)
    print(201*"-")

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("entered wrong input") 
            continue

        if choice == 1:
            courses_details()
        elif choice == 2:
            fees_details()
        elif choice == 3:
            facilities_details()
        elif choice == 4:
            hostel_details()
        elif choice == 5:
            placement_details()
        elif choice == 6:
            admission_cell_details()
        else:
            print("you have entered wrong choice.")
            continue
        print(201*"-")
        
        continu = input("Do you want more imformation (yes/no): ")
        if continu != 'yes':
            thankyou(name)
            print(201*"-")
            break
        
main()