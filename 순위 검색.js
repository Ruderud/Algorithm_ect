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
//     "cpp":      3, /* 011 */      "cpp":      4, /* 100 */
//     "java":     5, /* 101 */      "java":     2, /* 010 */
//     "python":   6, /* 110 */      "python":   1, /* 001 */

//     "backend":  6, /* 110 */      "backend":  1, /* 001 */
//     "frontend": 5, /* 101 */      "frontend": 2, /* 010 */

//     "senior":   6, /* 110 */      "senior":   1, /* 001 */
//     "junior":   5, /* 101 */      "junior":   2, /* 010 */

//     "chicken":  3, /* 011 */      "chicken":  4, /* 100 */
//     "pizza":    6, /* 110 */      "pizza":    1, /* 001 */

//     "-":        7, /* 111 */      "-":        0, /* 000 */
// } => 더 효율적으로 하기 위해, 맨앞글자가 동일할때, 동일한 비트값을 가지게 해서 비트 사용종류를 단축시켰음
// bit field&mask를 이용해서 조건이 만족할때 (cpp field and cpp mask: 3 & 4 = 011 & 100 = 000 = 0) 0을 반환,
//그 이외에는 0 이상의 값(cpp field and java mask: 3 & 2 = 011 & 010 = 010 = 2)을 얻음을 이용

// a   = 011 101 101 110 = 1902 // ["cpp", "frontend", "junior",  "pizza" ]
// b   = 000 010 000 100 = 132  // [ "-" , "frontend",    "-"  , "chicken"]
// a & b = 000 000 000 100 =  4 // [ true,    true   ,   true  ,   false  ] => 즉, field에 info, mask에 query를 대응시켜 & 연산시 모든값이 true (0)가 나오면 적합한다고 판정가능

function solution(info, query) {
  const table = { c: 3, j: 5, p: 6, b: 6, f: 5, s: 6, "-": 0 };

  // info항목을 공백을 기준으로 분할한 후, 각 단어의 첫글자만 가져와서 해당 글자에 해당하는 숫자의 bit값 000(2)를 오른쪽으로 밀어내며 배정
  //"java backend junior pizza 150" => 7 - 각원소의 필드값 (ex java=5 이므로 mask값은 2 = 010이 된다) => 010 001 010 001 = 010001010001 => [1105,150]

  const conv = (l, t) => [
    l.slice(0, -1).reduce((a, k) => (a << 3) + t(table[k[0]]), 0),
    Number(l[l.length - 1]),
  ];

  info = info.map((s) => conv(s.split(" "), (x) => 7 - x));
  //(s)는 info의 value, (x)는 info value의 index를 의미하는데, 이때 7-x를 해줌으로써, field(info)와 mask(query)를 구분할 수 있게된다
  query = query.map((s) =>
    conv(
      s.split(" ").filter((c) => c != "and"),
      (x) => x
    )
  );

  //아래는 Map에 info를 이진해시테이블 규칙에 맟춰 배정하는과정
  const map = new Map();
  for (const [k, v] of info) {
    if (!map.has(k)) map.set(k, []);
    map.get(k).push(v);
  }
  const dict = Array.from(map.entries()).map(([k, l]) => [
    //map.entries는 [key, val]을 한쌍으로하는 iterable객체를 반환 => for..of와 동일하게 쓰인다
    k,
    l.sort((a, b) => a - b),
  ]);
  return query.map(
    ([q, v]) => dict.reduce((a, [k, l]) => a + (k & q ? 0 : bisect_gt(l, v)), 0) //이진겁색을 통해서 해당 값이상의 점수를 가진 사람 수를 구한다
  );
}
