// https://programmers.co.kr/learn/courses/30/lessons/12916

function solution(s) {
  let counterP = 0;
  let counterY = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "p" || s[i] === "P") {
      counterP += 1;
    }
    if (s[i] === "y" || s[i] === "Y") {
      counterY += 1;
    }
  }
  return counterP === counterY ? true : false;
}

//다른답: 모든 알파벳을 대문자로 바꾼후, "P"와 "Y"로 분리해서 그 길이를 구함
function numPY(s) {
  //함수를 완성하세요
  return (
    s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length
  );
}

// pyY => PYY => [ '', 'YY' ](P로 split), [ 'P', '', '' ](y로 split) => 배열내 요소갯수 비교
