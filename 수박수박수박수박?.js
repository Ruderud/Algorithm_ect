// https://programmers.co.kr/learn/courses/30/lessons/12922

function solution(n) {
  var answer = "";

  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      answer += "수";
    } else {
      answer += "박";
    }
  }

  return answer;
}

//문자열 슬라이싱할때 str.substring(2,5) 이런식도 가능한데 무식한방법
// str.repeat(n/2)에 홀수일때 '수'문자열을 마지막에 붙여주는것이 더 좋은듯
