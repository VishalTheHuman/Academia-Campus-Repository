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
        header.style.paddingTop = "30px";
    }
}
