let button = document.querySelector('button');
let menu = document.getElementsByClassName('header_menu');
var solution = document.getElementsByClassName('what_i_do--solution')
let solution_array = Array.from(solution);

var problem = document.getElementsByClassName('what_i_do--problem')
let problem_array = Array.from(problem)

console.log('recebendo solution', solution_array);
console.log('recebendo problem', problem_array);


let button_state = false;

function turn_menu() {
    let my_menu = menu[0];
    console.log('-> menu: ', menu )
    console.log('-> botões: ', button);
    console.log(button_state);
    if (button_state) {
        button.style['backgroundColor'] = 'var(--background-color)'
        my_menu.style['left'] = '-100%'
        button_state = false;
    } else if (button_state == false) {
        button.style['backgroundColor'] = 'var(--blue-default)'
        my_menu.style['left'] = '0%'
        button_state = true;
    }
};


let toggle_problem_button = true
function toggle_problem_description () {
//     console.log(solution_array[0].style)
    if (toggle_problem_button) {
        solution_array.forEach((element) => {
            element.style['display'] = 'inline-block'
        });
        problem_array.forEach((element) => {
            element.style['display'] = 'none'
        })
        toggle_problem_button = false
        } 
    else {
        solution_array.forEach((element) => {
            element.style['display'] = 'none'
        });
        problem_array.forEach((element) => {
            element.style['display'] = 'inline-block'
        });
        toggle_problem_button = true
    }
};