var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
var fs = require('fs');
var example = false;
var filename = example ? "example.txt" : "input.txt";
var data = fs.readFileSync(filename, 'utf8').replace(/\n$/, "").split('\n');
function jump(argument, position) {
    return argument + position;
}
function acc(argument, accumulator) {
    return argument + accumulator;
}
function noOperation(argument) {
}
function execute(instructions) {
    var position = 0;
    var accumulator = 0;
    var visited = [];
    while (!(visited.includes(position))) {
        if (position === instructions.length) {
            return [accumulator, true];
        }
        if (position > instructions.length) {
            return [0, false];
        }
        var argument = Number(instructions[position].split(' ')[1]);
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
    var accumulator = execute(instructions);
    console.log("Part One answer: ".concat(accumulator[0]));
}
function partTwo(instructions) {
    var position = 0;
    while (position < instructions.length) {
        var temp = __spreadArray([], instructions, true);
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
        var result = execute(temp);
        if (result[1]) {
            console.log("Part Two answer: ".concat(result[0]));
            return;
        }
        position++;
    }
}
partOne(data);
partTwo(data);
