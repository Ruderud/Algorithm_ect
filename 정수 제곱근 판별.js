// https://programmers.co.kr/learn/courses/30/lessons/12934

function solution(n) {
  return n / Math.sqrt(n) === parseInt(n ** 0.5)
    ? (parseInt(n ** 0.5) + 1) ** 2
    : -1;
}
