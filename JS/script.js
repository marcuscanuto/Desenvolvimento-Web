function gritar(){
    alert("GANHOUUUUUUUUUUUUUUU")
}

function perguntar(){

    var nome;
    nome = prompt("Qual seu nome ?")
    alert("Seja bem vindo " + nome)

}

function mudar_texto(){
    // document.getElementsByTagName("h1") -> pega todos as tag h1 do documento e coloca na variável h1
    var h1 = document.getElementsByTagName("h1")

    // especifica que quer somente o primeiro h1
    h1[0].innerHTML = "Você ganhou 200 reais para sua próxima aposta"
}

function incrementar(){
    // document.getElementById("p0") -> pega pelo id único
    var p0 = document.getElementById("p0")
    if(p0.innerHTML == 20){
        p0.innerHTML = 0
    } else {
    p0.innerHTML = parseInt(p0.innerHTML) + 1
    }

}