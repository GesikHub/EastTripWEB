$(document).ready(function() {
	var a = {"Ё":"YO","Й":"I","Ц":"TS","У":"U","К":"K","Е":"E","Н":"N","Г":"G","Ш":"SH","Щ":"SCH","З":"Z","Х":"H","Ъ":"'","ё":"yo","й":"i","ц":"ts","у":"u","к":"k","е":"e","н":"n","г":"g","ш":"sh","щ":"sch","з":"z","х":"h","ъ":"'","Ф":"F","Ы":"I","В":"V","А":"a","П":"P","Р":"R","О":"O","Л":"L","Д":"D","Ж":"ZH","Э":"E","ф":"f","ы":"i","в":"v","а":"a","п":"p","р":"r","о":"o","л":"l","д":"d","ж":"zh","э":"e","Я":"Ya","Ч":"CH","С":"S","М":"M","И":"I","Т":"T","Ь":"'","Б":"B","Ю":"YU","я":"ya","ч":"ch","с":"s","м":"m","и":"i","т":"t","ь":"'","б":"b","ю":"yu"};	
	

	$('#transletterAddress').on('click', function (e) {
		e.preventDefault();
		$('#lAddress').val(transliterate($('#cAddress').val()));
	});


	$('#transletterName').on('click', function (e) {
		e.preventDefault();
		$('#lName').val(transliterate($('#cName').val()));
	});	

	$('#setWeek').on('click', function (e) {
		e.preventDefault();
		$("#oMon").val($("#oSet").val());
		$("#cMon").val($("#cSet").val());

		$("#oTue").val($("#oSet").val());
		$("#cTue").val($("#cSet").val());

		$("#oWed").val($("#oSet").val());
		$("#cWed").val($("#cSet").val());

		$("#oThu").val($("#oSet").val());
		$("#cThu").val($("#cSet").val());

		$("#oFri").val($("#oSet").val());
		$("#cFri").val($("#cSet").val());

		$("#oSat").val($("#oSet").val());
		$("#cSat").val($("#cSet").val());

		$("#oSun").val($("#oSet").val());
		$("#cSun").val($("#cSet").val());
	});

	$('#setWeekdays').on('click', function (e) {
		e.preventDefault();
		$("#oMon").val($("#oSet").val());
		$("#cMon").val($("#cSet").val());

		$("#oTue").val($("#oSet").val());
		$("#cTue").val($("#cSet").val());

		$("#oWed").val($("#oSet").val());
		$("#cWed").val($("#cSet").val());

		$("#oThu").val($("#oSet").val());
		$("#cThu").val($("#cSet").val());

		$("#oFri").val($("#oSet").val());
		$("#cFri").val($("#cSet").val());

		$("#oSat").val($("#oSet").val());
		$("#cSat").val($("#cSet").val());

		$("#oSun").val($("#oSet").val());
		$("#cSun").val($("#cSet").val());
	});

	$('#setWeekends').on('click', function (e) {
		e.preventDefault();
		$("#oSat").val($("#oSet").val());
		$("#cSat").val($("#cSet").val());

		$("#oSun").val($("#oSet").val());
		$("#cSun").val($("#cSet").val());
	});
	

	$('#fullWeek').on('click', function (e) {
	if($(this).prop('checked')){	
		$('input[type="time"]').attr("disabled", true); 
    	$('#FreeWeekends').attr("disabled", true); 
    	$('#FreeWeekends').prop('checked', false);
    }else{ 
		$('#FreeWeekends').attr("disabled", false);
		$('input[type="time"]').attr("disabled", false);
		$("#oMon").val("");
		$("#cMon").val("");

		$("#oTue").val("");
		$("#cTue").val("");

		$("#oWed").val("");
		$("#cWed").val("");

		$("#oThu").val("");
		$("#cThu").val("");

		$("#oFri").val("");
		$("#cFri").val("");

		$("#oSat").val("");
		$("#cSat").val("");

		$("#oSun").val("");
		$("#cSun").val("");
    }
	});


	$('#FreeWeekends').on('click', function (e) {
	if($(this).prop('checked')){		
		$("#oSat").attr("disabled", true);
		$("#cSat").attr("disabled", true);
		$("#oSun").attr("disabled", true);
		$("#cSun").attr("disabled", true); 
    }else{ 
    	$("#oSat").attr("disabled", false);
		$("#cSat").attr("disabled", false);
		$("#oSun").attr("disabled", false);
		$("#cSun").attr("disabled", false);


		$("#oSat").val("");
		$("#cSat").val("");

		$("#oSun").val("");
		$("#cSun").val("");
    }
	});
	
	//тут проблемы со складыванием времени
	/*$('#setEighthours').on('click', function (e) {
		e.preventDefault();
		if($('#fullWeek').prop('checked')){

		}else{ // Не работают ли всю неделю

	   	if($("#oMon").val() && $("#cMon").val()){
	   		$("#oMon").val("08:00");
	   		$("#cMon").val("17:00");
	   	}else{
	   		if($("#oMon").val()){
	   			var time1 = new Time('27.06.2017 8:30')
				time2 = new Time(+time1 + 45 * 6e4);// дичь
	   		}else{
	   			if($("#cMon").val()){

	   			}else{}
	   		}
	   	}

	   	if($("#oTue").val() && $("#cTue").val()){
	   		$("#oTue").val("08:00");
	   		$("#cTue").val("17:00");
	   	}else{
	   		if($("#oTue").val()){

	   		}else{
	   			if($("#cTue").val()){

	   			}else{}
	   		}
	   	}

	   	if($("#oWed").val() && $("#cWed").val()){
	   		$("#oWed").val("08:00");
	   		$("#cWed").val("17:00");
	   	}else{
	   		if($("#oWed").val()){

	   		}else{
	   			if($("#cWed").val()){

	   			}else{}
	   		}
	   	}

	   	if($("#oThu").val() && $("#cThu").val()){
	   		$("#oThu").val("08:00");
	   		$("#cThu").val("17:00");
	   	}else{
	   		if($("#oThu").val()){

	   		}else{
	   			if($("#cThu").val()){

	   			}else{}
	   		}
	   	}

	   	if($("#oFri").val() && $("#cFri").val()){
	   		$("#oFri").val("08:00");
	   		$("#cFri").val("17:00");
	   	}else{
	   		if($("#oFri").val()){

	   		}else{
	   			if($("#cFri").val()){

	   			}else{}
	   		}
	   	}

	   	if($('#FreeWeekends').prop('checked')){

	   	}else{ // Работают ли по выходным

	   	if($("#oSat").val() && $("#cSat").val()){
	   		$("#oSat").val("08:00");
	   		$("#cSat").val("17:00");
	   	}else{
	   		if($("#oSat").val()){

	   		}else{
	   			if($("#cSat").val()){

	   			}else{}
	   		}
	   	}

	   	if($("#oSun").val() && $("#cSun").val()){
	   		$("#oSun").val("08:00");
	   		$("#cSun").val("17:00");
	   	}else{
	   		if($("#oSun").val()){

	   		}else{
	   			if($("#cSun").val()){

	   			}else{}
	   		}
	   	}
	   	}

	   	}
	});*/









	


function transliterate(word){
  return word.split('').map(function (char) { 
    return a[char] || char; 
  }).join("");
}


});