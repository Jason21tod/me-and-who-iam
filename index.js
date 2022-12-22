



function toggleDescription () {
    
    var button = document.getElementsByClassName('skills_legend__container_icon');
    console.log(button);

    var description = document.querySelector('.skills_legend__container')
    console.log(description.getAttributeNames())

    if (description.style['visibility'] === 'visible') {
        console.log('desligado');
        description.style['visibility'] ='hidden';
        
    } else if (description.style['visibility'] === 'hidden') {
        console.log('desligado');
        description.style['visibility'] = 'visible';
        description.style['background-color'] = 'blue';
    }
}