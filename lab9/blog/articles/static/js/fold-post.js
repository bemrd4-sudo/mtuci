document.addEventListener("DOMContentLoaded", function() {
    
    var links = document.querySelectorAll('.fold-link');
    
    for (var i = 0; i < links.length; i++) {
        links[i].addEventListener('click', function(e) {
            var post = e.target.closest('.post');
            post.classList.toggle('folded');
            
            if (post.classList.contains('folded')) {
                e.target.textContent = 'развернуть';
            } else {
                e.target.textContent = 'свернуть';
            }
        });
    }
    
    console.log("кнопок сворачивания: " + links.length);
});