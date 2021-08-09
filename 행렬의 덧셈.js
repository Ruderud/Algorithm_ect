// https://programmers.co.kr/learn/courses/30/lessons/12950

function solution(arr1, arr2) {
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr1[0].length; j++) {
      arr2[i][j] += arr1[i][j];
    }
  }

  return arr2;
}

//다른답: map을 사용
function sumMatrix(A, B) {
  var answer;
  //맵을 이중으로 사용해서 val, index를 행단위([1,2]) => 행의 요소단위(1,2)로 세분해서 각 요소의 index와 동일한 위치의 다른배열값을 더함
  answer = A.map((a, i) => {
    console.log(a, i);
    return a.map((val, idx) => {
      console.log(val, idx);
      val += B[i][idx];
      return val;
    });
  });

  return answer;
}

console.log(
  sumMatrix(
    [
      [1, 2],
      [2, 3],
    ],
    [
      [5, 6],
      [4, 5],
    ]
  )
);
