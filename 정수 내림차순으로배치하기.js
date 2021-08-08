// https://programmers.co.kr/learn/courses/30/lessons/12933

function solution(n) {
  return +String(n).split("").sort().reverse().join("");
}

console.log(solution(118372));
