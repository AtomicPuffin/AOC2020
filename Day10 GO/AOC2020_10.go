package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

func main() {
	partOne()
	partTwo()
}

func setup() []int {
	//data, err := ioutil.ReadFile("example.txt")
	data, err := ioutil.ReadFile("input.txt")
	rawInput := strings.Split(strings.TrimSuffix(string(data), "\n"), "\n")
	if err != nil {
		panic(err)
	}
	input := []int{}
	for _, i := range rawInput {
		n, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}
		input = append(input, n)
	}

	return input
}

func contains(adapters []int, num int) bool {
	for _, v := range adapters {
		if v == num {
			return true
		}
	}
	return false
}

func partOne() { // iterate sorted list and count deltas
	input := setup()
	sort.Ints(input[:])
	input = append([]int{0}, input...)               //add outlet to list
	adapters := append(input, input[len(input)-1]+3) // add device
	counters := []int{0, 0, 0}
	for i := range input {
		delta := adapters[i+1] - adapters[i]
		counters[delta-1]++
	}
	fmt.Print("Part One answer: ")
	fmt.Println(counters[0] * counters[2])
}

func partTwo() { // iterate reversed and calculate total paths at position x, previous is sum off all in range
	input := setup()
	sort.Ints(input[:])
	input = append([]int{0}, input...)               //add outlet to list
	adapters := append(input, input[len(input)-1]+3) // add device
	arrangements := make(map[int]int)
	arrangements[input[len(input)-1]+3] = 1
	total := 0
	for i := range input {
		count := 0
		if contains(adapters, adapters[len(adapters)-i-2]+1) {
			count = count + arrangements[adapters[len(adapters)-i-2]+1]
		}
		if contains(adapters, adapters[len(adapters)-i-2]+2) {
			count = count + arrangements[adapters[len(adapters)-i-2]+2]
		}
		if contains(adapters, adapters[len(adapters)-i-2]+3) {
			count = count + arrangements[adapters[len(adapters)-i-2]+3]
		}
		arrangements[adapters[len(adapters)-i-2]] = count
		total = total + count

	}
	//fmt.Println(arrangements)
	fmt.Print("Part Two answer: ")
	fmt.Println(arrangements[0])
}
