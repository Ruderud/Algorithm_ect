// https://programmers.co.kr/learn/courses/30/lessons/12921

function solution(n) {
  var answer = 0;

  let prime = [2];
  let primeLen = 1;

  for (let i = 3; i <= n; i++) {
    let isPrime = true;
    let rootN = parseInt(i ** 0.5);
    // console.log(i,rootN);
    for (let j = 0; prime[j] <= rootN; j++) {
      //rootN보다 같거나 작은 소수들로 나눠서 확인해봄
      // console.log(i,prime[j]);
      if (i % prime[j] === 0) {
        isPrime = false;
        break;
      }
    }

    if (isPrime) {
      prime.push(i);
      primeLen += 1;
    }
    // console.log(prime)
  }
  return prime.length;
}

//다른답
function solution(n) {
  const s = new Set();
  //n까지의 홀수들을 가져옴
  for (let i = 1; i <= n; i += 2) {
    s.add(i);
  }
  s.delete(1);
  s.add(2);
  //3~sqrt(n)까지의 자연수를 배수로하는 s내의 값들을 순차적으로 지워나감 (채거르기 방식)
  for (let j = 3; j < Math.sqrt(n); j++) {
    //set.has(value) – 셋 내에 값이 존재하면 true, 아니면 false를 반환
    if (s.has(j)) {
      for (let k = j * 2; k <= n; k += j) {
        s.delete(k);
      }
    }
  }
  return s.size;
}
