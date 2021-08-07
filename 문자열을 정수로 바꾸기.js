https://programmers.co.kr/learn/courses/30/lessons/12925

function solution(s) {
    return (s[0] === '-') ? 
        -1 * parseInt(s.substring(1,s.length)) : 
        parseInt(s);
}

//다른답: 동적언어의 특성이용
function strToInt(str){
    return str/1
    }