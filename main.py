from screens import welcome_screen, login
from workout_log import log_workout
from tracking import track_activity
from planning import plan_health

# define main function calling all other defined functions
def main():
    #print the welcome screen
    welcome_screen()
    #Ask the user to login with a username
    username = login()
    #If the username is too long, keep asking to login
    while username == None:
        username = login()
    #Ask the user to choose an option (1, 2 or 3)
    option = input("Choose an option: ")
    #If they choose option 1, log an activity!
    if option == "1":
        log_workout(username)
    #If they choose option 2, track their fitness!
    elif option == "2":
        track_activity(username)
    #If they choose option 3, plan their health!
    elif option == "3":
        plan_health(username)
    return

# call main function
if __name__ == '__main__':
    main()
