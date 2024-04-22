const SQL = require('./sql.js');
const sqlWasmUrl = './sql-wasm.wasm';

(async () => {
    if (!window.SQL) {
        window.SQL = SQL;
    }
    if (!window.SQL.Database) {
        const wasm = await SQL.Wasm.instantiate(await (await fetch(sqlWasmUrl)).arrayBuffer());
        SQL.Wasm = wasm;
    }
})();

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const emailInput = document.querySelector('input[name=email]');
    const passwordInput = document.querySelector('input[name=password]');

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (email === '' || password === '') {
            alert('Por favor, preencha todos os campos.');
            return;
        }

        // Conectando ao banco de dados
        const conn = new SQL.Database('estacionamento.db');

        // Consultando o usuário no banco de dados
        const sql = `SELECT * FROM usuarios WHERE email = ? AND senha = ?`;
        const stmt = conn.prepare(sql);
        const result = stmt.get(email, password);

        if (result) {
            alert('Login realizado com sucesso!');
            // Redirecionando para a página principal
            window.location.href = 'principal.html';
        } else {
            alert('Credenciais inválidas. Por favor, tente novamente.');
        }
    });
});

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

function updateFileName(input) {
    const file = input.files[0];
    const fileName = file.name || file.type;
    const fileInput = input.previousElementSibling;
    fileInput.innerHTML = fileName;
  }