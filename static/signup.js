$('#btnSignUp').click(function() {
    $.ajax({
        url: '/sign-up',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
});
