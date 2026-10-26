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
