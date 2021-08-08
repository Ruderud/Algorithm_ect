function solution(n) {
  return +String(n).split("").sort().reverse().join("");
}

console.log(solution(118372));
