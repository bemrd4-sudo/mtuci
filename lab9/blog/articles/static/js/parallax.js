// ждем загрузки
$(document).ready(function() {
    
    // сколько проскроллили
    var scrolled = 0;
    
    // иконки и логотип
    var $icons = $('.parallax-icons img');
    var $logo = $('.logo');
    
    console.log("параллакс запущен, иконок: " + $icons.length);
    
    // при скролле
    $(window).scroll(function() {
        scrolled = $(window).scrollTop();
        
        // двигаем иконки с разной скоростью
        for (var i = 0; i < $icons.length; i++) {
            var speed = 0.1 * (i + 1);  // 0.1, 0.2, 0.3
            var yPos = scrolled * speed;
            $icons.eq(i).css('top', yPos + 'px');
        }
        
        // логотип
        var logoY = scrolled * 0.6;
        $logo.css('top', logoY + 'px');
    });
    
    console.log("эффект параллакса работает");
});