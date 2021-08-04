// https://programmers.co.kr/learn/courses/30/lessons/12918
function solution(s) {
  var num = /[0-9]/;

  if (s.length === 4 || s.length === 6) {
    for (let i = 0; i < s.length; i++) {
      if (!num.test(s[i])) {
        return false;
      }
    }
    return true;
  }
  return false;
}

//정규식과 test 메서드를 이용한 풀이
// https://ko.javascript.info/regexp-introduction
// '/ 내용 /'은 해당 내용의 정규식을 선언하는 방식
var check_num = /[0-9]/;
var check_eng = /[a-zA-Z]/;
var check_spc = /[~!@#$%^&*()_+|<>?:{}]/;
var check_kor = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;

check_num.test(str); //해당 문자열에 숫자문자의 존재여부체크 => return 값 true / false
