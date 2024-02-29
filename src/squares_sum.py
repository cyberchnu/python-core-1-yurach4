def squares_sum(n):
  sum_of_squares = 0
  for num in range(1, n + 1):
    sum_of_squares += num ** 2
  return sum_of_squares
