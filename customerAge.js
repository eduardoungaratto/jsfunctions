function customerAge(){
	var today = new Date();
	var yearToday = today.getFullYear();
	var monthToday = today.getMonth();
	var dayToday = today.getDate(); //day month
	var ageY = document.getElementsByName("yearNasc")[0].value;
	var ageM = document.getElementsByName("monthNasc")[0].value;
	var ageD = document.getElementsByName("dayNasc")[0].value;
	var age = yearToday - ageY;

	if(ageM<=monthToday){
		var months = (parseInt(ageM) + (12-parseInt(monthToday)));
	}else if(ageM>monthToday){
		var months = (parseInt(ageM) + (12-parseInt(monthToday))-12);
	}

	console.log(age + "  anos  " + months + "   Meses "+ " e   " + dayToday + "    dias ");
}
