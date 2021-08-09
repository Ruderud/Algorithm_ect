// https://programmers.co.kr/learn/courses/30/lessons/12943

function solution(num) {
  var answer = 0;

  while (num !== 1) {
    if (num % 2 === 0) {
      num = num / 2;
    } else {
      num = num * 3 + 1;
    }
    answer += 1;
    if (answer === 500) {
      return -1;
    }
  }

  return answer;
}

console.log(solution(626331));

//다른답: while문 조건에 answer을 넣어버리고 삼항연산자를 사용하면 더 간결하게도 가능하다
function collatz(num) {
  var answer = 0;
  while (num != 1 && answer != 500) {
    num % 2 == 0 ? (num = num / 2) : (num = num * 3 + 1);
    answer++;
  }
  return num == 1 ? answer : -1;
}
