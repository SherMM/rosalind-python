package main

import (
	"os"
	"fmt"
	"bufio"
	"strings"
	"strconv"
)

func readIntegers(path string) ([][]int) {
	file, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	
	var numbers [][]int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		numstr := strings.Split(scanner.Text(), " ")
		var nums []int
		for i := range numstr {
			curr, err := strconv.Atoi(numstr[i])
			if err != nil {
				fmt.Println(err)
			}
			nums = append(nums, curr)
		}
		numbers = append(numbers, nums)
		}
	return numbers[2:]
}

func binarySearch(yvalue int, xarray []int) int {
	x_beg := 0
	x_end := len(xarray) - 1
	for x_beg <= x_end {
		x_mid := (x_end + x_beg) / 2
		if xarray[x_mid] > yvalue {
			x_end = x_mid - 1
		} else if xarray[x_mid] < yvalue {
			x_beg = x_mid + 1
		} else {
			return x_mid + 1
		}
	}
	return -1
}


func indexFinder(xarray []int, yarray []int) []int {
	var indices []int
	for i := 0; i < len(yarray); i++ {
		index := binarySearch(yarray[i], xarray)
		indices = append(indices, index)
	} 
	return indices
}

func main() {
	numbers := readIntegers("../datasets/rosalind_bins.txt")
	xarray := numbers[0]
	yarray := numbers[1]
	indices := indexFinder(xarray, yarray)
	for i := range indices {
		fmt.Print(indices[i])
		fmt.Print(" ")
	}
}