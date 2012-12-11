/* Project Euler - Solutions

Extremely advanced Go usage here, watch out. Solutions to some Project Euler
problems, with each solved problem executed and returned with the time it took
to complete.

*/

package main

import (
  "fmt"
  "euler"
)

// Show all of the solved problems
func main() {
  fmt.Println("*************************")
  fmt.Println("** Project Euler in Go **")
  fmt.Println("*************************")

  // Cycle through the first 50
  for v := 1; v <= 50; v++ {
    fmt.Println(fmt.Sprintf("Problem %d:", v), euler.Problems(v))
  }

}
