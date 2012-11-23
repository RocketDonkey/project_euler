/*Project Euler - Problem 14
The following iterative sequence is defined for the set of positive integers:

  n  n/2 (n is even)
  n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

  13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem), it
is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

package main

import (
  "fmt"
)


func main() {
  // Store values and the number of steps it takes to get to 1
  steps_map := make(map[float64]int)
  max_steps := 0
  high_val := 0

  for i := 1000000; i > 0; i-- {
    steps := 0
    j := i
    // Cache any subsequent numbers to future calcs on them aren't run
    cache_steps := make([]float64, 0)

    for j != 1 {
      // If are value is already calculated, return num and exit
      if steps_map[float64(j)] != 0 {
        steps += steps_map[float64(j)]
        break
      }

      // If this is a new number, modify accordingly
      steps += 1
      if j % 2 > 0 {
        j = 3*j + 1
      } else {
        j /= 2
      }

      // Append our cache with the new number
      cache_steps = append(cache_steps, float64(j))

    }

   // Get total steps
   steps_map[float64(i)] = steps
   if steps > max_steps {
     max_steps = steps
     high_val = i
   }

   // If our cache is not empty, add the new value into the steps map
   if len(cache_steps) > 0 {
     for index, num := range(cache_steps) {
       steps_map[float64(num)] = steps - (index + 1)
     }
    }
  }

  fmt.Println(high_val)
}

