// список студентов (как в первой лабе)
var students = [
    {name:"Оксана", group:"2256", age:19, marks:[4, 3, 5, 5, 4]},
    {name:"Настя", group:"2257", age:18, marks:[3, 2, 3, 4, 3]},
    {name:"Кирилл", group:"2255", age:19, marks:[3, 5, 4, 3, 5]},
    {name:"Дима", group:"2258", age:18, marks:[5, 5, 5, 4, 5]},
    {name:"Александр", group:"2255", age:18, marks:[3, 4, 5, 4, 5]}
];

// функция для добавления пробелов
function pad(str, len) {
    str = str.toString();
    while(str.length < len) str += ' ';
    return str;
}

// вывод всех
function showAll() {
    console.log(pad("имя",15), pad("группа",8), pad("возраст",8), pad("оценки",20));
    for(var i=0; i<students.length; i++) {
        var s = students[i];
        console.log(pad(s.name,15), pad(s.group,8), pad(s.age,8), pad(s.marks,20));
    }
}

// фильтр по группе
function filterByGroup(group) {
    var res = [];
    for(var i=0; i<students.length; i++) {
        if(students[i].group == group) res.push(students[i]);
    }
    return res;
}

// тесты
console.log("все студенты:");
showAll();

console.log("группа 2255:");
var g1 = filterByGroup("2255");
for(var i=0; i<g1.length; i++) {
    console.log(g1[i].name, g1[i].group);
}

console.log("группа 2256:");
var g2 = filterByGroup("2256");
for(var i=0; i<g2.length; i++) {
    console.log(g2[i].name, g2[i].group);
}

console.log("группа 2257:");
var g3 = filterByGroup("2257");
for(var i=0; i<g3.length; i++) {
    console.log(g3[i].name, g3[i].group);
}

console.log("группа 2258:");
var g4 = filterByGroup("2258");
for(var i=0; i<g4.length; i++) {
    console.log(g4[i].name, g4[i].group);
}