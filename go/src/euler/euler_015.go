/*Project Euler - Problem 15

Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
*/

package main

import (
  "fmt"
  "math"
)

// Cache map for Factorial function
var cache = make(map[float64]float64)


// Find the factorial of a number
func Factorial(num float64) float64 {
  if num == 1 {
    return 1
  } else if c, ok := cache[num]; ok {
    return c
  }

  cache[num] = num * Factorial(num - 1)
  return cache[num]
}


// Return the Central Binomial Coefficient for a number
// The formula is:
//    (2n)!
//  --------
//  (n!)**2
func BinomialCoefficient (num float64) float64 {
  return Factorial(2 * num) / math.Pow(Factorial(num), 2)
}


func main() {
  bc := BinomialCoefficient(float64(20))
  fmt.Printf("%.0f\n", bc)
}
