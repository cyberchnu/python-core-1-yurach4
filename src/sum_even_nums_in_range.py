def sum_even_nums_in_range(start, stop):
  even_sum = 0
  for num in range(start, stop + 1):
    if num % 2 == 0:
      even_sum += num
  return even_sum