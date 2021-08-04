// https://programmers.co.kr/learn/courses/30/lessons/12903

function solution(s) {
  var answer = "";

  answer =
    s.length % 2 === 0
      ? s[parseInt(s.length / 2) - 1] + s[parseInt(s.length / 2)]
      : s[parseInt(s.length / 2)];

  return answer;
}
