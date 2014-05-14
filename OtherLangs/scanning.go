package main

import (
	"os"
	"fmt"
	"bufio"
)

func main() {
	file, err := os.Open("edge_list.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan() {
		str := scanner.Text()
		fmt.Println(str)
	}
}