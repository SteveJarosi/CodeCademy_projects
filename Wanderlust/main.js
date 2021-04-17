import {openWeatherKey, clientId, clientSecret} from "./api.js";
// Foursquare API Info
const url = 'https://api.foursquare.com/v2/venues/explore?near=';
// OpenWeather Info
const weatherUrl = 'https://api.openweathermap.org/data/2.5/weather';
// Page Elements
const $input = $('#city');
const $submit = $('#button');
const $destination = $('#destination');
const $container = $('.container');
const $venueDivs = [$("#venue1"), $("#venue2"), $("#venue3"), $("#venue4"), $("#venue5")];
const $weatherDiv = $("#weather1");
const nuberOfRandomVenues = 5;
// Add AJAX functions here:
const getVenues = async () => {
  const city = $input.val();
  let urlToFetch = `${url}${city}&limit=10&client_id=${clientId}&client_secret=${clientSecret}&v=20210129`;
  console.log(urlToFetch)
  try {
    const response = await fetch(urlToFetch);
    if (response.ok) {
      //console.log(response);
      const jsonResponse = await response.json();
      //console.log(jsonResponse);
      const venues = jsonResponse.response.groups[0].items.map(parameter => parameter.venue);
      //console.log(venues);
      let tempVenues = [];
      let tempVn;
      do {
        let idx = Math.floor(Math.random() * venues.length);
        //console.log(idx);
        //venues.splice(idx, 1)
        //console.log(venues.splice(idx, 1));
        tempVn = venues.splice(idx, 1);
        //console.log(tempVn[0]);
        tempVenues.push(tempVn[0]);
      } while (tempVenues.length < nuberOfRandomVenues);
      console.log(tempVenues);
      //venues = tempVenues;
      return tempVenues
    }


  } catch (e) {
    console.log("Error in getVenues:", e);
  }
}

const getForecast = async () => {
  const urlToFetch = `${weatherUrl}?&q=${$input.val()}&APPID=${openWeatherKey}`;
  //console.log(urlToFetch)
  try {
    const response = await fetch(urlToFetch);
    if (response.ok) {
      const jsonResponse = await response.json();
      //console.log(jsonResponse);
      return jsonResponse
    }
    console.log('Error in getForecast');

  } catch (e) {
    console.log(e);
  }
}


// Render functions
const renderVenues = (venues) => {
  $venueDivs.forEach(($venue, index) => {
    // Add your code here:
    const venue = venues[index];
    const venueIcon = venue.categories[0].icon;
    const venueImgSrc = `${venueIcon.prefix}bg_64${venueIcon.suffix}`;
    let venueContent = createVenueHTML(venue.name, venue.location, venueImgSrc);
    $venue.append(venueContent);
  });
  $destination.append(`<h2>${venues[0].location.city}</h2>`);
}

const renderForecast = (day) => {
  // Add your code here:

  let weatherContent = createWeatherHTML(day);
  $weatherDiv.append(weatherContent);
}

const executeSearch = () => {
  $venueDivs.forEach(venue => venue.empty());
  $weatherDiv.empty();
  $destination.empty();
  $container.css("visibility", "visible");
  getVenues().then(venues => renderVenues(venues));
  getForecast().then(forecast => renderForecast(forecast));
  return false;
}

$submit.click(executeSearch)

