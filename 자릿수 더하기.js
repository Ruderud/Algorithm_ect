// https://programmers.co.kr/learn/courses/30/lessons/12931
function solution(n) {
  var answer = 0;

  for (let i = 0; i < String(n).length; i++) {
    answer += +String(n)[i];
  }

  return answer;
}

//다른답: ""를 더해서 문자열화 한다음, 각 문자열을 split으로 한글자씩 나눠 배열에 넣은다음 이를 reduce를 이용하여 계산했다.
function solution(n) {
  // 쉬운방법
  return (n + "").split("").reduce((acc, curr) => acc + parseInt(curr), 0);
}
