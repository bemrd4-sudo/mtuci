// ждем загрузки страницы
document.addEventListener("DOMContentLoaded", function() {
    
    // ищем все кнопки
    var links = document.getElementsByClassName("fold-link");
    
    // для каждой кнопки
    for (var i = 0; i < links.length; i++) {
        links[i].addEventListener("click", function(e) {
            
            // находим родительский пост
            var post = e.target.closest('.post');
            
            // переключаем класс
            post.classList.toggle('folded');
            
            // меняем текст
            if (post.classList.contains('folded')) {
                e.target.innerHTML = "развернуть";
            } else {
                e.target.innerHTML = "свернуть";
            }
        });
    }
    
    console.log("скрипт сворачивания готов, кнопок: " + links.length);
});