// Following 2 functions placed here as it must be in global scope to work.
function initMap() {} 
function onYouTubeIframeAPIReady() {}

(function() {

	if ($('div').is('#event-info-page') || $('div').is('#new-event-page')) {

		$('#end-date-checkbox').click(function() {
			$('#end-date-container').toggle('fast');
		});

		$('#edit-btn').click(function() {
			$('#edit-event').toggle('fast');
		});

	}

	// Load this javascript if page is eventinfo
	if ($('div').is('#event-info-page')) {
		/* 
		* LOAD YOUTUBE PLAYER
		*/
		// Load Youtube iframe and video player
		var tag = document.createElement('script');
		tag.src = "https://www.youtube.com/iframe_api";
		var firstScriptTag = document.getElementsByTagName('script')[0];
		firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

		// Create an <iframe> (and YouTube player) after the API code downloads.
		var player;
		onYouTubeIframeAPIReady = function() {
			var youtubeID = $('#youtube-input').val();
			player = new YT.Player('player', {
				height: '390',
				width: '640',
				videoId: youtubeID,
				events: {
					'onReady': onPlayerReady,
					'onStateChange': onPlayerStateChange
				}
			});
		}

		// The API will call this function when the video player is ready.
		function onPlayerReady(event) {
			event.target.playVideo();
		}

		// The API calls this function when the player's state changes. The function indicates that when playing a video (state=1), the player should play for six seconds and then stop.
		var done = false;
		function onPlayerStateChange(event) {
			if (event.data == YT.PlayerState.PLAYING && !done) {
				setTimeout(stopVideo, 6000);
				done = true;
			}
		}

		function stopVideo() {
			player.stopVideo();
		}


		// toggle display of static maps
		var maps = $('#maps');
		$('#maps-btn').click(function() {
			maps.toggle('slow');
		});


		var locality = $('#locality-div').text().replace(/ +/g, "+");
		var city = $('#city-div').text().replace(/ +/g, "+");
		var country = $('#country-div').text().replace(/ +/g, "+");

		/* 
		* LOAD GOOGLE STATIC MAPS: use as reference with js map
		*/
		// AIzaSyCup9ch8zCcZ6BAzwnp4RnC4f8L-FOkI-Y API key for google maps
		var url = "https://maps.googleapis.com/maps/api/staticmap";
		var apikey = "key=" + "AIzaSyCup9ch8zCcZ6BAzwnp4RnC4f8L-FOkI-Y";
		var size = "size=600x400";
		var zoom = "zoom=";
		// var address also to be used in javascript maps, so var center will concatenate it
		var center = "center=";
		var address = ""; 
		var marker = "markers=color:red%7C";
		var imgHTML;

		if (country == '' && city == '') { // if both are empty
			$('#location-div').append("<p>No location specified</p>");
			zoom += "1";
			address += "0,0";
			marker = "";
			center += address;
		} else if (city == '' && country != '') { // if there is only a country
			zoom += "3";
			address += country;
			marker = "";
			center += address;
		} else if (city != '' && country == '') { //if there is only a city
			if (locality != '') { // locality alos named, so append a map of that first
				zoom += "14";
				address += locality + "," + city;
				marker += locality + "," + city;
				center += address;
				// append map for locality
				url += '?' + center + '&' + zoom + '&' + size + '&' + marker + '&' + apikey;
				imgHTML = "<img src='" + url + "'>";
				maps.append(imgHTML);
			}
			// reinitialise each varibale since it has already been appended with locality
			url = "https://maps.googleapis.com/maps/api/staticmap";
			zoom = "zoom=6";
			center = "center=" + city;
			marker = "markers=color:red%7C" + city;
		} else { // else both city and country are named
			if (locality != '') { //locality also named > append maps for locality and city
				zoom += "14";
				address += locality + "," + city + "," + country;
				marker += locality + "," + city + "," + country;
				center += address;
				// append map for locality
				url += '?' + center + '&' + zoom + '&' + size + '&' + marker + '&' + apikey;
				imgHTML = "<img src='" + url + "'>";
				maps.append(imgHTML);
				//append map for city
			} 
			// reinitialise each varibale since it has already been appended with locality
			zoom = "zoom=6";
			center = "center=" + city + "," + country;
			marker = "markers=color:red%7C" + city + "," + country;
			url = "https://maps.googleapis.com/maps/api/staticmap";
		}

		url += '?' + center + '&' + zoom + '&' + size + '&' + marker + '&' + apikey;
		imgHTML = "<img src='" + url + "'>";
		maps.append(imgHTML);


		/* 
		* LOAD GOOGLE JAVASCRIPT INTERACTIVE MAP
		*/
		var geocoder;
		var map;
		initMap = function() {
			geocoder = new google.maps.Geocoder();
			var eventlatlng = {lat: 0, lng: 0};
			map = new google.maps.Map(document.getElementById('map-js'), {
		      center: eventlatlng,
		      zoom: 4
		    });
		    codeAddress();
		};

		function codeAddress() {
			geocoder.geocode( { 'address': address}, function(results, status) {
				if (status == 'OK') {
					map.setCenter(results[0].geometry.location);
			        var marker = new google.maps.Marker({
			            map: map,
			            position: results[0].geometry.location
			        });
				} else {
					console.log('Geocode was not successful for the following reason: ' + status);
				}
			});
		}
	}

})();