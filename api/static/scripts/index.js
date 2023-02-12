const JASON_BOX = document.getElementById('jason_description-legend');
const ME_AND_WHO_IAM_BOX = document.getElementById('me_and_who_iam_description-legend')

console.log(JASON_BOX);


var activation = false;

function alter_box_description(activation_box, description_box) {
    var box = document.getElementById(activation_box);
    var description = document.getElementById(description_box);
    console.log('obtendo -> ', box);
    console.log('obtendo -> ', description);

    if (activation == false) {
        console.log('Activation state ', activation, 'Activating...');
        description.style['transition'] = 'all 1s ease 0s;'
        box.style['background'] = 'blue';
        description.style['opacity'] = '100';
        description.style['display'] = 'flex';
        activation = true;
        
    } else if (activation == true) {
        console.log('Activation state ', activation, 'off...');
        description.style['transition'] = 'all 1s ease 0s;'
        box.style['background'] = 'var(--aqua-default)';
        description.style['opacity'] = '0';
        description.style['display'] = 'none'
        activation = false
    }
}