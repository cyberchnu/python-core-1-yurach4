def mean(number):
    num_str = str(number)
    digit_sum = 0
    for digit_char in num_str:
        digit_sum += (
            int(digit_char))
    mean_value = (digit_sum /
                  len(num_str))
    return mean_value