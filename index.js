const JASON_BOX = document.getElementById('jason_description-legend');
const ME_AND_WHO_IAM_BOX = document.getElementById('me_and_who_iam_description-legend')

console.log(JASON_BOX);


function alter_box_description(name) {
    var box = document.getElementById(name);
    console.log('obtendo -> ', box);

    console.log('Opacidade', JASON_BOX.style['opacity']);
    if (JASON_BOX.style['opacity'] == '0') {
        console.log('ligado');
        box.style['background'] = 'blue'
        box.style['scale'] = '1.2'
        JASON_BOX.style['opacity'] = '100';

    } else {
        console.log('desligado');
        box.style['background'] = 'var(--aqua-default)'
        box.style['scale'] = '1'
        JASON_BOX.style['opacity'] = '0';
    }
}