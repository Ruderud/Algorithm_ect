// https://programmers.co.kr/learn/courses/30/lessons/81301

function solution(s) {
  var answer = "";

  const number = {
    zero: "0",
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  };

  let sentence = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) {
      answer += s[i];
    } else {
      sentence += s[i];
    }

    if (sentence in number) {
      answer += number[sentence];
      sentence = "";
    }
  }

  return +answer;
}

//다른답
function solution1(s) {
  let numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  var answer = s;

  for (let i = 0; i < numbers.length; i++) {
    let arr = answer.split(numbers[i]);
    //모든 zero, 모든 one... 이런식으로 영단어 종류별로 분리시킨후, 이를 숫자로 바꿔서 join으로 answer에 넣어버림
    //ex) zero1zero8eightfive8 => 'zero', '1','zero', '8eightfive8' => 0108eightfive8
    answer = arr.join(i);
  }

  return Number(answer);
}

console.log(solution1("2three45sixseven"));
