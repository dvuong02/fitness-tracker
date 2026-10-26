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
