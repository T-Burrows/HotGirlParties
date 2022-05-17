

// function atLeastOneRadio() {
//     var checked_level = document.querySelector('input[name = "level"]:checked');
//     console.log('checked');
//     if(checked_level == null){  //Test if something was checked
//     alert("Please select your role"); //Alert, nothing was checked.
//     }
// }


// var radios = document.querySelector('input[name = "level]');
// function validate(element){
//     var checked = False;
//     for (var i = 0; i < radios.length; i++) {
//         if (radios[i].type === 'radio' && radios[i].checked) {
//             checked = True;      
//         }
//     }
//     if (checked = False) {
//         alert("Please select your role");
//     }
// }

function over(element) {
    element.style.backgroundColor = "lime";    
}
    
function out(element) {
    element.style.backgroundColor = "silver";   
}