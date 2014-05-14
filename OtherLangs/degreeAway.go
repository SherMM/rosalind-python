package main

import (
	"os"
	"fmt"
	"bufio"
	"strings"
	"strconv"
)

func readGraph (path string) map[int][]int {
	file, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	
	first_line := false
	m := make(map[int][]int)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if first_line {
			edge_str := strings.Split(scanner.Text(), " ")
			var edge []int
			for _, j := range (edge_str) {
				node, err := strconv.Atoi(j)
				if err != nil {
					fmt.Println(err)
				}
				edge = append(edge, node)
			}
			m[edge[0]] = append(m[edge[0]], edge[1])
			m[edge[1]] = append(m[edge[1]], edge[0])			
		} else {
			first_line = true
		}
	}
	return m	
}

func degreeCounter (graph map[int][]int) []int {
	var degrees []int
	for i := 1; i < len(graph) + 1; i++ {
		degrees = append(degrees, len(graph[i]))
	}
	return degrees
}

func main() {
	graph := readGraph("/Users/QuantumIan/downloads/rosalind_deg.txt")
	degrees := degreeCounter(graph)
	for _, dcount := range degrees {
		fmt.Print(dcount)
		fmt.Print(" ")
		
	}
}
