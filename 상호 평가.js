// https://programmers.co.kr/learn/courses/30/lessons/83201
function solution(scores) {
  var answer = "";

  let students = {};

  for (let i = 0; i < scores.length; i++) {
    students[i] = [];
    for (let j = 0; j < scores.length; j++) {
      students[i].push(scores[j][i]);
    }
    if (
      students[i][i] === Math.max(...students[i]) &&
      students[i].reduce(
        (cnt, ele) => cnt + (Math.max(...students[i]) === ele),
        0
      ) === 1
    ) {
      // console.log("삭제");
      students[i].splice(i, 1);
    } else if (
      students[i][i] === Math.min(...students[i]) &&
      students[i].reduce(
        (cnt, ele) => cnt + (Math.min(...students[i]) === ele),
        0
      ) === 1
    ) {
      // console.log("삭제");
      students[i].splice(i, 1);
    }

    let score =
      students[i].reduce((cur, acc) => cur + acc) / students[i].length;
    console.log(score);

    switch (true) {
      case score >= 90:
        console.log("A등급");
        answer += "A";
        break;
      case score >= 80:
        answer += "B";
        break;
      case score >= 70:
        answer += "C";
        break;
      case score >= 50:
        answer += "D";
        break;
      default:
        answer += "F";
    }
  }

  // console.log(students);

  return answer;
}
