package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	partOne()
	partTwo()
}

func setup() []string {
	//data, err := ioutil.ReadFile("example.txt")
	data, err := ioutil.ReadFile("input.txt")
	inputRaw := strings.Split(strings.TrimSuffix(string(data), "\n"), "\n")
	if err != nil {
		panic(err)
	}

	input := []string{}
	for _, line := range inputRaw {
		input = append(input, "."+line+".")
	}
	emptyLine := ""
	for i := 0; i < len(input[0]); i++ {
		emptyLine = emptyLine + "."
	}
	input = append([]string{emptyLine}, input...)
	input = append(input, emptyLine)
	return input
}

type coordinate struct {
	x int
	y int
}

func countNeighbours1(layout []string, seat coordinate) int {
	neighbours := [][]int{{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}
	count := 0
	for _, i := range neighbours {
		if string(layout[seat.y+i[0]][seat.x+i[1]]) == "#" {
			count++
		}
	}
	return count
}

func countNeighbours2(layout []string, seat coordinate) int {
	neighbours := [][]int{{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}
	count := 0
	for _, i := range neighbours {
		for y, x := seat.y+i[0], seat.x+i[1]; x >= 0 && y >= 0 && x < len(layout[0]) && y < len(layout); y, x = y+i[0], x+i[1] {
			if string(layout[y][x]) == "#" {
				count++
				break
			} else if string(layout[y][x]) == "L" {
				break
			}
		}
	}
	return count
}

func seatEvaluation(layout []string, seat coordinate, limit int, count func([]string, coordinate) int) (string, bool) {
	if string(layout[seat.y][seat.x]) == "." { // border will never check neighbours
		return ".", false
	}
	neighbours := count(layout, seat)
	if string(layout[seat.y][seat.x]) == "L" {
		if neighbours == 0 {
			return "#", true
		} else {
			return "L", false
		}
	} else if string(layout[seat.y][seat.x]) == "#" {
		if neighbours >= limit {
			return "L", true
		} else {
			return "#", false
		}
	}
	panic("seatEval not matching")
}

func countSeats(layout []string) int {
	counter := 0
	for y := 0; y < len(layout); y++ {
		for x := 0; x < len(layout[0]); x++ {
			if string(layout[y][x]) == "#" {
				counter++
			}
		}
	}
	return counter
}

func partOne() {
	currentState := setup()
	noChange := true
	for noChange {
		noChange = false
		nextState := []string{}
		for y := 0; y < len(currentState); y++ {
			row := ""
			for x := 0; x < len(currentState[0]); x++ {
				newSeat, change := seatEvaluation(currentState, coordinate{x, y}, 4, countNeighbours1)
				row = row + newSeat
				noChange = noChange || change
			}
			nextState = append(nextState, row)
		}
		currentState = nextState
	}

	fmt.Print("Part One answer: ")
	fmt.Println(countSeats(currentState))
}

func partTwo() {
	currentState := setup()
	noChange := true
	for noChange {
		noChange = false
		nextState := []string{}
		for y := 0; y < len(currentState); y++ {
			row := ""
			for x := 0; x < len(currentState[0]); x++ {
				newSeat, change := seatEvaluation(currentState, coordinate{x, y}, 5, countNeighbours2)
				row = row + newSeat
				noChange = noChange || change
			}
			nextState = append(nextState, row)
		}
		currentState = nextState
	}
	fmt.Print("Part Two answer: ")
	fmt.Println(countSeats(currentState))
}
