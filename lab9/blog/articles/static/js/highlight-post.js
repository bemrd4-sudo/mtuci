$(document).ready(function() {
    
    console.log("подсветка постов");
    
    $('.post').hover(
        function() {
            $(this).css('background', 'rgba(255,255,255,0.1)');
            $(this).css('border-radius', '10px');
        },
        function() {
            $(this).css('background', 'transparent');
        }
    );
    
});