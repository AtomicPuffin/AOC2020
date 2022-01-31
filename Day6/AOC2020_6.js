'use strict';
const fs = require('fs');
const example = false;
const filename = example? "example.txt" : "input.txt";

const data = fs.readFileSync(filename, 'utf8');

function countYes(groupAnswer){
    let listOfYes = {}
    for (const answer of groupAnswer) {
        for (const char of answer.trim()) {
            if (listOfYes[char]) {
                listOfYes[char] = listOfYes[char] + 1
            } else {
                listOfYes[char] = 1
            }
            
        }
    }
    return listOfYes
}

function partOne(questionaires){
    let total = 0
    for (const group of questionaires.split('\n\n')) {
        const answers = countYes(group)
        total = total + Object.keys(answers).length
    }
    console.log(total)
}

function partTwo(questionaires) {
    let total = 0
    for (let group of questionaires.split('\n\n')) {
        const answers = countYes(group)
        group = group.trim()
        const groupSize = group.split(/\n/).length
        for (const [key, value] of Object.entries(answers)) {
            if (value  === groupSize) {
                total++
            }
        }
    }
    console.log(total)
}

partOne(data)
partTwo(data)