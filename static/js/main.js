$(document).ready(function(){

	console.log('js works!')
	

})


       /*$('#next').on('click', function(){

		
       })*/




        $('#sendCommand').on('click', function(){
		console.log('button works!')
		var csrftoken = getCookie('csrftoken');
		$.ajax({
			type: "POST",
			url:"/repositorios/consultar/",
			method:"POST",
			dataType:"json",
			data:{"command": $("#dataCommand").val() },
			beforeSend: function(xhr){
				$('.rm').remove()
				console.log('Value : ', $("#dataCommand").val())
				xhr.setRequestHeader("X-CSRFToken", csrftoken)
			},
			success: function(){
				console.log("Hello wordl!")
			}
		}).done(function(msg){
			var arr = []
			var ren = []
			var $list = $("#hereText")
			msg.data.map(i => arr.push(i))
			console.log(arr[0])
			$.each(arr, function(i, el){
				ren[i] = "<li class='rm'>" + el + "</li>"
				})
			$list.append(ren.join(""))
		}).fail(function(jqXHR, textStatus){
				
			alert('Connection failed!', textStatus)
				
			
		}).always(function(){
			console.log('Alaways Sentence')
		})
		})

function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


function setear(str){

	if(str){
		
	}

}
    
