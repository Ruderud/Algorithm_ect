function solution(arr, divisor) {
  var answer = [];

  answer = arr.filter((val) => val % divisor === 0);

  return answer == false
    ? [-1]
    : answer.sort((a, b) => {
        console.log(a, b);
        if (a > b) return 1;
        if (a == b) return 0;
        if (a < b) return -1;
      });
}

solution([2, 36, 1, 3], 1);

//마지막 sort를
return answer == false ? [-1] : answer.sort((a, b) => a - b);
//로 하면 더 깔끔해진다.

//js의 sort는 파이썬과 달리, elements를 문자열로 가져와서 유니코드순으로 정리하기에, [5,10] => [10,5]가 된다
//그렇기에 숫자로써 정렬하려면 a-b비교처리를 통해 -면 좌, +면 우, 0이면 동 위치에 두도록 하는 작업이 필요

//+ 화살표함수 쓸때, {}를 이용해서 여러줄로 항목을 작성할시, 꼭 return을 통해서 최종결과를 반환케 해야한다
