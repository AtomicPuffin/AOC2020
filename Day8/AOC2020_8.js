const fs = require('fs');
const example = false;
const filename = example ? "example.txt" : "input.txt";
const data = fs.readFileSync(filename, 'utf8').replace(/\n$/, "").split('\n');
//console.log('inp '+ input)
//const data = input.split('\n');
//console.log('dad '+data)
function jump(argument, position) {
    return argument + position;
}
function acc(argument, accumulator) {
    return argument + accumulator;
}
function noOperation(argument) {
}
function execute(instructions) {
    let position = 0;
    let accumulator = 0;
    let visited = [];
    while (!(visited.includes(position))) {
        if (position === instructions.length) {
            return [accumulator, true];
        }
        if (position > instructions.length) {
            return [0, false];
        }
        const argument = Number(instructions[position].split(' ')[1]);
        switch (instructions[position].split(' ')[0]) {
            case 'acc':
                accumulator = acc(argument, accumulator);
                visited.push(position);
                position++;
                break;
            case 'jmp':
                visited.push(position);
                position = jump(argument, position);
                break;
            case 'nop':
                noOperation(argument);
                visited.push(position);
                position++;
                break;
            default:
                console.log('Switch messup execute');
                console.log('switch error ' + instructions[position]);
                return;
        }
    }
    return [accumulator, false];
}
function partOne(instructions) {
    let accumulator = execute(instructions);
    console.log(`Part One answer: ${accumulator[0]}`);
}
function partTwo(instructions) {
    let position = 0;
    while (position < instructions.length) {
        let temp = [...instructions];
        switch (instructions[position].split(' ')[0]) {
            case 'acc':
                break;
            case 'jmp':
                temp[position] = 'nop ' + instructions[position].split(' ')[1];
                break;
            case 'nop':
                temp[position] = 'jmp ' + instructions[position].split(' ')[1];
                break;
            default:
                console.log('Switch messup p2');
                console.log(temp[position]);
                return;
        }
        let result = execute(temp);
        if (result[1]) {
            console.log(`Part Two answer: ${result[0]}`);
            return;
        }
        position++;
    }
}
partOne(data);
partTwo(data);
//# sourceMappingURL=AOC2020_8.js.map