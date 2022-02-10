'use strict';
const fs = require('fs');
const example = false;
const filename = example? "example.txt" : "input.txt";

const data = fs.readFileSync(filename, 'utf8');

function parseRule(rule){
        const key = rule.split(' ')[0] + rule.split(' ')[1];
        let tail = rule.split(' ').slice(4);
        let values = {};
        while (tail.length > 0) {
            if (tail[0] === 'no') {
                break
            } else {
                values[tail[1]+tail[2]] = parseInt(tail[0])
                tail = tail.slice(4)
            }
        }
    return [key, values]
}

function createLookupTable(rules) {
    let ruleTable = {}
    rules = rules.split('\n')
    for (const rule of rules) {
        ruleTable[parseRule(rule)[0]] = parseRule(rule)[1]
    }
    return ruleTable
    
}

function recursiveSearch(lookupTable, lookingFor, rule) {
    let answer = false
    if (rule === {}) {
        return false
    }
    if (lookingFor in rule) {
        return true
    }
    for (const bag in rule) {
        answer = answer || recursiveSearch(lookupTable, lookingFor, lookupTable[bag])
    }
    return answer
}

function recursiveCount(lookupTable, lookingFor) {
    let count = 0
    if (lookupTable[lookingFor] === {}) {
        return count
    }
    for (const bag in lookupTable[lookingFor]) {
        count = count + lookupTable[lookingFor][bag] + lookupTable[lookingFor][bag] * recursiveCount(lookupTable, bag)
    }
    return count
}

function partOne(rules){
    const lookingFor = 'shinygold'
    let answer = 0
    const lookupTable = createLookupTable(rules)
    for (const rule in lookupTable) {
        if (lookupTable[rule] !== {} && recursiveSearch(lookupTable, lookingFor, lookupTable[rule])) {
            answer++
        }
    }
    console.log(`Part One answer: ${answer}`)
}

function partTwo(rules) {
    const lookingFor = 'shinygold'
    const lookupTable = createLookupTable(rules)
    let answer = recursiveCount(lookupTable, lookingFor)
    console.log(`Part Two answer: ${answer}`)
}

partOne(data)
partTwo(data)