# define welcome screen function
def welcome_screen():
    # define recurring horizontal border
    horizontal_border = "*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    # construct welcome screen, formatting using horizontal border
    welcome_screen = f'''{horizontal_border}
| WELCOME TO USYD FITNESS |
{horizontal_border}
*    LOGS YOUR WORKOUT    *
*   TRACKS YOUR FITNESS   *
*    GET FIT & HEALTHY    *
{horizontal_border}'''
    # print welcome screen
    print(welcome_screen)
    pass

# define login function
def login():
    # prompt user for username
    username = input("Login with your username: ")
    # if username is over the limit, print message and exit code
    if len(username) > 20:
        print("Your username is too long.")
        return None

    # define recurring horizontal border
    horizontal_border = "~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    # construct login screen using horizontal border
    login_screen = f'''{horizontal_border}
| Hi {username:20} |
{horizontal_border}
| [1] Log an activity     |
| [2] Track your fitness  |
| [3] Plan your health    |
{horizontal_border}'''
    # print login screen
    print(login_screen)
    return username
    pass
