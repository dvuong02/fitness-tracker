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
