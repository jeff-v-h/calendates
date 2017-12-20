(function() {
	
	document.getElementById("end-date-checkbox").addEventListener("click", function() {
		var endDateContainer = document.getElementById("end-date-container");
		if (this.checked) {
			endDateContainer.style.display = "block";
		} else {
			endDateContainer.style.display = "none";
		}
	});

})();