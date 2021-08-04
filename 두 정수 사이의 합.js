// https://programmers.co.kr/learn/courses/30/lessons/12912

function solution(a, b) {
  var answer = 0;
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) answer += i;
  return answer;
}

function adder(a, b) {
  var result = 0;
  //함수를 완성하세요

  return ((a + b) * (Math.abs(b - a) + 1)) / 2;
}

//가우스공식을 사용: a~b까지의 모든 수의 합은 (a+b) * |b-a| / 2 인것을 이용
