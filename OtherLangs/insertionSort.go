package main

import (
	"os"
	"fmt"
	"bufio"
	"strings"
	"strconv"
)

func readIntegers(path string) ([]int) {
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
	return numbers[1:][0]
}

func insertionSort(a []int) int {
	swaps := 0
	for i := range a {
		value := a[i]
		j := i - 1
		for j >= 0 && a[j] > value {
			a[j+1] = a[j]
			swaps += 1
			j -= 1
		}
		a[j+1] = value
	}
	return swaps
}

func main() {
	array := readIntegers("/Users/QuantumIan/downloads/rosalind_ins.txt")
	swaps := insertionSort(array)
	fmt.Println(swaps)
}