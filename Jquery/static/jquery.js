$(document).ready(function(){
    $('#jquery').click(function(){
        var data = {
            'nome_aluno':$('#name').val(),
            'email':$('#email').val(),
            };
            $.ajax({
                type: 'POST',
                url: '/api/retorno',
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify(data),
                success: function(callback) {
                    $("#resposta").html("<br>" + callback.nome_aluno +"<br>" + callback.email)
                },
                error: function() {
                    $(this).html("error!");
                }
            });
        });
});