# React 基础笔记

## About React

virtual DOM is a lightweight in-memory representation of UI.

## Composing Components

### Passing data to components

使用 this.props 来获取父组件传递的数据

use this.props to passing data from father components to child components.

```javascript
// counters.jsx
<Counter key={counter.id} value={counter.value}>
	<h4>Dialog</h4>
</Counter>

// counter.jsx
render() {
  console.log("props", this.props);
  ...
}
// {value: 4, children: {…$$typeof:{React Element}, type:'h4'}}

// use **this.props.children** to get references
render(){
	{this.props.children}
}
```

### State vs Props

```javascript
// **state** is private, local and internal to that component,
// invisible to other components.

// **props** is read-only, so we need to put props to it's local state
// if we want to modify it.
state = {
  value: this.props.value,
};
```

### Raising and handling events

子组件引发一个事件，由父组件处理此事件

child component raising an event, and father component handling this event.

```javascript
// call handler in father components via **props**
// counters.jsx
handleDelete = () => {
    console.log("Event Handler Called");
	};

render() {
    return (
      <div>
        {this.state.counters.map(counter => (
          <Counter
            onDelete={this.handleDelete}
          />
        ))}
      </div>
    );
}
```

​

```javascript
// counter.jsx
render() {
    return (
        <div>
          <button
            onClick={this.props.onDelete}
            className="btn btn-danger btn-sm m-2"
          >
            Delete
          </button>
        </div>
    );
}
```

### Update State

我们不直接修改 state 的值，而使用 setState 方法来更新 state

we don't update state directly, we use **setState** method to update the state.

```javascript
handleDelete = (counterId) => {
  // create a new array except the counter that delete button is clicked.
  const counters = this.state.counters.filter((c) => c.id !== counterId);
  // overwrite the value
  this.setState({ counters: counters });
};
```

### Single source of truth

remove the state from child component, and only rely under props to receive the data that component need. we refer this kind of component as controlled component.(doesn't have it's local state, receive all data via props, and raises events when data needs to be changed, so the component is entirely controlled by it's parent. )

```javascript
class Counter extends Component {
  render() {
    return (
      <React.Fragment>
        <div>
          <button
            onClick={() => this.props.onIncrement(this.props.counter)}
            className="btn btn-secondary btn-sm"
          >
            Increment
          </button>
      </React.Fragment>
    );
  }
}
```

### Stateless functional components

Stateless Functional Component rather than Class Component, without local state.

note Stateless Functional Component don't have **this.props**, we have to pass data use parameter **props.**

```javascript
// navbar.jsx
const NavBar = (props) => {
  return (
    <nav className="navbar navbar-light bg-light">
      <a className="navbar-brand" href="#">
        Navbar{" "}
        <span className="badge badge-pill badge-secondary">
          {props.totalCounters}
        </span>
      </a>
    </nav>
  );
};
```

### Destructing arguments

use destructing to simplify the code.

```javascript
// counter.jsx
render() {
    const { onIncrement, onDelete, counter } = this.props;
    return (
      <React.Fragment>
        <div>
          <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
          <button
            onClick={() => onIncrement(counter)}
            className="btn btn-secondary btn-sm"
          >
            Increment
          </button>
          <button
            onClick={() => onDelete(counter.id)}
            className="btn btn-danger btn-sm m-2"
          >
            Delete
          </button>
        </div>
      </React.Fragment>
    );
  }
```

### Lifecycle Hooks

these are mainly used lifecycle hooks:

1. **MOUNT:** constructor, render, componentDidMount. (when the component is created)

2. **UPDATE:** render, componentDidMount (when the state or props of component is changed)

3. **UNMOUNT**:componentWillUnmount (when the component is removed from the DOM)

```javascript
class App extends Component {
  state = {};

constructor(props){
  super(props);
  this.state = props;
}

// this method will call after rendered
// best place to add ajax call to server
componentDidMount(){
  //Ajax Call
  // data = ...
  this.setState({ data })
}
render() {
  return ();
}
}
```

note:

1. when a component is rendered, all its children are also rendered recursively.
2. you can only use lifecycle hooks in class components.

```javascript
componentDidUpdate(prevProps, prevState) {
    if (prevProps.counter.value !== this.props.counter.value) {
      // Ajax call and get new data from the server
    }
  }
```

## ECMAScript 6 new features

作用域(scope):

    const → block
    let → block
    var → function

使用优先级：const > let > var, 只有在充分的理由下我们才使用 var。

priority: const > let > var, only use var when have valid reason.

```javascript
const person = {
  name: "Alex",
  walk() {
    console.log(this);
  },
};
```

const 变量不能被重新赋值，但其成员可以被重新赋值。

const can't be reassigned, but its members can be reassigned.

```javascript
person.name = "Embers";

console.log(person.name);
// Embers
```

### this

```javascript
// obj.method() -> this === obj
// function() -> this === window || this === undefined (on strict mode)
```

如果函数作为对象的方法被调用，this 会返回当前对象的引用。

if we call a function as **method** in one object, **this** will return the references to the current object.

```javascript
person.walk();
//{name: "Embers", walk: ƒ}
```

如果函数作为一个独立的对象或在对象外的函数被调用，this 会返回 broswer 中的全局对象 window，在严格模式下则会返回 undefined.

if we call a function as a standalone object or outside of an object this will return the global object, which is the **window** object in browser, and in strict mode returns undefined.

```javascript
const walk = person.walk;
walk();
// undefined
```

javascript 的函数是对象，包含属性和方法供我们使用。使用 bind() 方法可以获取对象的引用。

Functions in javascript is objects, they have properties and methods we can use. use bind() method can get the references of object.

```javascript
const walk = person.walk.bind(person);
walk();
```

### 箭头函数

箭头表示使函数更加清晰。

arrow functions is clearer.

```javascript
const jobs = [
  { id: 1, isActive: true },
  { id: 2, isActive: true },
  { id: 3, isActive: false },
];

const activateJobs = jobs.filter((job) => job.isActive);
```

箭头函数不会重新绑定 this 关键字，它会继承 this 关键字。

```javascript
arrow functions don't rebind this keyword, it will inherit the this keyword.

// normal function
const man = {
  talk() {
    setTimeout(function() {
      console.log(this);
    }, 1000);
  }
};

man.talk();
// Window {parent: Window, opener: null, top: Window, length: 0, frames: Window, …}
// setTimeout callback function is not part of any objects.

// arrow function
const man = {
  talk() {
    setTimeout(() => console.log(this), 1000);
  }
};

man.talk();
// {talk: ƒ}
```

### 实用函数: Array.map()

```javascript
const colors = ["red", "green", "blue"];
const items = colors.map((color) => `<li>${color}</li>`);
console.log(items);
// ["<li>red</li>", "<li>green</li>", "<li>blue</li>"]

// template literal: `<li>${color}</li>` equal to "<li>" + color + "</li>"
```

### Object destructing

```javascript
const address = {
  street: "some street",
  city: "some city",
  country: "some country",
};

const street = address.street;
const city = address.city;
const country = address.country;

// equal to
const { street, city, country } = address;

// and also can set an alias
const { street: st } = address;
console.log(st);
// some street
```

### Spread operator

spread operator is ...

to concat array:

```javascript
const first = [1, 2, 3];
const second = [4, 5, 6];

const combined = first.concat(second);
// equal to
const combined1 = [...first, ...second];
// it can also insert more elements
const combined2 = [...first, "a", ...second, "b"];

// and a easy way to clone an array
const clone = [...first];
console.log(clone);
```

concat objects:

```javascript
const first = { name: "Alex" };
const second = { job: "student" };
const combined = { ...first, ...second, location: "China" };
console.log(combined);
// {name: "Alex", job: "student", location: "China"}

// and a easy way to clone an object
const clone = { ...first };
console.log(clone);
```

### Classes

类是创建该类型对象的蓝图。

the blueprint to create objects of that type.

```javascript
class Person {
  constructor(name) {
    this.name = name;
  }
  walk() {
    console.log(this);
  }
}

const person = new Person("Alex");
```

### Inheritance

```javascript
class Teacher extends Person {
  constructor(name, degree) {
    // have to call super() to use father constructor
    super(name);
    this.degree = degree;
  }
  teach() {
    console.log("teach");
  }
}

const teacher = new Teacher("Alex", "Science");
```

### Modules

from ES6 we have concept of modules natively in javascript.

引入模块的概念是为了**模块化** **modularize**

模块默认是私有的，要让其成为公有的需要 export 到外部才可被其他模块导入。

module is default private. to make it public we need to export the class to the outside.

```javascript
// person.js
export class Person {
  constructor(name) {
    this.name = name;
  }
  walk() {
    console.log(this);
  }
}

// index.js
import { Person } from "./person";

const person = new Person("Alex");
person.walk();
```

### Named and default exports

```javascript
// Default -> import ... from "";
// Named -> import { ... } from "";

// teacher.js

export function promote() {}

export default class Teacher{
	...
}

// index.js
import Teacher, { promote } from "./teacher";

...
```

### For ... in & for ... of

[for in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in) loops over enumerable property names of an object.

[for of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)(new in ES6) does use an [object-specific *iterator*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) and loops over the values generated by that.

```javascript
var arr = [3, 5, 7];
arr.foo = "hello";

for (var i in arr) {
  console.log(i); // logs "0", "1", "2", "foo"
}

for (var i of arr) {
  console.log(i); // logs "3", "5", "7"
  // it is does not log "3", "5", "7", "hello"
}
```

### References Course:

[React Tutorial - Learn React - React Crash Course [2019]](https://www.youtube.com/watch?v=Ke90Tje7VS0&list=RDCMUCWv7vMbMWH4-V0ZXdmDpPBA&start_radio=1&t=566)

[JavaScript for React Developers | Mosh](https://www.youtube.com/watch?v=NCwa_xi0Uuc)

## Bug 修复及设置

遇到 "gyp: No Xcode or CLT version detected!" 问题描述及解决方法：

[npm install fails on node-gyp rebuild with "gyp: No Xcode or CLT version detected!" · Issue #7 · schnerd/d3-scale-cluster](https://github.com/schnerd/d3-scale-cluster/issues/7#issuecomment-550579897)

this.props.data.length always return 0:

[React prop array length returning 0](https://stackoverflow.com/questions/42986404/react-prop-array-length-returning-0)

npm set Proxy:

```bash
npm config set proxy http://proxy.company.com:<port>
npm config set https-proxy http://proxy.company.com:<port>
```

npm show global installed packages:

```bash
npm list -g --depth 0
```

## Pic Tools

[Lorem Picsum](https://picsum.photos/)

# Code Style Guide

We largely follow Airbnb's React/JSX Style Guide:

[airbnb/javascript](https://github.com/airbnb/javascript/tree/master/react)
