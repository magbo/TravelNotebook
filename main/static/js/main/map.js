var mymap = L.map('mapid').setView([51.505, -0.09], 2);
// setView([51.505, -0.09], 13)

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    // satelite map:
    id: 'magbo.pp277k86', 
    // basic map:
    id2: 'magbo.pp2849kk',
    accessToken: 'pk.eyJ1IjoibWFnYm8iLCJhIjoiY2luZW5hbzB6MDA2b3ZrbHhuenJpejlkdyJ9.LEce2AH5VgB16ybip-bsqQ'}
    ).addTo(mymap);

var marker = L.marker([52.0977181, 19.0258159]).addTo(mymap);