from models import User

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
