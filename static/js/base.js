$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();
    setTimeout(function() {
        $('.messages').fadeOut('fast');
    }, 3000);
});


