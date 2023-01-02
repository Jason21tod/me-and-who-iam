
var description = document.getElementsByClassName('skills_legend__container');
console.log(description);

var description = description.item(0);
console.log(description);

description.style['visibility'] ='hidden';
description.style['opacity'] = '0%';
description.style['margin-bottom'] = '-10%';


function toggleDescription () {
    
    var button = document.getElementsByClassName('skills_legend__container_icon');
    console.log(button);
    
    if (description.style['visibility'] === 'visible') {
        console.log('desligado');
        description.style['visibility'] ='hidden';
        description.style['opacity'] = '0%';
        description.style['margin-bottom'] = '-10%';
        
    } else if (description.style['visibility'] === 'hidden') {
        console.log('ligado');
        description.style['visibility'] = 'visible';
        description.style['background-color'] = '#000045';
        description.style['opacity'] = '100%';
        description.style['margin-bottom'] = '10%';
    }
}


function toggleJasonWpp () {
    var jason_image = document.getElementById('jason_wpp');

    if (jason_image.innerHTML.endsWith('<a class="jason_link" href="#"><img class="jason_image" src="static/css/jason.png" alt="jason logo"></a>')) {
        var jason_link = jason_image.getElementsByClassName('jason_link');
        jason_link.item(0).remove();
    }
    else {
        jason_image.insertAdjacentHTML("beforeend", '<a class="jason_link" href="#"><img class="jason_image" src="static/css/jason.png" alt="jason logo"></a>');
    };
}
