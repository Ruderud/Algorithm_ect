// https://programmers.co.kr/learn/courses/30/lessons/12926

function solution(s, n) {
  var answer = "";

  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") {
      answer += " ";
    } else if (s[i].charCodeAt() <= 90) {
      s[i].charCodeAt() + n > 90
        ? (answer += String.fromCharCode(s[i].charCodeAt() + n - 25))
        : (answer += String.fromCharCode(s[i].charCodeAt() + n));
    } else {
      s[i].charCodeAt() + n > 122
        ? (answer += String.fromCharCode(s[i].charCodeAt() + n - 26))
        : (answer += String.fromCharCode(s[i].charCodeAt() + n));
    }
  }

  return answer;
}
//아스키코드 값을 이용

//다른답
//2진법으로 대문자의 코드들은 1000001~1011010, 소문자는 1100001~1111010임.
//대문자 소문자는 앞에 2자리 빼고는 같기에, 32로 나눈 나머지값으로 대소문자 구분을 하고, 나머지는 시저암호화
function caesar(s, n) {
  var result = s.replace(
    /[a-z]/gi,
    (c) =>
      [
        (c = c.charCodeAt(0)),
        String.fromCharCode((c & 96) + (((c % 32) + n - 1) % 26) + 1),
      ][1]
  );

  // 함수를 완성하세요.
  return result;
}
