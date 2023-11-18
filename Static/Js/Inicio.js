$(document).ready(function () {
    $(".menu_hamburguesa img").click(function () {
        $(".opciones ul").toggleClass("show");
        $("body").toggleClass("menu_abierto");
    });
});