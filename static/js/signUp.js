$(function() {
    $('#btnSignUp').click(function() {
	console.log("This is working so far");
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
	   
            success: function(response) {
		console.log(response);
                document.getElementById('yourname').innerHTML = JSON.parse(response)['yourpokename'];
		document.getElementById('yourtype1').innerHTML = JSON.parse(response)['yourpoketype1'];
		document.getElementById('yourtype2').innerHTML = JSON.parse(response)['yourpoketype2'];
		document.getElementById('yourinfo').style.display = "block";

		document.getElementById('enemyname').innerHTML = JSON.parse(response)['enemypokename'];
		document.getElementById('enemytype1').innerHTML = JSON.parse(response)['enemypoketype1'];
		document.getElementById('enemytype2').innerHTML = JSON.parse(response)['enemypoketype2'];
		document.getElementById('enemyinfo').style.display = "block";
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});


