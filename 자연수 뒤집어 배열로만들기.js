// https://programmers.co.kr/learn/courses/30/lessons/12932

function solution(n) {
  var answer = [];

  let str = String(n);

  for (let i = str.length - 1; i >= 0; i--) {
    answer.push(+str[i]);
  }

  return answer;
}

//다른답
function solution(n) {
  return n
    .toString() //n을 문자열로 바꾼후
    .split("") //숫자하나씩 분리해서 배열에 담고
    .reverse() //순서를 뒤집는다
    .map((o) => (o = parseInt(o))); // 마지막으로 배열내 문자화 되어있는 숫자들을 다시 정수로 바꾼다
}
