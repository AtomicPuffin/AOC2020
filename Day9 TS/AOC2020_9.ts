const fs = require('fs');

const example = false;
const filename = example? "example.txt" : "input.txt";

const data = fs.readFileSync(filename, 'utf8').replace(/\n$/, "").split('\n').map(Number);

if (example) {
    var preamble_length = 5
} else {var preamble_length = 25}
partOne(data, preamble_length)
partTwo(data, preamble_length)

function validator(preamble: number[], check: number): boolean {
    while (preamble.length > 0) {
        const a = preamble.shift()
        for (const b of preamble) { // unsure if "can not be same number" is literal or instanced
            if (a + b === check && a != b) { // applied literal check
                return true
            }
        }
    }
    return false
}

function find_first_invalid(data:number[], preamble_length: number): number{
    let iter = preamble_length
    while (iter < data.length) {
        if (!validator(data.slice(iter-preamble_length ,iter+1), data[iter+1])) {
            return data[iter +1]
        }
        iter++
    }
}

function contiguos(data:number[], invalid: number): number{
    let iter_start = 0
    while (iter_start < data.length) {
        let sum = 0
        let iter_end = iter_start
        while (sum <= invalid) {
            sum = sum + data[iter_end]
            if (sum === invalid) {
                const min = Math.min(...data.slice(iter_start, iter_end+1))
                const max = Math.max(...data.slice(iter_start, iter_end+1))
                return min + max
            }
            iter_end++
        }
        iter_start++
    }
}

function partOne(data:number[], preamble_length: number): void{
    const result = find_first_invalid(data, preamble_length)
    console.log(`Part One answer: ${result}`)
    
}

function partTwo(data:number[], preamble_length: number): void{
    const invalid = find_first_invalid(data, preamble_length)
    const result = contiguos(data, invalid) 
    console.log(`Part Two answer: ${result}`)
}
