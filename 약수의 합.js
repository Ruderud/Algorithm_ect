// https://programmers.co.kr/learn/courses/30/lessons/12928

function solution(n) {
  let box = [];
  if (n === 0) return 0;

  for (let i = 1; i <= parseInt(n ** 0.5); i++) {
    if (n % i === 0) {
      let a = parseInt(n / i);
      a === i ? box.push(i) : box.push(i, a);
    }
  }

  return box.reduce((acc, cur) => acc + cur);
}

//다른답. 그냥 num까지 하나씩 전부 확인하면서 약수를 더해버림
function solution(num) {
  let sum = 0;
  for (let i = 1; i <= num; i++) {
    if (num % i === 0) sum += i;
  }
  return sum;
}
