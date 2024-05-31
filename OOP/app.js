// class is a blue print of how an object is created together with its attributes and behaviours(methods)
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

const john = new Person('John', 30);
john.greet();


const Joseph = new Student()
Joseph.name = 'Joseph';
Joseph.age = 25;
