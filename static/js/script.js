document.getElementById("form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let word = document.getElementById("wordInput").value.toUpperCase();
    
    // Verificar se a palavra contém espaços
    if (word.includes(" ")) {
        alert("A palavra não pode conter espaços.");
        return;  // Impede que o restante do código seja executado
    }

    let resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "";  // Limpar resultados anteriores

    for (let i = 0; i < word.length; i++) {
        let letter = word[i];
        let img = document.createElement("img");
        img.src = `/static/letras/${letter}.png`;  // Caminho das imagens
        img.alt = letter;
        img.onerror = function() { this.style.display = "none"; };  // Oculta caso não exista
        resultDiv.appendChild(img);
    }
});
