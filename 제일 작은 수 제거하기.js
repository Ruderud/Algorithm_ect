function solution(arr) {
  let a = arr.indexOf(Math.min(...arr));
  arr.splice(a, 1);

  return arr != false ? arr : [-1];
}

console.log(solution([5, 1, 3]));

// let arr = [1, 2, 3];

// arr.splice(1, 1);

// console.log(arr);
