// https://programmers.co.kr/learn/courses/30/lessons/12940

function solution(n, m) {
  var answer = [];

  //유클리드 호제법을 이용한 최대공약수 계산 => 큰값이 a, 작은값이 b, a%b=r이라고할때, r을 b로하면서 재귀화 => r === 0 이 될때의 a가 바로 최대공약수
  const gcd = (a, b) => {
    if (b === 0) return a;
    return gcd(b, a % b);
  };

  answer.push(gcd(n, m));
  answer.push((n * m) / answer[0]);
  return answer;
}

console.log(solution(3, 12));
