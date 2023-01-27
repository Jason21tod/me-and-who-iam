const JASON_BOX = document.getElementById('jason_description-legend');
const ME_AND_WHO_IAM_BOX = document.getElementById('me_and_who_iam_description-legend')

console.log(JASON_BOX);


function alter_box_description(activation_box, description_box) {
    var box = document.getElementById(activation_box);
    var description = document.getElementById(description_box);
    console.log('obtendo -> ', box);
    console.log('obtendo -> ', description);

    console.log('Opacidade', description.style['opacity']);
    if (description.style['opacity'] == '0') {
        console.log('ligado');
        box.style['background'] = 'blue'
        box.style['scale'] = '1.2'
        description.style['opacity'] = '100';
        description.style['display'] = 'flex'

    } else {
        console.log('desligado');
        box.style['background'] = 'var(--aqua-default)'
        box.style['scale'] = '1'
        description.style['opacity'] = '0';
        description.style['display'] = 'none'
    }
}