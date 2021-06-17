function printName() {
  var inner1 = () => console.log(this.name, name);
  var inner2 = function () {
    console.log(this.name, name);
  };
  function print() {
    inner1();
    inner2();
  }
  console.log(name); //1-1.undefined출력; (name이라는 변수가 정의되지않은상태)
  var name = "C"; //1-2.name이 이제 선언되고, "C"가 할당되었음

  print();
  //2-1. print -> inner1() -> A, C; { name: "A", fnc: printName }객체단을 this로 가져오게되어 A가 출력, name은 할당된 "C"를 가져옴
  //           -> inner2() -> B, C; function() { console.log(this.name, name); }시, Closure에 의해 여기서의 this는 global(브라우져에서는 window)단에서 값을 가져옴
  //                                그렇기에 this.name = global.name이되어 global에있는 "B"를 가져오며, name은 1-2에서 선언된 "C"를 가져온다

  name = "D"; //2-2. 선언되어있는 name의 value가 "D"로 바뀜

  console.log(this); //3. { name: 'A', fnc: [Function: printName] }출력; 여기서의 this는 function printName이 속한 객체 { name: "A", fnc: printName }를 의미한다.

  return print;
  //4. print -> inner1() -> A, D;
  //         -> inner2() -> B, D;     -> inner각각의 A,B는 위의 2-1의 이유로 동일하게 출력, printName함수내에서 선언된 name값만 "C"->"D"로바뀌었다.
}
name = "B";
({ name: "A", fnc: printName }.fnc()());

/*
출력결과:
undefined
A C
B C
{ name: 'A', fnc: [Function: printName] }
A D
B D
*/

// 함수내부의 function() { ...this } 의 this는 global(window)를 향한다는것이 핵심
// https://jeonghwan-kim.github.io/2017/10/22/js-context-binding.html js의 this 바인딩 우선순위
