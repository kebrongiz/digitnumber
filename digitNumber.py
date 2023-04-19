def get_digit_nums():
    curr_input = 1
    while curr_input > 0:
        curr_input = input("Enter a number: ")
        curr_input = curr_input.replace(',', '')
        if (int(curr_input) < 0):
            break
        print("The number of digits in {} is {}".format(
            curr_input, len(curr_input)))
        curr_input = int(curr_input)


get_digit_nums()
