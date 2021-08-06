// https://programmers.co.kr/learn/courses/30/lessons/12919

function solution(seoul) {
  let site = seoul.findIndex((val) => val === "Kim");

  return `김서방은 ${site}에 있다`;
}

//indexOf도 쓸수있음 => seoul.indexOf("Kim") // 1
