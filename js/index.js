if (localStorage.getItem("token") == null){
    alert("Você precisa estar logado para acessar essa página");
    window.location.href = "../signin.html";
}

let userLogado = JSON.parse(localStorange.getItem("userLogado"));

let logado = document.querySelector("logado");
logado.innerHTML = 'Olá ${userLogado.nome}';

function sair() {
    localStorage.removeItem("token");
    localStorage.removeItem("userLogado");
    window.location.href = "../signin.html";
}


$(document).ready(function(){
    $(".menu").click(function(){
        $(".keep").toggleClass("width");
    });
});