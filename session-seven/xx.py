def input_validation(lower, upper, prompt):
    ''' Validates the user input....
        lower = lower bound of acceptable values (int)
        ...
        returns the ....
    '''
    valid = False
    while not valid:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid value")
        else:
            valid = lower <= value and value <= upper
    return value

def options(lower, upper, prompt):
    ''' Given a set of values the user selects from those values and the
        resulting "constants" are returned as a tuple.
    '''
    # internally use a dictionary (map) to store the values for the variables
    dict = {1:(10,30,45,56), 2:(12,50,45,78), 3: (15,30,67,89)}
    value = input_validation(lower, upper, prompt)
    # we can be sure that the returned value is within range so just
    # return the values associated with the key.
    return dict[value]

def main():
    (dollars,cents,pounds,pence) = options(1,3,"Enter a value between 1 and 3 inclusive: ")
    print(dollars,cents)

if __name__ == "__main__":
    main()
