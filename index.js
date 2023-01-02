



function toggleDescription () {
    
    var button = document.getElementsByClassName('skills_legend__container_icon');
    console.log(button);

    var description = document.querySelector('.skills_legend__container')
    console.log(description.getAttributeNames())

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