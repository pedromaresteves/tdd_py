import random

def generate_4_digit_num():
    secret_num_list = []
    for i in range(4):
        new_digit = random.randint(1, 9)
        while new_digit in secret_num_list:
           new_digit = random.randint(1, 9) 
        secret_num_list.append(new_digit)
    return secret_num_list

def check_if_input_is_valid_and_return_numberized(user_input):
    user_input_numberized = []
    if(user_input == "exit"): return False
    user_input = list(user_input)
    if(len(user_input) != 4):
        print("You have to insert a 4 digit number. Try Again")
        return False
    for x in user_input:
        if(user_input.count(x) > 1):
            print("You can't insert the same digit twice!")
            return False
        try:
            x_numberized = int(x)
            user_input_numberized.append(x_numberized)
        except:
            print("You can only insert digits!")
            return False
    return user_input_numberized

def count_cows_bulls(user_input, secret_num):
    cows_and_bulls = {
        "cows" : 0,
        "bulls" : 0
    }
    for x in user_input:
        x_index = user_input.index(x)
        if(user_input[x_index] == secret_num[x_index]):
            cows_and_bulls["bulls"] += 1
        elif(secret_num.count(user_input[x_index])):
            cows_and_bulls["cows"] += 1
    return cows_and_bulls

def guess_number(num_of_tries):
    user_input = input("Insert a 4 digit number: ")
    checked_user_input = check_if_input_is_valid_and_return_numberized(user_input)
    if(checked_user_input):
        cs_and_bs = count_cows_bulls(checked_user_input, secret_num)
        if(cs_and_bs["bulls"] == 4):
            if(num_of_tries == 1):
                print(f"You win sucka! You took {num_of_tries} try.")
            else:
                print(f"You win sucka! You took {num_of_tries} tries")
            return True
        else:
            num_of_tries += 1
            cows = cs_and_bs["cows"]
            bulls = cs_and_bs["bulls"]
            print(f"You got {cows} cow(s) and {bulls} bull(s). Do it again you can do it!")
            guess_number(num_of_tries)
    else:
        guess_number(num_of_tries)

secret_num = generate_4_digit_num()   
guess_number(1)