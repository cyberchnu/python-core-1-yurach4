def int_within_bounds(number, lower_bound, upper_bound):
    if type(number) != int:
      return False
    elif number >= lower_bound and number< upper_bound:
      return True
    else:
      return False



print(int_within_bounds(5,5,8))