package main

import (
  "fmt"
  "math"
)

func Answer(n int) int{
  // Square of the sum
  n_sum := (n*(n+1))/2
  square_of_sum := int(math.Pow(float64(n_sum), 2))

  // Sum of squares is pyramidal, so we can plug in our n
  // and get the sum of the first n numbers
  n_three, n_two := int(math.Pow(float64(n), 3)), int(math.Pow(float64(n), 2))
  sum_of_squares := (2*(n_three) + 3*(n_two) + n)/6

  return int(square_of_sum - sum_of_squares)
}

func main() {
  answer := Answer(100)
  fmt.Println(answer)
}
