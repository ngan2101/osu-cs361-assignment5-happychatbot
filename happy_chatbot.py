import random


def job_matching():
    while True:
        experience = input("\nTell me about your experience: ")
        if any(word in experience.lower() for word in ["radiology", "x-ray", "rad tech", "radiology technologist"]):
            print("Based on your experience, we recommend you to apply for the Radiology Technologist (full-time, day shift) position.")
            choice = input("Enter 'back' to return to the home page, 'continue' to start over, or 'quit' to end the session: ")
            if choice.lower() == 'back':
                return
            elif choice.lower() == 'continue':
                continue
            elif choice.lower() == 'quit':
                print("Thank you for using our service. Have a great day!")
                exit()
            else:
                print("Invalid input. Please try again.")
        elif any(word in experience.lower() for word in ["pharm", "pharmacy", "pharm tech", "pharmacy technician", "pharmacist"]):
            print("Based on your experience, we recommend you to apply for the Pharmacist 1 (full-time, day shift) position.")
            choice = input("Enter 'back' to return to the home page, 'continue' to start over, or 'quit' to end the session: ")
            if choice.lower() == 'back':
                return
            elif choice.lower() == 'continue':
                continue
            elif choice.lower() == 'quit':
                print("Thank you for using our service. Have a great day!")
                exit()
            else:
                print("Invalid input. Please try again.")
        elif any(word in experience.lower() for word in ["program coordinator", "project coordinator", "supply chain"]):
            print("Based on your experience, we recommend you to apply for the Implant Coordinator (full-time, night shift) position.")
            choice = input("Enter 'back' to return to the home page, 'continue' to start over, or 'quit' to end the session: ")
            if choice.lower() == 'back':
                return
            elif choice.lower() == 'continue':
                continue
            elif choice.lower() == 'quit':
                print("Thank you for using our service. Have a great day!")
                exit()
            else:
                print("Invalid input. Please try again.")
        else:
            print("Sorry, we couldn't find a suitable position based on your experience.")
            choice = input("Enter 'back' to return to the home page, 'continue' to start over, or 'quit' to end the session: ")
            if choice.lower() == 'back':
                return
            elif choice.lower() == 'quit':
                print("Thank you for using our service. Have a great day!")
                exit()
            elif choice.lower() != 'continue':
                print("Invalid input. Please try again.")


def application_status():
    while True:
        req_number = input("\nPlease enter the requisition number: ")
        if req_number.isdigit() and len(req_number) == 5:
            status = random.choice(['"In review by HR"', '"Resume sent to Hiring Manager"', '"Position cancelled"'])
            print(f"Application status for REQ# {req_number}: {status}")
            choice = input("Enter 'back' to return to the home page, 'continue' to start over, or 'quit' to end the session: ")
            if choice.lower() == 'back':
                return
            elif choice.lower() == 'continue':
                continue
            elif choice.lower() == 'quit':
                print("Thank you for using our service. Have a great day!")
                exit()
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please try again with a 5-digit number.")


def position_information():
    while True:
        req_number = input("\nPlease enter the requisition number: ")
        if req_number.isdigit() and len(req_number) == 5:
            while True:
                choice = input('What would you like to know about this position?\n'
                               'Enter "1" for PTO\n'
                               'Enter "2" for healthcare benefits\n'
                               'Enter "3" for career development \n'
                               'Enter "4" for eligible bonuses\n'
                               'Enter "5" for other benefits: ')
                if choice == '1':
                    print("This position is eligible for vacation time and sick time off that accrues monthly, including 12 paid holidays and 1 personal float.")
                    choice = input("Enter 'back' to return to the home page, 'continue' to explore more, or 'quit' to end the session: ")
                    if choice.lower() == 'back':
                        return
                    elif choice.lower() == 'continue':
                        continue
                    elif choice.lower() == 'quit':
                        print("Thank you for using our service. Have a great day!")
                        exit()
                    else:
                        print("Invalid input. Please try again.")
                elif choice == '2':
                    print("This position is eligible for excellent healthcare, dental, disability, and retirement plan options")
                    choice = input("Enter 'back' to return to the home page, 'continue' to explore more, or 'quit' to end the session: ")
                    if choice.lower() == 'back':
                        return
                    elif choice.lower() == 'continue':
                        continue
                    elif choice.lower() == 'quit':
                        print("Thank you for using our service. Have a great day!")
                        exit()
                    else:
                        print("Invalid input. Please try again.")
                elif choice == '3':
                    print("This position is eligible for State Employee Tuition Exemption Program covering up to 6 credits of qualifying coursework per quarter.")
                    choice = input("Enter 'back' to return to the home page, 'continue' to explore more, or 'quit' to end the session: ")
                    if choice.lower() == 'back':
                        return
                    elif choice.lower() == 'continue':
                        continue
                    elif choice.lower() == 'quit':
                        print("Thank you for using our service. Have a great day!")
                        exit()
                    else:
                        print("Invalid input. Please try again.")
                elif choice == '4':
                    print("This position is eligible for $5,000 sign-on bonus with two years of commitment, and relocation bonus up to $10,000 if applicable.")
                    choice = input("Enter 'back' to return to the home page, 'continue' to explore more, or 'quit' to end the session: ")
                    if choice.lower() == 'back':
                        return
                    elif choice.lower() == 'continue':
                        continue
                    elif choice.lower() == 'quit':
                        print("Thank you for using our service. Have a great day!")
                        exit()
                    else:
                        print("Invalid input. Please try again.")
                elif choice == '5':
                    print("This position is eligible for:\n"
                          "• Fully subsidized public transit pass that covers multiple forms of public transportation in the region\n"
                          "• Lots of free fitness, healthy eating, finance, and stress reduction classes offered internally\n"
                          "• Public Service Loan Forgiveness Program\n")
                    choice = input("Enter 'back' to return to the home page, 'continue' to explore more, or 'quit' to end the session: ")
                    if choice.lower() == 'back':
                        return
                    elif choice.lower() == 'continue':
                        continue
                    elif choice.lower() == 'quit':
                        print("Thank you for using our service. Have a great day!")
                        exit()
                    else:
                        print("Invalid input. Please try again.")
                else:
                    print("Invalid input. Please enter a number between 1 and 5.")
        else:
            print("Invalid input. Please try again with a 5-digit number.")

def help_message():
    print("If you have any other questions that Happy can't assist you with, please feel free to email us at "
          "hrservice@talenthub.com or give us a call at 321-123-3214 during our office hours, Monday to Friday, "
          "8:00 am to 5:00 pm PT. Thank you!")
    while True:
        choice = input("Enter 'back' to return to the home page or 'quit' to end the session: ")
        if choice.lower() == 'back':
            return
        elif choice.lower() == 'quit':
            print("Thank you for using our service. Have a great day!")
            exit()
        else:
            print("Invalid input. Please try again.")

def privacy_notice():
    print("We value your privacy. Your conversations with Chatbot Happy are not recorded, saved,"
          " or used for any purpose other than improving your experience.\n"
          "Your privacy is important to us, and we will never sell your conversation data or spam you.\n"
          "Your interactions with Chatbot Happy are confidential and solely for the purpose of providing you with assistance. "
          "If you have any concerns, please feel free to reach out to us at any time.")
    while True:
        choice = input("Enter 'back' to return to the home page or 'quit' to end the session: ")
        if choice.lower() == 'back':
            return
        elif choice.lower() == 'quit':
            print("Thank you for using our service. Have a great day!")
            exit()
        else:
            print("Invalid input. Please try again.")


def main():
    print("Hello, welcome to our 24/7 online chat support. My name is Happy, it's my pleasure to assist you today!")

    while True:
        choice = input('\nBefore we get started, you can input "help" to get further assistance, or "privacy" to read more about our privacy notice.\n' 
                       'Enter "1" for job matching recommendations\n'
                       'Enter "2" for application status check\n'
                       'Enter "3" for position information inquiry: ')
        if choice == 'help':
            help_message()
        elif choice == 'privacy':
            privacy_notice()
        elif choice == '1':
            job_matching()
        elif choice == '2':
            application_status()
        elif choice == '3':
            position_information()
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
