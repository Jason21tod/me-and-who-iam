


var description = document.getElementsByClassName('skills_legend__container');
console.log(description);

var description = description.item(0);
console.log(description);


var jason_link = document.getElementsByClassName('jason_link');
var jason_link = jason_link[0];

var portifolio = document.getElementsByClassName('portifolio_description');
var portifolio = portifolio[0];


function normalizeDescripitions (element) {

    element.style['display'] = 'none'
    element.style['visibility'] = 'hidden';
    element.style['opacity'] = '0%';
    element.style['margin-bottom'] = '-10%';
}


description.style['visibility'] ='hidden';
description.style['opacity'] = '0%';
description.style['margin-bottom'] = '-10%';



normalizeDescripitions(jason_link);
normalizeDescripitions(portifolio);

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
};


function toggleContainer (container) {
    console.log(container);
    console.log(container.style);

    if (container.style['display'] === 'none') { 
        container.style['display'] = 'flex';
        container.style['visibility'] = 'visible';
        container.style['background-color'] = 'transparent'
        container.style['opacity'] = '100%';
        container.style['margin-bottom'] = '10%';

    } else if (container.style['display'] === 'flex') {
        container.style['display'] = 'none';
        container.style['visibility'] = 'hidden';
        container.style['background-color'] = 'transparent';
        container.style['opacity'] = '0%';
        container.style['margin-bottom'] = '-10%';
    }
};
