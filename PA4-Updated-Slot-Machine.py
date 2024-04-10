# Michael Carr
# Programing Assignment 4
# MIS 301
# 04-06-2024

# Diagonal check in matrix
def check_diagonal(matrix):
    if matrix[0][0]==matrix[1][1]==matrix[2][2]:
        return True
    else:
        return False
# Off diagonal check in matrix
def check_off_diagonal(matrix):
    if matrix[2][0]==matrix[1][1]==matrix[0][2]:
        return True
    else:
        return False
# Checks vertical match in matrix 
def check_vert(matrix, col):
    if matrix[0][col]==matrix[1][col]==matrix[2][col]:
        return True
    else:
        return False
#   checks horizontal match in matrix
def check_hori(matrix, row):
    if matrix[row][0]==matrix[row][1]==matrix[row][2]:
        return True
    else:
        return False
# Starts the slots
def main():
# Getting starting coins and checking value
    int_is_valid = False
    while not int_is_valid:
        try:
            coins = input("how many tokens are you starting with? ")
            coins = int(coins)
            int_is_valid = coins > 0
        except ValueError:
            print("Please input an integer greater than 0!")
    # Reads the file into a list
    file = open("played_slots.txt").read().split()
    # Initialize the index and starts the loop
    for file_i in range(0,len(file),9):
        # Create next matrix for that spin
        matrix = [[0]*3]*3
        #save numbers to matrix
        for i in range(0,3):
            # reset line list
            line = [0]*3
            for j in range(0,3):
                # gets character
                c = file[file_i + (3 * i) + j]
                # saves the character
                line[j] = c
            #saves into the line
            matrix [i] = line
        # Uses a coin per spin
        coins -= 1 
        # print top of grid
        print(" _=========_")
        print("|#|~-~-~-~|#|")
        #prints matrix
        for i in range(0,3):
            print("| | |", end="")
            for j in range(0,3):
                print(matrix[i][j],end="")
            print("| | |")
        # print bottom of grid
        print("|#|~-~-~-~|#|")
        print("=============")
        # check if there is a Jackpot
        if check_diagonal(matrix) == True:
            print("JACKPOT!!")
            coins += 10
        if check_off_diagonal(matrix) == True:
            print("JACKPOT!!")
            coins += 10
        for i in range(0,3):
            if check_vert(matrix, i) == True:
                print("JACKPOT!!")
                coins += 10
            if check_hori(matrix, i) == True:
                print("JACKPOT!!")
                coins += 10
        print("You have " + str(coins) + " tokens left!")
        # Winning condition
        if coins >= 122:
            print("The house has gone bust! You left with " + str(coins) + " tokens!")
            quit()
        # Spin slots until user decides to quit 
        user_input = input("Press carriage return to spin the slots, or type any other character to quit!")
        if coins < 1:
            print("Sorry, you are out of coins")
            quit()
        if user_input != "":
            print("You left with " + str(coins) + " tokens!")
            quit()
# Starts the program
main()
