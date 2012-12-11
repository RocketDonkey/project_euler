/* Project Euler - Utility Functions */

package euler

import (
  "math/big"
)

// Function for finding the factorial of large numbers
func BigFactorial (n *big.Int) (result *big.Int) {
  o := big.NewInt(1)
  if n.Cmp(o) == -1 {
    result = o
  }
  if n.Cmp(o) == 0 {
    result = o
  } else {
    result = new(big.Int)
    result.Set(n)
    result.Mul(result, BigFactorial(n.Sub(n, o)))
  }
  return result
}


// Cache map to store already-calculated values for Factorial
var factorial_cache = make(map[float64]float64)

// Find the factorial of (smaller) numbers
func Factorial(num float64) float64 {

  if num == 1 {
    return 1
  } else if c, ok := factorial_cache[num]; ok {
    return c
  }

  factorial_cache[num] = num * Factorial(num - 1)
  return factorial_cache[num]
}
