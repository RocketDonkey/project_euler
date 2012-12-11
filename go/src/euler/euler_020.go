/*Project Euler - Problem 20

n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
*/


package euler

import (
  "fmt"
  "math/big"
  "strconv"
)

func Euler020() string {
  num := big.NewInt(100)
  answer := BigFactorial(num)

  // Convert to string and sum the digits
  a_str := answer.String()
  var dig_sum int64 = 0
  for _, v := range(a_str) {
    n, _ := strconv.ParseInt(string(v), 0, 0)
    dig_sum += n
  }
    //fmt.Println(dig_sum)
    return fmt.Sprint(dig_sum)
}

