# "Learning Kotlin Basic"

## Basic Syntax

### Program entry point

an entry point is the `main` function

```kotlin
fun main() {
    println("Hello world!")
}
```

### Variables

read-only: `val`

reassignable: `var`

```kotlin
val a: Int = 1  // immediate assignment
val b = 2   // `Int` type is inferred
var x = 5 // `Int` type is inferred
x += 1
```

### Nullable values and _null_ checks

the default variable in Kotlin cannot be null.

use `?` to mark the nullable variable.

(A reference must be explicitly marked as nullable when _null_ value is possible.)

```kotlin
var name: String? = "Kate"
name = null
```

### Functions

use `fun` keywords to declare functions.

```kotlin
fun double(x: Int): Int {
    return 2 * x
}
```

named arguments: function parameters can be named when calling functions. This is very convenient when a function has a high number of parameters or default ones.

```kotlin
fun greetPerson(greeting: String, name: String) = println("$greeting $name")

fun main() {
    greetPerson(name = "Nate", greeting = "Hi")
}
```

parameters with default value.

```kotlin
fun greetPerson(greeting: String = "Hello", name: String = "Kotlin") = println("$greeting $name")

fun main() {
    greetPerson()
}

// Hello Kotlin
```

`vararg` support zero one or any other number of argument values to be passed it.

[Variable number of arguments (_vararg_)](https://kotlinlang.org/docs/reference/functions.html#variable-number-of-arguments-varargs) can be passed in the named form by using the **spread** operator:

```kotlin
fun sayHello(greeting: String, vararg itemsToGreet: String) {
    itemsToGreet.forEach { itemToGreet ->
        println("$greeting $itemToGreet")
    }
}

fun main() {
    val interestingThings = arrayOf("Kotlin", "Programming", "Comic Books")
    sayHello("hi", *interestingThings)
}

// hi Kotlin
// hi Programming
// hi Comic Books
```

### Conditional expressions

`if`...`else` expression

```kotlin
fun maxOf(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}
```

`when` expression

```kotlin
fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }
```

### Collections

declare a collection.

```Kotlin
val interestingThings = listOf("Kotlin", "Programming", "Comic Books")
```

basic properties.

```kotlin
interestingThings.size
interestingThings[0]
```

use `for` ...`in` to iterate.

```kotlin
for (interestingThing in interestingThings) {
    println(interestingThing)
}
```

use builtin `forEach` method to iterate.

```kotlin
interestingThings.forEach {
    println(it)
}
// or
interestingThings.forEach { interestingThing ->
    println(interestingThing)
}
```

use builtin `forEachIndexed` method to iterate with index.

```kotlin
interestingThings.forEachIndexed { index, interestingThing ->
    println("$interestingThing is at index $index")
}
```

> defaultly, collection and map is immutable. if you want to make changes, use `mutable` collection and map.

mutable list

```kotlin
val interestingThings = mutableListOf("Kotlin", "Programming", "Comic Books")
interestingThings.add("Dog")
```

mutable map

```kotlin
val map = mutableMapOf(1 to "a", 2 to "b", 3 to "c")
map[4] = "d"
map.forEach { (key, value) -> println("$key -> $value") }
```

## Classes

use `class` keyword to declare classes.

```kotlin
class Person {/*...*/}
```

A class in Kotlin can have a **primary constructor** and one or more **secondary constructors**. The primary constructor is part of the class header: it goes after the class name (and optional type parameters).

```kotlin
class Person constructor(firstName: String) { /*...*/ }
```

If the primary constructor does not have any annotations or visibility modifiers, the _constructor_ keyword can be omitted:

```kotlin
class Person(firstName: String) { /*...*/ }
```

### Declaring Properties

### Getters and Setters

The initializer, getter and setter are optional. Property type is optional if it can be inferred from the initializer (or from the getter return type, as shown below).

rewrite `get` and `set` method.

```kotlin
class Person(val firstName: String, val lastName: String) {
    var nickName: String? = null
        set(value) {
            field = value
            println("the new nickname is $value")
        }
        get() {
            println("the returned value is $field")
            return field
        }

  // basic method
    fun printInfo() {
        val nickNameToPrint = nickName ?: "no nickname"
        println("$firstName ($nickNameToPrint) $lastName")
    }
}
```

## Basic Types

> In Kotlin, everything is an object in the sense that we can call member functions and properties on any variable. Some of the types can have a special internal representation - for example, numbers, characters and booleans can be represented as primitive values at runtime - but to the user they look like ordinary classes. In this section we describe the basic types used in Kotlin: numbers, characters, booleans, arrays, and strings.

### Numbers

integer numbers

| Type  | Size (bits) | Min value                         | Max value                           |
| :---- | :---------- | :-------------------------------- | :---------------------------------- |
| Byte  | 8           | -128                              | 127                                 |
| Short | 16          | -32768                            | 32767                               |
| Int   | 32          | -2,147,483,648 (-231)             | 2,147,483,647 (231 - 1)             |
| Long  | 64          | -9,223,372,036,854,775,808 (-263) | 9,223,372,036,854,775,807 (263 - 1) |

floating-point numbers

| Type   | Size (bits) | Significant bits | Exponent bits | Decimal digits |
| :----- | :---------- | :--------------- | :------------ | :------------- |
| Float  | 32          | 24               | 8             | 6-7            |
| Double | 64          | 53               | 11            | 15-16          |

## References

https://kotlinlang.org/docs/reference/basic-syntax.html

https://kotlinlang.org/docs/reference/basic-types.html

https://kotlinlang.org/docs/reference/functions.html

https://www.youtube.com/watch?v=F9UC9DY-vIU
