
var description = document.getElementsByClassName('skills_legend__container');
console.log(description);

var description = description.item(0);
console.log(description);


var jason_link = document.getElementsByClassName('jason_link');
var jason_link = jason_link[0];


description.style['visibility'] ='hidden';
description.style['opacity'] = '0%';
description.style['margin-bottom'] = '-10%';

jason_link.style['display'] = 'none'
jason_link.style['visibility'] = 'hidden';
jason_link.style['opacity'] = '0%';
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
    console.log(jason_link);
    console.log(jason_link.style);

    if (jason_link.style['display'] === 'none') { 
        jason_link.style['display'] = 'flex';
        jason_link.style['visibility'] = 'visible';
        description.style['background-color'] = 'transparent'
        jason_link.style['opacity'] = '100%';
        jason_link.style['margin-bottom'] = '10%';

    } else if (jason_link.style['display'] === 'flex') {
        jason_link.style['display'] = 'none';
        jason_link.style['visibility'] = 'hidden';
        description.style['background-color'] = 'transparent';
        jason_link.style['opacity'] = '0%';
        jason_link.style['margin-bottom'] = '-10%';
    }
}
