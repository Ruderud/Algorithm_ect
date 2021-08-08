// https://programmers.co.kr/learn/courses/30/lessons/12935
function solution(arr) {
  let a = arr.indexOf(Math.min(...arr));
  arr.splice(a, 1);

  return arr != false ? arr : [-1];
}

console.log(solution([5, 1, 3]));
