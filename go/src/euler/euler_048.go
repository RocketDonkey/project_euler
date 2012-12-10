/* Project Euler - Problem 48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
*/

package main

import (
  "fmt"
  "math/big"
)


// Apply the exponents to each number
func PowerUp(num int) *big.Int {
  curr_num := big.NewInt(int64(num))
  big_num := big.NewInt(int64(num))
  for i := 1; i < num; i++ {
    big_num.Mul(big_num, curr_num)
  }

  return big_num
}


// Iterate through each number in the range, summing the results
func SumUntil(num int) *big.Int {
  sum := big.NewInt(0)
  for i := 1; i <= num; i++ {
    sum = sum.Add(sum, PowerUp(i))
  }
  return sum
}

func main() {
  sum_str := SumUntil(1000).String()
  fmt.Println(sum_str[len(sum_str)-10:])
}
