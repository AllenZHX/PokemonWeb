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
		if(JSON.parse(response)['yourpoketype2'] == ""){
			document.getElementById('yourtype2').innerHTML = "NAN";
		}else{	
		document.getElementById('yourtype2').innerHTML = JSON.parse(response)['yourpoketype2'];
		}
		document.getElementById('yourinfo').style.display = "block";
		document.getElementById('yourType1').value = JSON.parse(response)['yourpoketype1'];

		document.getElementById('enemyname').innerHTML = JSON.parse(response)['enemypokename'];
		document.getElementById('enemytype1').innerHTML = JSON.parse(response)['enemypoketype1'];
		if(JSON.parse(response)['enemypoketype2'] == ""){
			document.getElementById('enemytype2').innerHTML = "NAN";
		}else{	
		document.getElementById('enemytype2').innerHTML = JSON.parse(response)['enemypoketype2'];
		}
		document.getElementById('enemyinfo').style.display = "block";
		document.getElementById('enemyType1').value = JSON.parse(response)['enemypoketype1'];
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#btnSignUp02').click(function() {
	console.log("This is working so far");
        $.ajax({
            url: '/signUp02',
            data: $('form').serialize(),
            type: 'POST',
	   
            success: function(response) {
		console.log(response);
		document.getElementById('yourDamage').innerHTML = parseFloat(JSON.parse(response)['yourdamage'])*100 + "%";
		document.getElementById('enemyDamage').innerHTML = parseFloat(JSON.parse(response)['enemydamage'])*100 + "%";

            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});


