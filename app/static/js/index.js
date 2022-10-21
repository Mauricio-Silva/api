document.getElementById('SaveStudentModalBtn').addEventListener('click', () => {
    if (document.getElementById('CreateName').value != '') {
        btn = document.getElementById('SaveStudentModalBtn');
        btn.setAttribute('data-bs-dismiss', 'modal');
        btn.click();
    } 
});
document.getElementById('UpdateStudentModalBtn').onclick = () => {
    if (document.getElementById('CreateName').value != '') {
        btn = document.getElementById('UpdateStudentModalBtn');
        btn.setAttribute('type', 'submit');
        btn.click();
    } 
}



function deleteNameModal(name) {
    document.getElementById('DeleteName').value = name;
}
function updateNameModal(name) {
    document.getElementById('UpdateOldName').value = name;
}
function checkSimilarNames() {
    old_name = document.getElementById('UpdateOldName').value;
    new_name = document.getElementById('UpdateNewName').value;
    new_name = new_name.replace( /\s/g, '')
    if (old_name == new_name) {
        document.getElementById('newNameHelp').style.display = 'block';
    }
    else {
        document.getElementById('newNameHelp').style.display = 'none';
    }
}


