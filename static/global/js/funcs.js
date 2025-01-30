function changeImage() {
    var botao = document.getElementById('exercise_button_image');
    if (botao.src.endsWith('global/images/ButtonUnclicked.png')) {
        botao.src = '{% static "global/images/ButtonClicked.png" %}';  // Troca para imagem2.png
    } else {
        botao.src = '{% static "global/images/ButtonUnclicked.png" %}';  // Troca para imagem1.png
    }
    console.log('oi');
}