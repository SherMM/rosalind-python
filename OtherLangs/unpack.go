package main

import (
	"fmt"
	"strings"
)

func main () {
	str := "Hello there!"
	word := strings.Split(str, " ")
	for i, j := range word {
		fmt.Println(i)
		fmt.Println(j)
	}
}