'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

let target = document.getElementById("target");
let student_array = [];
for (let i = 0; i < students.length; i++){
  student_array[i] = document.createElement("option");
  student_array[i].value = students[i]
}
