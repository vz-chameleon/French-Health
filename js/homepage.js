/**
* homepage.js contains all necessary functions for the homepage of this visualisation project to function, from displaying the home page with France's map
* to charging up the data, giving information and previews, and switching up the visualisations
* @file Contains the necessary functions for the home page behaviour
* @author Valentina Zelaya & Timothy Garwood
* @version 1.0
*/
//HISTORY : January 1st 2018 - Initial design and coding (@vz-chameleon)

/**
* Custom resize function
*/
function resize() {
    var width = $(window).width();
    var height = $(window).height();

    projection.scale([height * 5])
              .translate([width / 2, height / 2]);

    d3.select("#map").attr("width", width).attr("height", height);
    d3.select("svg").attr("width", width).attr("height", height);

    d3.selectAll("path").attr('d', path);
}


/**
* A function to initialize homepage
* Here is where we load France's regions map
*/
function initHomepage(){

  var width = $(window).width();
  var height = $(window).height();

  // Set resize function through d3 var
  d3.select(window).on('resize', resize);


  //------- FRANCE'S MAP SET UP (OLD REGIONS, before 2015) ------

  // Create a path object to manipulate geoJSON data
  var geopath = d3.geoPath();

  // Define projection property
  var projection = d3.geoConicConformal() // Lambert-93
  		               .center([2.454071, 46.279229]) // Center on France
  		               .scale(3000)
  		               .translate([300,300]);

  geopath.projection(projection); // Assign projection to path object

  // Add svg HTML tag to DOM
  var svg = d3.select('#france_map').append("svg")
  		        .attr("id", "svg")
  		        .attr("width", width)
  		        .attr("height", height);

  // Append the group that will contain our paths
  //var fr_regions = svg.append("g");
  var deps=svg.append("g");

  var div = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

  d3.json('data/regions-avant-redecoupage-2015.geojson', function(error,geojson) {
    deps.selectAll("path")
        .data(geojson.features)
        .enter()
        .append("path")
        .attr('class', 'France_region')
        .attr("d", geopath)
        .on("mouseover", function(d) {
            div.transition()
                .duration(200)
                .style("opacity", .8);
            div.html(" <b> Région </b> : " + d.properties.nom)
                .style("left", (d3.event.pageX + 30) + "px")
                .style("top", (d3.event.pageY - 30) + "px")
        })
        .on("mouseout", function(d) {
            div.transition()
                .duration(500)
                .style("opacity", 0);
            div.html("")
                .style("left", "0px")
                .style("top", "0px");
        });
});

  /*d3.json('regions-avant-redecoupage-2015.geojson', function(req, geojson) {
    fr_regions.selectAll("path")
        .data(geojson.features)
        .enter()
        .append("path")
        .attr("d", path);
});*/
}