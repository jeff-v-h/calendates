/*var city = document.getElementById('city-div').textContent;
var country = document.getElementById('country-div').textContent;
/* For javascript map -- faster net connection required
var map;
function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 4
    });
} */

var city = $('#city-div').text().replace(/ +/g, "+");
var country = $('#country-div').text().replace(/ +/g, "+");

// AIzaSyDUqXmP7zeKMgsLSRCXTYqvUqLO2fux8xA API key for static map
var url = "https://maps.googleapis.com/maps/api/staticmap";
var apikey = "key=" + "AIzaSyDUqXmP7zeKMgsLSRCXTYqvUqLO2fux8xA";
var size = "size=600x300";
var zoom = "zoom=";
var geocode = "center=";

if (country == '' && city == '') { // if both are empty
	$('#location-title').after("<div>No location specified for this event</div>");
	zoom += "1";
	geocode += "0,0";
} else if (city == '' && country != '') { // if there is only a country
	zoom += "3";
	geocode += country;
} else if (city != '' && country == '') { //if there is only a city
	zoom += "5";
	geocode += city;
} else { // else both city and country are named
	zoom += "5";
	geocode += city + "," + country;
}

url += '?' + geocode + '&' + zoom + '&' + size + '&' + apikey;
var imgHTML = "<img src='" + url + "'>";
$('#map').append(imgHTML);

console.log(geocode);
console.log(url);
