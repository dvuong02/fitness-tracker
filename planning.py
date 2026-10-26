from models import User

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
