import random
import sys

correct_answer_txt = "You did a good job!"
incorrect_answer_too_high_txt = "You're too high"
incorrect_answer_too_low_txt = "You're too low!"
exit_msg = "Bye"


def check_number(num, rand_num, num_tries):
    feedback = {}
    if (num == rand_num):
        feedback["result"] = True
        feedback["message"] = correct_answer_txt
    else:
        if (num > rand_num):
            feedback["message"] = incorrect_answer_too_high_txt
        if (num < rand_num):
            feedback["message"] = incorrect_answer_too_low_txt
        feedback["result"] = False
    return feedback


def convert_user_input(user_input):
    if(user_input == "exit"):
        sys.exit(exit_msg)
    try:
        return int(user_input)
    except:
        return False


random_number = random.randint(1, 50)


def guess_number(rand_num):
    number_of_tries = 0
    print('A random number from 1 to 50 as been generated. You have 5 tries to find it out. (Type "exit" to leave the program.)')
    while number_of_tries < 5:
        user_input = input("Insert number: ")
        converted_user_input = convert_user_input(user_input)
        if(converted_user_input):
            get_feedback = check_number(
                converted_user_input, rand_num, number_of_tries)
            print(get_feedback["message"])
            if (get_feedback["result"]):
                break
            number_of_tries += 1
            if (number_of_tries == 5):
                print("You failed")
                return False
        else:
            print('That\'s not a valid input value. You should type an integer. (Type "exit" to leave the program.)')

# guess_number(random_number)
