const fs = require("fs");
let input = Number(fs.readFileSync("/dev/stdin").toString().trim());
let fibo = [BigInt(0), BigInt(1)];

for (let i = 2; i <= input; i++) {
  fibo[i] = BigInt(fibo[i - 1]) + BigInt(fibo[i - 2]);
}

console.log(fibo[input].toString());
