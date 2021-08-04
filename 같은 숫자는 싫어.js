// https://programmers.co.kr/learn/courses/30/lessons/12906

//가장 기본적인접근인, 가져온 배열이 저장중인배열의 맨뒷글자와 같지않을때만 추가하는방법

console.log(solution([1, 3, 3, 0, 0, 1]));
// function solution(arr)
// {
//     var answer = [];

//     for(var i=0; i<arr.length; i++){
//         if(arr[i]!==answer[answer.length-1]){
//             answer.push(arr[i]);
//         }
//     }
//     return answer;
// }

//다른답 1
function solution(arr) {
  return arr.filter((val, index) => val != arr[index + 1]);
}

//filter는 조건에 부합하는 요소들을 배열에 담아서 반환하는 함수
//여기서 val은 원 배열 arr에서 하나씩 가져오는 원소이며, index는 arr의 포인터의 역할을 하게끔 값을 선언해서 사용했다.
