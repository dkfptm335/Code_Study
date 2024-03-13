import Swift

let age: Int = 10

print("안녕하세요 저는 \(age)살 입니다.")
print("안녕하세요 저는 \(age + 10)살 입니다.")

print("\n####################\n")

class Person {
    var name: String = "Gloomy"
    var age: Int = 10
}

let Gloomy: Person = Person()

print(Gloomy)
print("\n####################\n")
dump(Gloomy)