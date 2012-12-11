/*Project Euler - Problem 15

Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
*/

package euler

import (
  "fmt"
  "math"
)


// Return the Central Binomial Coefficient for a number
// The formula is:
//    (2n)!
//  --------
//  (n!)**2
func BinomialCoefficient (num float64) float64 {
  return Factorial(2 * num) / math.Pow(Factorial(num), 2)
}


func Euler015() string {
  bc := BinomialCoefficient(float64(20))
  return fmt.Sprintf("%.0f", bc)
}
