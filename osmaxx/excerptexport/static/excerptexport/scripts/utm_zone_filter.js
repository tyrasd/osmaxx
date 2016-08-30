jQuery(document).ready(function(){
    var utm_optgroup_html_element = '#id_coordinate_reference_system optgroup[label="UTM zones"]';
    var utm_zone_optgroup_original = jQuery(utm_optgroup_html_element).clone();

    window.filterUTMZones = function (leafletGeometry) {
        var utm_zone_optgroup = jQuery(utm_optgroup_html_element);

        if (utm_zone_optgroup !== null) {
            utm_zone_optgroup.html("");
            getUTMZones(leafletGeometry).done(function(data){
                var srids = data["utm_zone_srids"].sort();

                var options_html = '';
                srids.forEach(function(srid){
                    var original_text = utm_zone_optgroup_original.find('option[value=' + srid + ']').text();
                    options_html += _optionHTML(srid, original_text);
                });
                utm_zone_optgroup.html(options_html);
            }).error(function(data, other, other2, other3){
                console.log(data, other, other2, other3);
            });
        }

        function getUTMZones(leafletGeometry) {
            var geometry = leafletGeometry.toGeoJSON()["geometry"],
                srid = 4326;
            var csrftoken = Cookies.get('csrftoken');
            return jQuery.ajax({
                url: '/api/utm-zone-info/',
                contentType: "application/json; charset=utf-8",
                dataType: 'json',
                type: 'POST',
                data: JSON.stringify({"geom": geometry, "srid": srid}),
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            });
        }

        function _optionHTML(srid, name) {
            return '<option value="' + srid + '">' + name + '</option>';

        }
    };

});
