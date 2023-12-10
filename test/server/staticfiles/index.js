function toggleForm() {
    var loginForm = document.querySelector('.login');
    var signupForm = document.querySelector('.signup');
    var header = document.querySelector("#logorsign");

    if (loginForm.style.display === 'none') {
        loginForm.style.display = 'block';
        signupForm.style.display = 'none';
        header.innerText = "Login"; 
        header.style.paddingTop = "90px";
    } else {
        loginForm.style.display = 'none';
        signupForm.style.display = 'block';
        header.innerText = "Sign Up"; 
        header.style.paddingTop = "50px";
        document.getElementById("teacherIdSection").style.display = "none";
        document.getElementById("rollNumberSection").style.display = "none";
    }
}

function showRollNumber() {
    var header = document.querySelector("#logorsign");
    document.getElementById("rollNumberSection").style.display = "block";
    document.getElementById("teacherIdSection").style.display = "none";
    header.style.paddingTop = "0px";
    header.style.marginTop ="20px";
    document.getElementById("teacher_id").innerText = "";
}

function showTeacherId() {
    var header = document.querySelector("#logorsign");
    document.getElementById("teacherIdSection").style.display = "block";
    document.getElementById("rollNumberSection").style.display = "none";
    header.style.paddingTop = "0px";
    header.style.marginTop ="20px";
    document.getElementById("roll_number").innerText = "";
}

function deselect(){
    var sr = document.getElementById("studentRadio")
    var tr = document.getElementById("teacherRadio")
    sr.checked = false;
    tr.checked = false;
}