/* For javascript map -- faster net connection required
var map;
function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 4
    });
} */
var locality = $('#locality-div').text().replace(/ +/g, "+");
var city = $('#city-div').text().replace(/ +/g, "+");
var country = $('#country-div').text().replace(/ +/g, "+");

// AIzaSyDUqXmP7zeKMgsLSRCXTYqvUqLO2fux8xA API key for static map
var url = "https://maps.googleapis.com/maps/api/staticmap";
var apikey = "key=" + "AIzaSyDUqXmP7zeKMgsLSRCXTYqvUqLO2fux8xA";
var size = "size=600x300";
var zoom = "zoom=";
var geocode = "center=";
var marker = "markers=color:red%7C";
var imgHTML;

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
		$('#map').append(imgHTML);
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
		$('#map').append(imgHTML);
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
$('#map').append(imgHTML);

console.log(geocode);
console.log(url);
