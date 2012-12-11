/* Project Euler - Problems

Main function to execute completed problems. When a problem is done,
add its case here.

*/


package euler

// Return the result of the specified problem
func Problems(num int) string {
  switch num {
    case 6:
        return Euler006()
    case 13:
        return Euler013()
    case 14:
        return Euler014()
    case 15:
        return Euler015()
    case 16:
        return Euler016()
    case 20:
        return Euler020()
    case 48:
        return Euler048()
    default:
        return "So unsolved, go back to school."
  }
  return "Returned?"
}
