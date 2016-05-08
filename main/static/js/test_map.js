<script type="text/javascript">
		// L.mapbox.accessToken = 'pk.eyJ1IjoibWFnYm8iLCJhIjoiY2luZW5hbzB6MDA2b3ZrbHhuenJpejlkdyJ9.LEce2AH5VgB16ybip-bsqQ';
		var geojson = {{ geo_json|safe }}
		console.log(geojson)

		var postTitle = "{{post.title|safe}}"
		var postPlace = "{{post.place|safe}}"
		var postText = "{{post.text|safe}}"
		var postImage = "{{post.image|safe}}"
		// var popupImgUrl = "{{post.image.url|safe}}" // ValueError when imageField is empty

		// var postImageUrl = function() {
		// 	if (postImage != null) {
		// 		var popupImgUrl = "{{post.image.url|safe}}"
		// 		return popupImgUrl
		// 	else {
		// 		return "some str"
		// 	}	
		// 	}
		// };
		// postImageUrl();

		var postImagePopup = function() {
			if (postImage == null) {
				return '<img src='+'travelapp/mysite/static/css/main/images/main-boat.jpg' + ' alt="Photo" class="popup-img"/>'
				// console.log('image is null')
			} 
			// else {
				// return '<img src='+ popupImgUrl + ' alt="Photo" class="popup-img"/>'
			};
			
		};
		// isEmpty(postImage);
		console.log(postImage)

		console.log(postPlace)
		function onEachFeature(feature, layer) {
    		// does this feature have a property named popupContent?
    	if (feature.properties && feature.properties.popupContent) {
        	layer.bindPopup(feature.properties.popupContent);
    	}
	}

		function map_init_basic (map, options) {
			L.geoJson(geojson).addTo(map)
				.bindPopup(postImagePopup() + '<div class="popup-text"><p>' + postTitle + '</p><p>' + postPlace + '</p></div>')
				.openPopup();
			// L.marker([22.35,78.66]).addTo(map);

			map.setZoom(13);
		// 	L.geoJson(geojson, {
		// 		onEachFeature: onEachFeature
		// 	}).addTo(map);
		 } 
		// var map = L.mapbox.map('map', 'mapbox.streets')
    // .setView([40, -74.50], 2);

    function map_init_basic (map, options) {
			var overlaysBounds = [];
			var layer = L.geoJson(geojson);
			layer.addTo(map)
			overlaysBounds.push(layer.getBounds());
			map.fitBounds(overlaysBounds, {padding: [50, 50]});
			// map.setZoom(13);

	</script> 