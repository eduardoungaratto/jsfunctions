function getFullAge() {	
	customerData = form.getElementsByClassName('customerData');
	contentCustomerData = customerData[0].childNodes[3];
	dataField = contentCustomerData.getElementsByClassName('dataField');
	fDays = dataField[0].children[1];
	fMonth = dataField[0].children[2];
	fYear = dataField[0].children[3];
	arrDays = [fDays.children];
	arrMonth = [fMonth.children];
	arrYear = [fYear.children];

	for(d=0; d<arrDays[0].length; d++) {
		if(arrDays[0][d].selected == true){
			  sDay = parseInt(arrDays[0][d].value);
			for (m=0; m<arrMonth[0].length; m++) {
				if(arrMonth[0][m].selected == true){
					sMonth = parseInt(arrMonth[0][m].value);
					for (y=0; y<arrYear[0].length; y++) {
						if(arrYear[0][y].selected == true){
							sYear = parseInt(arrYear[0][y].value);
						};
					};
				};
			};
		};
	};

	if(sMonth == 2){
		if(sYear%400==0){
			if (sDay<=29) {
				valid = true;
			} else {
				valid = false;
			};
		} else {
			if (sDay<=28) {
				valid = true;
			} else {
				valid = false;
			};
		};
	} else if ([4,6,9,11].includes(sMonth)) { 
		if (sDay<=30) {
			valid = true;
		} else {
			valid = false;
		};
	} else { 
		for(m=0; m<arrMonth31.length; m++){ 
			if(sMonth == arrMonth31[m]){
				valid = true;
			}
		}
	}
	return valid;
}