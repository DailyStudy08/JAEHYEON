
const fs = require('fs')

const input = fs.readFileSync("/dev/stdin").toString().trim()

let inputNumber = Number(input)

let answer = 0

function get_sum(number) {
    for (i=1; i<=number; i++) {
        answer += i 
    }
}

get_sum(inputNumber)

console.log(answer)