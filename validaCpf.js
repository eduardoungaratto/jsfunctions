function validaCpf() {
	arrMulti1 = [10, 9, 8, 7, 6, 5, 4, 3, 2];
	arrMulti2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2];
	arrR1 = [];
	arrR2 = [];
	somaR1 = 0;
	somaR2 = 0;
	repeatNumber = 0;
	validFormat = true;
	strCPF = document.getElementById('cpf').value; //get cpf
	arrCPF = strCPF.split(''); // split char
	valid = false;

		for (index=10; index>=0; index--) {
			if(arrCPF[index] == arrCPF[index-1]){
				repeatNumber++;
			}
		}

		if(repeatNumber == 10) {
			validFormat = false
			document.getElementById('cpf').value = '';
			alert('Formato inválido!');
		}

		if(validFormat) {
			if(!valid){
				for (index=0; index<=8; index++) {
					arrR1[index] = (arrCPF[index] * arrMulti1[index]); // multi and save the response in arrR
				}


				for (index=0; index<=8; index++) {
					somaR1+= arrR1[index];
				}

				divQ1 = parseInt((somaR1*10)/11);
				divR1 = parseInt((somaR1*10)%11);
				
				if (divR1 == 10 || divR1 == 11) {
					validaPD = 0;
				} else {
					validaPD = divR1;
				}

				if(validaPD == arrCPF[9]){ // verify if the result digit from calc is equals to arrCPF[9] = first digit;
					valid = true;
				} else {
					valid = false;
				}
			}

			if(valid) {
				for (index=0; index<=9; index++) {
					arrR2[index] = (arrCPF[index] * arrMulti2[index]);
				}


				for (index=0; index<=9; index++) {
					somaR2+= arrR2[index];
				}

				divQ2 = parseInt((somaR2*10)/11);
				divR2 = parseInt((somaR2*10)%11);

				if (divR2 == 10 || divR2 == 11) {
					validaSD = 0;
				} else {
					validaSD = divR2;
				}

				if (validaSD == arrCPF[10]){ // verify if the result digit from calc is equals to arrCPF;
					valid = true;
				} else {
					valid = false;
				}
			}

			if(!valid) {
				document.getElementById('cpf').value = '';
				alert('CPF inválido!');
			}
		return valid;
		}
}