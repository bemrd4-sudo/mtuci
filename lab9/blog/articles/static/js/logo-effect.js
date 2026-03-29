$(document).ready(function() {
    
    console.log("эффект для логотипа запущен");
    
    // при наведении на логотип
    $('.header img').hover(
        function() {
            // увеличиваем
            $(this).stop().animate({
                width: '200px'
            }, 300);
            console.log("логотип увеличился");
        },
        function() {
            // возвращаем обратно
            $(this).stop().animate({
                width: '150px'
            }, 300);
            console.log("логотип вернулся");
        }
    );
    
});