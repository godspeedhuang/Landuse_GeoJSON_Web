// map
var mymap = L.map('mapid').setView([23.8759391,120.588669,8], 8);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZ29kc3BlZWQ4ODE2OCIsImEiOiJjazJyYXFxOWswbzBmM2NwaHliYjk3OHM4In0.PbTCzhNRc1P09XF2Z-pd0g'
}).addTo(mymap);

// var xhr = new XMLHttpRequest();
// xhr.open('get', 'https://godspeedhuang.github.io/landuse_cralwer/KHH_block/E0101_block.json', true);
// xhr.send();

// $.getJSON("map.geojson", function (r) {
//     L.geoJSON(r, { color: "#333" }).addTo(mymap);
//   });


// get district 代碼
// let districtId =document.getElementById('area_list');
// districtId.onchange = function() { //當選項改變時觸發
//     var valOption = this.options[this.selectedIndex].value; //獲取option的value
//     console.log(valOption);
// }



