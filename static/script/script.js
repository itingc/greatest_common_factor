$(function(){
    $('button').click(function(){
        $.ajax({
            url: '/gcf_result',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                $('#result').text(`GCF = ${response["GCF"]}`);
            },
            error: function(response) {
                $('#result').text("The numbers must be positive integer");
            }
        });
    });
});

