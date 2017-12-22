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

var city = $('#city-div').text();
var country = $('#country-div').text();

// AIzaSyDUqXmP7zeKMgsLSRCXTYqvUqLO2fux8xA API key for static map
// https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key=YOUR_API_KEY
var url = "https://maps.googleapis.com/maps/api/staticmap";
var apikey = "AIzaSyDUqXmP7zeKMgsLSRCXTYqvUqLO2fux8xA";
// Need to replace spaces within city and country
var geocode = "center=" + city + "," + country;
var size = "size=600x300";
var zoom = "zoom=10";
url += '?' + geocode + '&' + zoom + '&' + size + '&key=' + apikey;

var imgHTML = "<img src='" + url + "'>";

$('#map').append(imgHTML);

console.log(city + " " + country);
console.log(url);

