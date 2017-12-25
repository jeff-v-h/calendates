function initMap() {} // placed here as it must be in global scope to work.
(function() {

	if ($('div').is('#event-info-page') || $('div').is('#new-event-page')) {
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
			}
		});
	}

	// Load this javascript if page is eventinfo
	if ($('div').is('#event-info-page')) {
		// load javascript interactive map
		initMap = function() {
			var event = {lat: -25.344877, lng: 131.032854};
			var map = new google.maps.Map(document.getElementById('map-js'), {
		      center: event,
		      zoom: 4
		    });
		    var marker = new google.maps.Marker({
		    	position: event,
		    	map: map
		    });
		};

		// load static maps to be used as reference with js map
		var locality = $('#locality-div').text().replace(/ +/g, "+");
		var city = $('#city-div').text().replace(/ +/g, "+");
		var country = $('#country-div').text().replace(/ +/g, "+");

		// AIzaSyDUqXmP7zeKMgsLSRCXTYqvUqLO2fux8xA API key for static map
		var url = "https://maps.googleapis.com/maps/api/staticmap";
		var apikey = "key=" + "AIzaSyDUqXmP7zeKMgsLSRCXTYqvUqLO2fux8xA";
		var size = "size=600x400";
		var zoom = "zoom=";
		var geocode = "center=";
		var marker = "markers=color:red%7C";
		var imgHTML;
		var maps = $('#maps');

		if (country == '' && city == '') { // if both are empty
			$('#location-div').append("<p>No location specified</p>");
			zoom += "1";
			geocode += "0,0";
			marker = "";
		} else if (city == '' && country != '') { // if there is only a country
			zoom += "3";
			geocode += country;
			marker = "";
		} else if (city != '' && country == '') { //if there is only a city
			if (locality != '') { // locality alos named, so append a map of that first
				zoom += "14";
				geocode += locality + "," + city;
				marker += locality + "," + city;
				// append map for locality
				url += '?' + geocode + '&' + zoom + '&' + size + '&' + marker + '&' + apikey;
				imgHTML = "<img src='" + url + "'>";
				maps.append(imgHTML);
			}
			// reinitialise each varibale since it has already been appended with locality
			url = "https://maps.googleapis.com/maps/api/staticmap";
			zoom = "zoom=6";
			geocode = "center=" + city;
			marker = "markers=color:red%7C" + city;
		} else { // else both city and country are named
			if (locality != '') { //locality also named > append maps for locality and city
				zoom += "14";
				geocode += locality + "," + city + "," + country;
				marker += locality + "," + city + "," + country;
				// append map for locality
				url += '?' + geocode + '&' + zoom + '&' + size + '&' + marker + '&' + apikey;
				imgHTML = "<img src='" + url + "'>";
				maps.append(imgHTML);
				//append map for city
			} 
			// reinitialise each varibale since it has already been appended with locality
			zoom = "zoom=6";
			geocode = "center=" + city + "," + country;
			marker = "markers=color:red%7C" + city + "," + country;
			url = "https://maps.googleapis.com/maps/api/staticmap";
		}

		url += '?' + geocode + '&' + zoom + '&' + size + '&' + marker + '&' + apikey;
		imgHTML = "<img src='" + url + "'>";
		maps.append(imgHTML);

		console.log(geocode);
		console.log(url);
	}

	if ($('div').is('#map-page')) {
		
	}

})();