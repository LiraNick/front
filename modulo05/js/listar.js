function carregar(){
    console.log('Carregando janela');
    var tbody = document.querySelector('tbody');
    tbody.innerHTML = ''

    var alunos = localStorage.getItem('Alunos');

    alunos = JSON.parse(alunos);
    
    alunos.forEach((e) =>{
    var tr = `<tr>
                    <td>${e['id']}</td>
                    <td>${e['nome']}</td>
                    <td>${e['cpf']}</td>
                    <td>${e['idade']}</td>
                    <td>
                    <a href="editar.html">editar</a>
                    </td>
                </tr>`

        tbody.innerHTML += tr
        
    });
}

window.onload = carregar