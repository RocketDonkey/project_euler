/*Project Euler - Problem 6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
*/
package euler

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

func Euler006() string {
  answer := fmt.Sprint(Answer(100))
  return answer
}
