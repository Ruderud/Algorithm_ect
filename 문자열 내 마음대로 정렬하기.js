// https://programmers.co.kr/learn/courses/30/lessons/12915#

function solution(strings, n) {
  var answer = [];
  answer = strings.sort((val1, val2) => {
    if (val1[n] === val2[n]) {
      //n번째 문자열이 같을때는 전체 문자열의 앞에서부터 순서를 비교해서 서열값을 반환
      return (val1 > val2) - (val1 < val2); // val1 = aab, val2 = aac일때 => (false) - (true) = 0 - 1 = -1을 반환
    } else {
      return (val1[n] > val2[n]) - (val1[n] < val2[n]);
    }
  });

  return answer;
}

//다른답
function solution(strings, n) {
  // strings 배열
  // n 번째 문자열 비교
  return strings.sort((s1, s2) =>
    s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n])
  );
}
// a.localeCompare(b)는 문자열을 유니코드로써 비교할때 사용한다
// a < b이면 음수, a > b이면 양수, a === b이면 0을 반환
