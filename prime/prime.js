var checkPrime = function(input) {
	var n = parseInt(input, 10);
	if(n > 1){
		var prime = true;
		for(i=2; i<(Math.round(Math.sqrt(n)))+1; i++){
			if(n % i ===0){
				prime = false;
			}
		}
		if(prime === true){
			console.log("true");
		}
		else{
			console.log("false");
		}
	}
	else {
		console.log("false");
	}
};


checkPrime(process.argv[2]);
