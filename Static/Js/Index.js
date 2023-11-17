$(document).ready(function(){
    $("#loginForm").on('submit', function(e){
        e.preventDefault();

        var correo = $("#correo").val();
        var passwd = $("#passwd").val();

        $.ajax({
            url: login_url,
            method: "POST",
            data: {correo: correo, passwd: passwd},
            success: function(response, textStatus, xhr){
                if(xhr.status === 200 && response.redirect){
                    window.location.href = response.redirect;
                }else{
                    alert("Invalid credentials. Please try again.");
                }
            }            
        });
    });
});


