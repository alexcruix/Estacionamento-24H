let inputs = document.getElementsByClassName('input-form');
for (let input of inputs) {
    input.addEventListener("blur", function() {
        if(input.value.trim() != ""){
            input.classList.add("has-val");
        } else {
            input.classList.remove("has-val");
        }
    });
}

    let form = document.getElementsById('login-form');
form.addEventListener("submit", function(event) {
    let inputs = document.getElementsByClassName('input-form');
    for (let input of inputs){
        if(input.value.trim() == ""){
            input.parantElement.classList.add("wrap-input-invalid");
}
}
event.preventDefault();
});