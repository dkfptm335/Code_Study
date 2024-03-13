import Swift

// 상수와 변수
// 상수 선언 let
// 변수 선언 var

// let or var 변수명: 타입 = 값

let constant : String = "상수"
var variable : String = "변수"

variable = "변수 변경"
// constant = "상수 변경" // 상수는 변경 불가능

// 상수 선언 후에 나중에 값 할당하기
let sum : Int
let inputA : Int = 100
let inputB : Int = 200

sum = inputA + inputB // 한번만 할당 가능

// 변수나 상수의 타입이 명확하다면 타입 어노테이션을 생략할 수 있음
let name = "Gloomy"
var age = 27

print(constant)
print(variable)
print(sum)

print("안녕하세요 저는 \(age)살 \(name)입니다.")