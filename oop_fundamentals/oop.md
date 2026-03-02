# Object-Oriented Programming — Quick Refresher

## What is OOP?

Object-Oriented Programming (OOP) models software as a collection of objects that hold data and provide behavior (methods). An object groups state (data) and the functions that operate on that state.

## Why prefer OOP?

- Useful for large codebases and complex domains.
- Encourages encapsulation, which eases maintenance and reduces unintended coupling.
- Supports reuse via inheritance and flexible behavior via polymorphism.

## What is a class?

- A class is a user-defined data type that bundles data members and member functions.
- It acts as a template for creating objects (instances) with common properties and methods.

## What is an object?

An object is an instance of a class. You typically create an object by calling the class as a constructor.

Example (Python):

```python
class Student:
	def __init__(self, name=""):
		self.name = name

# create object
student1 = Student()
student1.name = "Rahul"
print("student1.name:", student1.name)
```

## Main features of OOP

**Encapsulation**

Binding data and methods into a single unit (class). Encapsulation hides internal state and exposes a clear interface.

Small example (Python "private" attribute by convention):

```python
class BankAccount:
	def __init__(self, balance=0):
		self._balance = balance  # "protected" by convention

	def deposit(self, amount):
		self._balance += amount

	def get_balance(self):
		return self._balance
```

**Data Abstraction**

Expose only necessary details. For example, a `Car` object offers methods like `accelerate()` without exposing transmission internals.

**Polymorphism**

Allow the same operation to behave differently for different types or contexts.

Compile-time polymorphism (overloading) — languages like C++/Java support method overloading. Python does not do static overloading in the same way; operator overloading is possible:

```python
class Vec:
	def __init__(self, x, y):
		self.x, self.y = x, y

	def __add__(self, other):
		return Vec(self.x + other.x, self.y + other.y)

v1 = Vec(1, 2)
v2 = Vec(3, 4)
v3 = v1 + v2  # uses __add__
```

Run-time polymorphism (overriding) — a base reference calls overridden methods on concrete subclasses:

```python
class Animal:
	def speak(self):
		return "(generic sound)"

class Dog(Animal):
	def speak(self):
		return "Bark"

class Cat(Animal):
	def speak(self):
		return "Meow"

def animal_sound(a: Animal):
	print(a.speak())

animal_sound(Dog())  # Bark
animal_sound(Cat())  # Meow
```

**Inheritance**

Mechanism to derive a new class from an existing one to reuse and extend behavior.

Example (Python):

```python
class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		return f"{self.name} makes a sound."

class Dog(Animal):
	def __init__(self, name, breed):
		super().__init__(name)
		self.breed = breed

	def speak(self):
		return f"{self.name}, the {self.breed}, barks."

class Cat(Animal):
	def speak(self):
		return f"{self.name} meows."
```

## Access specifiers

- Public: accessible from anywhere.
- Private: restricted to the defining class (in languages like C++/Java). In Python, use name-mangling (`__name`) or conventions (`_name`).
- Protected: accessible within class and subclasses (language-dependent semantics).

Example (C++-style, illustrative):

```cpp
class Example {
public:
	int pub;
private:
	int priv;
};
```

## Overloading vs Overriding

- Overloading: same name, different parameter lists (compile-time resolution in static languages).
- Overriding: subclass provides a new implementation for a base class method (runtime dispatch).

## Types of inheritance

- Single: one base, one derived.
- Multiple: a derived class with multiple bases (language-dependent).
- Multilevel: chain of inheritance (A -> B -> C).
- Hierarchical: multiple derived classes from one base.
- Hybrid: combination of the above.

## Interface vs Abstract Class (quick)

| Abstract Class | Interface |
|---|---|
| May contain concrete and abstract methods | Typically only method signatures (language-dependent) |
| Can have instance/state variables | Usually only static/final constants (language-dependent) |
| Often doesn't support multiple inheritance (language-dependent) | Can support multiple inheritance of type |

Example (Java-like pseudo):

```java
// interface
interface Flyable { void fly(); }

// abstract class
abstract class Vehicle {
	void start() { /* concrete */ }
	abstract void move();
}
```

In Python, use the `abc` module for abstract base classes when you need abstract methods.

---

This file is a concise reference — let me know if you want short diagrams, language-specific notes (Java/C++/Python), or a one-page printable cheat-sheet.

## Additional important concepts you might be missing

- SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion).
- Composition over inheritance — prefer composing objects with small, single-purpose components instead of deep inheritance hierarchies.
- Common design patterns: Factory, Singleton (use sparingly), Observer, Strategy, Decorator, Adapter.
- Dependency injection and inversion of control for testability.
- Cohesion & coupling: aim for high cohesion, low coupling.
- Immutability and value objects (helps reasoning and concurrency).
- Testing & mocking of object behavior (unit tests focus on public behavior).
- Concurrency/thread-safety concerns for shared mutable objects.
- Law of Demeter (talk to your immediate friends only) — reduces coupling.

Below is a very small example showing composition + the Strategy pattern (injecting behavior at runtime instead of subclassing):

```python
from abc import ABC, abstractmethod

class Formatter(ABC):
	@abstractmethod
	def format(self, text: str) -> str:
		pass

class PlainFormatter(Formatter):
	def format(self, text: str) -> str:
		return text

class HtmlFormatter(Formatter):
	def format(self, text: str) -> str:
		return f"<p>{text}</p>"

class Document:
	# Document composes a Formatter instead of inheriting different Document types
	def __init__(self, text: str, formatter: Formatter):
		self.text = text
		self.formatter = formatter

	def render(self) -> str:
		return self.formatter.format(self.text)

# usage
doc = Document("Hello", PlainFormatter())
print(doc.render())            # Hello
doc.formatter = HtmlFormatter()  # swap strategy at runtime
print(doc.render())            # <p>Hello</p>
```

Why this matters: instead of creating `HtmlDocument` and `PlainDocument` subclasses, we inject the formatting behaviour. This makes the code easier to test, extend, and combine (follows composition and Single Responsibility).

---

I implemented all three expansions below: SOLID principles (brief descriptions + tiny examples), a short gallery of common design patterns, and Java/C++ variants of the core examples in this file.

## SOLID principles (brief)

- Single Responsibility Principle (SRP): a class should have one reason to change.

	Example (Python):
	```python
	# violates SRP: both data storage and printing
	class Report:
			def __init__(self, data):
					self.data = data
			def save(self):
					pass
			def print(self):
					pass

	# SRP: separate responsibilities
	class ReportStorage:
			def save(self, data):
					pass
	class ReportPrinter:
			def print(self, data):
					pass
	```

- Open/Closed Principle (OCP): open for extension, closed for modification. Add behavior by extending, not modifying existing code.

	Example (Python using polymorphism):
	```python
	class Shape: 
			def area(self):
					raise NotImplementedError
	class Circle(Shape):
			def area(self):
					return 3.14 * 1 * 1
	# add more shapes without changing code that consumes Shape
	```

- Liskov Substitution Principle (LSP): subclasses must be substitutable for their base types.

	Note: classic Rectangle/Square counterexample shows violating LSP when subclass changes expected behavior.

- Interface Segregation Principle (ISP): prefer many small, client-specific interfaces over a single large interface.

	Example (conceptual): split `Printer` into `Printable` and `Scannable` instead of one fat `AllInOne` interface.

- Dependency Inversion Principle (DIP): high-level modules should depend on abstractions, not concrete implementations.

	Example (Python):
	```python
	class Logger:
			def log(self, msg):
					raise NotImplementedError
	class ConsoleLogger(Logger):
			def log(self, msg):
					print(msg)
	class Service:
			def __init__(self, logger: Logger):
					self.logger = logger
			def run(self):
					self.logger.log('running')
	```

## Design patterns (short gallery)

- Factory: create objects via a factory function/class instead of direct constructors. (Useful for encapsulating creation logic.)

	One-line example (Python): `shape = ShapeFactory.create('circle')`

- Singleton: single shared instance (use sparingly; often better solved via dependency injection).

	One-line example: `logger = Logger.get_instance()`

- Observer: publish/subscribe; observers register and get notified on changes.

	One-line example: `subject.subscribe(observer)`

- Strategy: inject interchangeable behavior at runtime (we already showed this with `Formatter`).

- Decorator: wrap objects to add behavior without modifying them.

	One-line example: `logged = LoggingDecorator(service)`

- Adapter: convert one interface to another so incompatible types can work together.

	One-line example: `adapter = UsbToSerialAdapter(usb_device)`

- Facade: provide a simplified interface over a complex subsystem.

	One-line example: `payment = PaymentFacade.process(order)`

- Builder: step-by-step construction of complex objects.

	One-line example: `car = CarBuilder().with_engine(e).build()`

## Java and C++ variants of select examples

Below are concise translations of the earlier examples (Student, BankAccount, Vec add/operator, Animal polymorphism, Strategy/Document).

Student (Java):

```java
public class Student {
		public String name = "";
		public static void main(String[] args) {
				Student s = new Student();
				s.name = "Rahul";
				System.out.println(s.name);
		}
}
```

Student (C++):

```cpp
#include <iostream>
#include <string>
struct Student { std::string name; };
int main(){ Student s; s.name = "Rahul"; std::cout<<s.name<<"\n"; }
```

BankAccount (Java):

```java
public class BankAccount {
		private int balance = 0;
		public void deposit(int amount){ balance += amount; }
		public int getBalance(){ return balance; }
}
```

BankAccount (C++):

```cpp
class BankAccount {
	int balance = 0;
public:
	void deposit(int amount){ balance += amount; }
	int getBalance() const { return balance; }
};
```

Vec addition (C++ operator overloading):

```cpp
struct Vec { int x,y; Vec(int a,int b):x(a),y(b){} };
Vec operator+(const Vec &a, const Vec &b){ return Vec(a.x+b.x, a.y+b.y); }
```

Vec addition (Java — no operator overloading):

```java
class Vec { int x,y; Vec(int x,int y){this.x=x;this.y=y;} Vec add(Vec o){return new Vec(x+o.x,y+o.y);} }
```

Animal polymorphism (Java):

```java
class Animal { String speak(){ return "(generic)"; } }
class Dog extends Animal { @Override String speak(){ return "Bark"; } }
class Cat extends Animal { @Override String speak(){ return "Meow"; } }
```

Animal polymorphism (C++):

```cpp
struct Animal { virtual std::string speak(){ return "(generic)"; } };
struct Dog : Animal { std::string speak() override { return "Bark"; } };
struct Cat : Animal { std::string speak() override { return "Meow"; } };
```

Strategy/Document (Java):

```java
interface Formatter { String format(String s); }
class PlainFormatter implements Formatter { public String format(String s){ return s; } }
class HtmlFormatter implements Formatter { public String format(String s){ return "<p>"+s+"</p>"; } }
class Document { String text; Formatter f; Document(String t, Formatter f){this.text=t;this.f=f;} String render(){ return f.format(text);} }
```

Strategy/Document (C++):

```cpp
struct Formatter { virtual std::string format(const std::string &s)=0; virtual ~Formatter()=default; };
struct PlainFormatter: Formatter { std::string format(const std::string &s) override { return s; } };
struct HtmlFormatter: Formatter { std::string format(const std::string &s) override { return "<p>"+s+"</p>"; } };
// Document holds a pointer to Formatter and delegates render()
```


