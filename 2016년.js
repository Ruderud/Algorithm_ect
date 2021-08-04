// https://programmers.co.kr/learn/courses/30/lessons/12901

function solution(a, b) {
  var days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  var day = new Date(`2016-${a}-${b}`).getDay();
  return days[day];
}
