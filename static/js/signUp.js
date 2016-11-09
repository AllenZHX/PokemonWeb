$(function() {
    $('#btnSignUp').click(function() {
	console.log("This is working so far");
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
	   
            success: function(response) {
                document.getElementById('yourname').innerHTML = response;
		//document.getElementById('yourname').style.display = "block";
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});


