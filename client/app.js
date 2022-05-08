function onPageLoad() {
    var url = "http://127.0.0.1:5000/get_district_names";

    $.get(url,function(data, status) {
        if(data) {
            var districts = data.districts;
            var uiDistricts = document.getElementById("uiDistricts");
            $('#uiDistricts').empty();
            $('#uiDistricts').append(new Option("hk_central_and_western"));
            for (var i in districts) {
                $('#uiDistricts').append(new Option(districts[i]));
            }
        }
    });
}
window.onload = onPageLoad;


function onClickEstimatePrice() {
    var area = document.getElementById("uiArea");
    var market = document.querySelector('input[name="Market"]:checked');
    var district = document.getElementById("uiDistricts");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        area: parseFloat(area.value),
        market: market.value,
        district: district.value
    }, function(data, status) {
        var priceHKD = data.predicted_price;
        var psfHKD = Math.round(priceHKD*1000000 / parseFloat(area.value));
        var priceCAD = (data.predicted_price * 0.16).toFixed(2);
        var psfCAD = Math.round(priceCAD*1000000 / parseFloat(area.value));
        estPrice.innerHTML = "<h2>That will be <br>HKD" + priceHKD + "M ($" + psfHKD + " per sqft)<br>or CAD" 
        + priceCAD + "M ($" + psfCAD + " per sqft)</h2>";
    });
}