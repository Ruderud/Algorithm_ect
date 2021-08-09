// https://programmers.co.kr/learn/courses/30/lessons/12954
function solution(x, n) {
  var answer = [];

  for (let i = 1; i <= n; i++) {
    answer.push(x * i);
  }

  return answer;
}

//다른답: n개의 원소가 들은 배열을 미리 만들어두고, 각 원소값에 값을 채워넣는다(fill, map)
function solution(x, n) {
  return Array(n)
    .fill(x)
    .map((v, i) => (i + 1) * v);
}
