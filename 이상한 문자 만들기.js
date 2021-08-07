// https://programmers.co.kr/learn/courses/30/lessons/12930
function solution(s) {
  var answer = "";
  let pointer = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] !== " " && pointer % 2 === 0) {
      answer += s[i].toUpperCase();
      pointer += 1;
    } else if (s[i] !== " " && pointer % 2 === 1) {
      answer += s[i].toLowerCase();
      pointer += 1;
    } else {
      answer += " ";
      pointer = 0;
    }
  }
  return answer;
}

//다른답: 공백을 기준으로 단어 단위로 나눈후, map을 이용하여 각 단어를 알파벳으로 쪼갠다.
//쪼갠 단어단위 배열은 (알파벳, index)로 불러와서, index의 홀 짝여부로 삼항연산자를 이용하여 대문자/소문자 작업을 해서 join으로 조립후, 단어들을 또한번 join으로 묶음
function toWeirdCase(s) {
  return s
    .split(" ")
    .map((i) =>
      i
        .split("")
        .map((j, key) => (key % 2 === 0 ? j.toUpperCase() : j))
        .join("")
    )
    .join(" ");
}
