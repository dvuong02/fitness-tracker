# define class 'Exercise' taking 4 inputs, and create local variables
class Exercise:
    def __init__(self, name, distance, duration, date):
        self.name = name
        self.distance = float(distance)
        self.duration = int(duration)
        self.date = date
        pass
        
    # define getter methods for local variables
    def get_name(self):
        return self.name
        pass

    def get_distance(self):
        return self.distance
        pass

    def get_duration(self):
        return self.duration
        pass

    def get_date(self):
        return self.date
        pass      

# define user 'Class' taking 1 input, and create local variables
class User:
    def __init__(self, username):
        self.username = username
        self.exercises = []
        pass
        
    # define getter methods for local variables
    def get_username(self):
        return self.username
        pass
    
    def get_exercises(self):
        return self.exercises
        pass    

    # define method to read files
    def read_data(self):
        # attempt to read file
        try:
            file_read = open(f"{self.username}.txt", "r")
        # if file not found error occurs, print error and return false
        except FileNotFoundError:
            print(f"{self.username} has no available data.")
            return False
        # if file exists, split each line into 4 variables and append into
        # empty list self.exercises
        else:
            for line in file_read.readlines():
                fields = line.split(",")
                if len(fields) == 4:
                    name, distance, duration, date = fields
                    exercise = Exercise(name, distance, \
                    duration, date.strip())
                    self.exercises.append(exercise)
            file_read.close()
            return True
        pass
        
    # define method to calculate distance within a time period
    def calculate_distance(self, exercise_name, month):
        total_distance = 0
        # if no month provided, sum distances across all months
        if month is None:
            for exercise in self.exercises:
                if exercise.name == exercise_name:
                    total_distance += exercise.distance
        # if month provided, sum distances across all matching months
        else:
            for exercise in self.exercises:
                if exercise.name == exercise_name and exercise.date == month:
                    total_distance += exercise.distance
        return total_distance
        pass

    # define method to calculate max distance
    def calculate_max_distance(self, exercise_name):
        distances = []
        # create a list of exercises matching the input exercise
        for exercise in self.exercises:
            if exercise.name == exercise_name:
                distances.append(exercise.distance)
        # return max distance from exercise list
        return max(distances)
        pass
    
    # define method to calculate duration within time period
    def calculate_duration(self, exercise_name, month):
        total_duration = 0
        # if month is not provided, sum duration across all months
        if month is None:
            for exercise in self.exercises:
                if exercise.name == exercise_name:
                    total_duration += exercise.duration
        # if month is provided, sum durations across matching months
        else:
            for exercise in self.exercises:
                if exercise.name == exercise_name and exercise.date == month:
                    total_duration += exercise.duration
        return total_duration
        pass
    
    # define method to calculate max duration
    def calculate_max_duration(self, exercise_name):
        durations = []
        # create a list of all durations of exercises matching input exercise
        for exercise in self.exercises:
            if exercise.name == exercise_name:
                durations.append(exercise.duration)
        # return max duration of exercise list
        return max(durations)
        pass 

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

# define function is_valid_date taking a string input 'date'
def is_valid_date(date: str):
    # split variable date into a list using / as separator
    date_split = date.split("/")
    # check that a valid separator is used by checking length of list 
    # date_split
    if len(date_split) != 2:
        print("Please use '/' as a separator")
        return False
        exit()
    # check if month is within range and correctly formatted
    if (int(date_split[0]) >= 1 and int(date_split[0]) <= 12) and \
    len(date_split[0]) == 2:
        # check if year is within range and correctly formatted
        if(int(date_split[1]) >= 2000 and int(date_split[1]) <= 2025) and \
        len(date_split[1]) == 4:
            # return true if all conditions met
            return True
        # if year is outside of range, print error and return false
        elif int(date_split[1]) < 2000 or int(date_split[1]) > 2025:
            print("Please enter a valid year.")
            return False
    # if month is outside of range, print error and return false
    elif int(date_split[0]) < 1 or int(date_split[0]) > 12:
        print("Please enter a valid month.")
        return False
    # if other or no characters are detected, prompt for valid month and 
    # return false
    else:
        print("Please enter a valid month.")
        return False
    pass

# define function log_workout taking a string input 'username'
def log_workout(username: str):
    # prompt user to input exercise
    exercise = input("What exercise would you like to log? ")
    # check input exercise against valid exercises
    exercise_list = ["swim", "run", "cycle"]
    if exercise.lower() not in exercise_list:
        print(f"Sorry, {exercise} is not supported.")
        exit()

    # prompt user to input date of exercise
    date = input(f"What month did you {exercise} (mm/yyyy)? ")
    # check if date is valid
    date_split = date.split("/")
    # check that a valid separator is used
    if len(date_split) != 2:
        print("Please use '/' as a separator")
        exit()
    # if month is outside of range, print error
    elif not(int(date_split[0]) >= 1 and int(date_split[0]) <= 12):
        print("Please enter a valid month.")
        exit()
    # if year is outside of range, print error
    elif not(int(date_split[1]) >= 2000 and int(date_split[1]) <= 2025):
        print("Please enter a valid year.")
        exit()

    # prompt user for distance of exercise
    distance = input(f"What distance did you {exercise} (km or miles)? ")
    # convert distance to kilometres if necessary
    split_distance = distance.split()
    distance = float(split_distance[0])
    if split_distance[1] == "miles":
        distance = distance * 1.6
    distance = round(distance, 1)

    # prompt user for duration of exercise
    duration = input(f"How long did you {exercise} (minutes)? ")

    # create file
    output_info = f"{exercise.lower()},{distance},{duration},{date}"
    file_create = open(f"{username}.txt", "a")
    file_create.write(output_info + "\n")
    pass

# define function track_activity taking input username and create custom
# class-objects
def track_activity(username):
    create_user = User(username)
    exists = create_user.read_data()
    exercise_list = ["swim", "run", "cycle"]
    exercise_log = create_user.get_exercises()
    # if file does not exist, exit function
    if exists == False:
        exit()

    # Check if input exercise is valid
    track_exercise = input("What exercise would you like to track? ")
    if track_exercise.lower() not in exercise_list:
        print(f"Sorry, {track_exercise} is not supported.")
        exit()
    
    # Check if input month is valid
    track_month = input("What month would you like to track (mm/yyyy)? ")
    if track_month != "all":
        # split variable date into a list using / as separator
        date_split = track_month.split("/")
        # check that a valid separator is used by checking length of list 
        # date_split
        if len(date_split) != 2:
            print("Please use '/' as a separator")
            exit()
        # check if month is within range and correctly formatted
        if (int(date_split[0]) >= 1 and int(date_split[0]) <= 12) and \
        len(date_split[0]) == 2:
            # if year is outside of range, print error and exit
            if int(date_split[1]) < 2000 or int(date_split[1]) > 2025:
                print("Please enter a valid year.")
                exit()
        # if month is outside of range, print error and exit
        elif int(date_split[0]) < 1 or int(date_split[0]) > 12:
            print("Please enter a valid month.")
            exit()
        # if other or no characters are detected, prompt for valid month 
        # and exit
        else:
            print("Please enter a valid month.")
            exit()

    # Calculate total and average distance
    total_distance = 0
    count = 0
    for exercise in exercise_log:
        # if track month input is all, sum distances across all months
        if exercise.name == track_exercise.lower() and track_month == "all":
            total_distance += exercise.distance
            count += 1
        # if track month input is specified, sum distances across given month
        elif exercise.name == track_exercise.lower() and exercise.date == \
        track_month:
            total_distance += exercise.distance
            count += 1
    # calculate average distance and print total and average distances
    average_distance = (total_distance / count)
    print(f"Total distance: {total_distance:.1f}km")
    print(f"Average distance: {average_distance:.1f}km")

    # Calculate total and average duration
    total_duration = 0
    count = 0
    for exercise in exercise_log:
        # if track month input is all, sum distances across all months
        if exercise.name == track_exercise.lower() and track_month == "all":
            total_duration += exercise.duration
            count += 1
        # if track month input is specified, sum distances across given month
        elif exercise.name == track_exercise.lower() and exercise.date == \
        track_month:
            total_duration += exercise.duration
            count += 1
    # calculate average duration and print total and average durations
    average_duration = round(total_duration / count)
    print(f"Total duration: {total_duration} mins")
    print(f"Average duration: {average_duration} mins")

    # calculate average speed and print 
    average_speed = round((total_distance / (total_duration / 60)), 5)
    print(f"Average speed (km/h): {average_speed:.2f}km/h")
    pass

# define function plan_health taking one input and create custom class-objects
def plan_health(username):
    create_user = User(username)
    exists = create_user.read_data()
    exercise_log = create_user.get_exercises()
    goal_list = ["marathon run", "marathon swim", "century", \
    "ironman", "5 minute mile"]
    marathon_run_distance = 42
    marathon_swim_distance = 10
    century_distance = 100
    ironman_distance = [4, 180, 42]
    five_mile_speed_mph = 12
    five_mile_speed_kmph = five_mile_speed_mph * 1.6

    # prompt user to input goal and check against goal list
    goal = input("What goal would you like to achieve? ")
    if goal.lower() not in goal_list:
        print("Sorry, that goal is not supported.")
        exit()
    # prompt user to input time frame in weeks to complete goal
    weeks = int(input("How many weeks do you have to achieve it? "))
    
    # initialise lists for exercise distances
    swim_list = []
    run_list = []
    cycle_list = []
    # initialise lists for speed
    speed_list = []

    # if the goal is one of: marathon run, marathon swim or century, calculate
    if goal.lower() == "marathon run" or goal.lower() == "marathon swim" or \
    goal.lower() == "century":

        # for marathon run goal
        if goal.lower() == "marathon run":
            exercise_type = "run"
            # create a list of run distances
            for exercise in exercise_log:
                if exercise.name == exercise_type:
                    run_list.append(exercise.distance)
            # find the max run distance in list
            maximum_distance = max(run_list)
            # calculate weekly increase required to achieve goal
            if maximum_distance >= marathon_run_distance:
                weekly_increase = 0
            else:
                weekly_increase = (marathon_run_distance - maximum_distance) \
                / weeks

        # for marathon swim goal
        elif goal.lower() == "marathon swim":
            exercise_type = "swim"
            # create a list of swim distances
            for exercise in exercise_log:
                if exercise.name == exercise_type:
                    swim_list.append(exercise.distance)
            # find the max swim distance in list
            maximum_distance = max(swim_list)
            # calculate weekly increase required to achieve goal
            if maximum_distance >= marathon_swim_distance:
                weekly_increase = 0
            else:
                weekly_increase = (marathon_swim_distance - maximum_distance)\
                / weeks

        # for century goal
        elif goal.lower() == "century":
            exercise_type = "cycle"
            # create a list of cycle distances
            for exercise in exercise_log:
                if exercise.name == exercise_type:
                    cycle_list.append(exercise.distance)
            # find max cycle distance from list
            maximum_distance = max(cycle_list)
            # calculate weekly increase required to achieve goal
            if maximum_distance >= century_distance:
                weekly_increase = 0
            else:
                weekly_increase = (century_distance - maximum_distance) \
                / weeks
        # finally, print health plan message
        print(f'''To achieve the {goal} challenge you need to:
    Increase your max {exercise_type} by {weekly_increase:.1f}km per week.''')

    # for ironman goal
    elif goal.lower() == "ironman":
        exer_type1 = "swim"
        exer_type2 = "cycle"
        exer_type3 = "run"

        # swim calculations
        # create a list of swim distances
        for exercise in exercise_log:
            if exercise.name == exer_type1:
                swim_list.append(exercise.distance)
        # find max swim distance from list
        maximum_distance = max(swim_list)
        # calculate weekly increase required to achieve goal
        if maximum_distance >= ironman_distance[0]:
            weekly_increase1 = 0
        else:
            weekly_increase1 = (ironman_distance[0] - maximum_distance) \
            / weeks
        
        # cycle calculations
        # create a list of cycle distances
        for exercise in exercise_log:
            if exercise.name == exer_type2:
                cycle_list.append(exercise.distance)
        # find max cycle distance from list
        maximum_distance = max(cycle_list)
        # calculate weekly increase required to achieve goal
        if maximum_distance >= ironman_distance[1]:
            weekly_increase2 = 0
        else:
            weekly_increase2 = (ironman_distance[1] - maximum_distance) \
            / weeks
        
        # run calculations
        # create list of run distances
        for exercise in exercise_log:
            if exercise.name == exer_type3:
                run_list.append(exercise.distance)
        # find max run distance from list
        maximum_distance = max(run_list)
        # calculate weekly increase required to achieve goal
        if maximum_distance >= ironman_distance[2]:
            weekly_increase3 = 0
        else:
            weekly_increase3 = (ironman_distance[2] - maximum_distance) \
            / weeks
        # finally, print health plan message
        print(f'''To achieve the {goal} challenge you need to:
    Increase your max {exer_type1} by {weekly_increase1:.1f}km per week.
    Increase your max {exer_type2} by {weekly_increase2:.1f}km per week.
    Increase your max {exer_type3} by {weekly_increase3:.1f}km per week.''')
    
    # for 5 minute mile goal
    elif goal.lower() == "5 minute mile":
        exercise_type = "run"
        # calculate run distance and duration to create list of speed
        for exercise in exercise_log:
            if exercise.name == exercise_type:
                run_distance = exercise.distance
                run_duration = exercise.duration
                speed_list.append((run_distance/run_duration)*60)
        # find max speed from list
        maximum_speed = max(speed_list)
        # calculate weekly increase required to achieve goal
        if maximum_speed >= five_mile_speed_kmph:
            weekly_increase = 0
        else:
            weekly_increase = (five_mile_speed_kmph - maximum_speed) \
            / weeks
        # finally print health plan message
        print(f'''To achieve the {goal} challenge you need to:
    Increase your max speed by {weekly_increase:.2f}km/h per week.''')
    pass

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