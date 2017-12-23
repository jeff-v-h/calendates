(function() {
	
	document.getElementById('end-date-checkbox').addEventListener('click', function() {
		var endDateContainer = document.getElementById('end-date-container');
		if (this.checked) {
			endDateContainer.style.display = 'block';
		} else {
			endDateContainer.style.display = 'none';
		}
	});

	document.getElementById('edit-btn').addEventListener('click', function() {
		var editForm = document.getElementById('edit-event');
		if (editForm.style.display == 'block') {
			editForm.style.display = 'none';
		} else {
			editForm.style.display = 'block';
		};
	});

	
})();