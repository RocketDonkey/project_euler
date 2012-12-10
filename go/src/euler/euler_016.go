/*Project Euler - Problem 16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
*/

package main

import (
  "math/big"
  "fmt"
  "strconv"
  )

func main() {
  // Allocate new int
  num_str := big.NewInt(2)

  // Multiply by 2 1000 times
  for i := 1; i < 1000; i++ {
    num_str = num_str.Mul(num_str, big.NewInt(2))
  }

  // Create total and digit var
  total := 0
  dig := 0

  // Loop through characters of the string, summing ints
  for _, c := range num_str.String() {
    dig, _ = strconv.Atoi(string(c))
    total += dig
  }

  // Print total
  fmt.Println(total)
}

