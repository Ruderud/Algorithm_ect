// https://programmers.co.kr/learn/courses/30/lessons/72412?language=javascript

//이진검색 함수구현 => 배열a와 목표값 x를 받아서, a배열에서 x값이상의 갯수를 반환
function bisect_gt(a, x) {
  let lo = 0,
    hi = a.length;
  while (lo < hi) {
    let mid = Math.floor((lo + hi) / 2);
    if (a[mid] < x) lo = mid + 1;
    else hi = mid;
  }
  return a.length - lo;
}

//해시 테이블종류가 총 108종류(4*3*3*3)이므로, 이를 먼저 만들어놓고, info의 데이터를 여러 부분집합에 할당하게함

// table = {
//     "cpp": 1, "java": 2, "python": 3,
//     "backend": 1, "frontend": 2,
//     "senior": 1, "junior": 2,
//     "chicken": 1, "pizza": 2,
//     "-": 0,
// }

// a = [1, 2, 2, 2] # ["cpp", "frontend", "junior",  "pizza" ]
// b = [0, 2, 0, 1] # [ "-" , "frontend",    "-"  , "chicken"]
// info를 숫자를 이용한 테이블화를 통해 검색시 보다 효율적으로 진행하게함

// field = {                     mask = {
//     "cpp":      1, /* 001 */      "cpp":      6, /* 110 */
//     "java":     2, /* 010 */      "java":     5, /* 101 */
//     "python":   4, /* 100 */      "python":   3, /* 011 */

//     "backend":  1, /* 001 */      "backend":  6, /* 110 */
//     "frontend": 2, /* 010 */      "frontend": 5, /* 101 */

//     "senior":   1, /* 001 */      "senior":   6, /* 110 */
//     "junior":   2, /* 010 */      "junior":   5, /* 101 */

//     "chicken":  1, /* 001 */      "chicken":  6, /* 110 */
//     "pizza":    2, /* 010 */      "pizza":    5, /* 101 */

//     "-":        7, /* 111 */      "-":        0, /* 000 */
// }
// bit field&mask를 이용해서 조건이 만족할때 (cpp field and cpp mask: 1 & 6 = 001 & 110 = 000 = 0) 0을 반환,
//그 이외에는 0 이상의 값(cpp field and java mask: 1 & 5 = 001 & 101 = 001 = 1)을 얻음을 이용

// a   = 001 010 010 010 = 658 // ["cpp", "frontend", "junior",  "pizza" ]
// b   = 000 101 000 110 = 326 // [ "-" , "frontend",    "-"  , "chicken"]
// a & b = 000 000 000 010 =   2 // [ true,    true   ,   true  ,   false  ] => 즉, field에 info, mask에 query를 대응시켜 & 연산시 모든값이 true (0)가 나오면 부합한다고 판정가능

function solution(info, query) {
  const table = { c: 3, j: 5, p: 6, b: 6, f: 5, s: 6, "-": 0 };

  // info항목을 공백을 기준으로 분할한 후, 각 단어의 첫글자만 가져와서 해당 글자에 해당하는 숫자의 bit값을 오른쪽 3칸만큼을 이용하여 배정
  //"java backend junior pizza 150" => 010 + 001 + 010 + 010 = 111 => [1105,150]   //101 110 101 101  413

  const conv = (l, t) => [
    l.slice(0, -1).reduce((a, k) => (a << 3) + t(table[k[0]]), 0),
    Number(l[l.length - 1]),
  ];
  info = info.map((s) => conv(s.split(" "), (x) => 7 - x));
  //   console.log(info);
  query = query.map((s) =>
    conv(
      s.split(" ").filter((c) => c != "and"),
      (x) => x
    )
  );
  const map = new Map();
  for (const [k, v] of info) {
    if (!map.has(k)) map.set(k, []);
    map.get(k).push(v);
  }
  const dict = Array.from(map.entries()).map(([k, l]) => [
    k,
    l.sort((a, b) => a - b),
  ]);
  return query.map(([q, v]) =>
    dict.reduce((a, [k, l]) => a + (k & q ? 0 : bisect_gt(l, v)), 0)
  );
}
