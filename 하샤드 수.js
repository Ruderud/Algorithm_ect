// https://programmers.co.kr/learn/courses/30/lessons/12947

function solution(x) {
  let numSum = String(x)
    .split("")
    .reduce((cur, acc) => +cur + +acc);

  return x % numSum === 0 ? true : false;
}

//return에서 (x%numSum === 0)을 나누어 떨어질때(0) == false, 그렇지않을때 == true로 판정할 수 있으니 그렇게 하면 더 짧아짐
