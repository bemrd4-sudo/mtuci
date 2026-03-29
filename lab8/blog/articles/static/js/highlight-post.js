// ждем загрузки страницы и jQuery
$(document).ready(function() {
    
    console.log("jQuery версия: " + $.fn.jquery);
    console.log("постов найдено: " + $('.one-post').length);
    
    // эффект тени при наведении
    $('.post').hover(
        function() {
            // плавно показываем тень
            $(this).find('.post-shadow').stop().animate({
                opacity: 0.15
            }, 300);
            console.log("тень появилась");
        },
        function() {
            // плавно убираем тень
            $(this).find('.post-shadow').stop().animate({
                opacity: 0
            }, 300);
            console.log("тень исчезла");
        }
    );
    
    console.log("эффект подсветки готов");
});