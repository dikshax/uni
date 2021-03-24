// check brower cache first, see if there is fresh and less than 10 seconds data then use it

if(localStorage.when != null && parseInt(localStorage.when) + 10000 > Date.now()){
    let time = Math.round((Date.now() - localStorage.when)/1000) + "seconds(s)";
    document.getElementById('city').innerHTML = localStorage.city;
    document.getElementById('country').innerHTML = localStorage.country;
    document.getElementById('description').innerHTML = localStorage.description;
    document.getElementById('tempreture').innerHTML = localStorage.temperature;
    document.getElementById('high').innerHTML = localStorage.high;
    document.getElementById('low').innerHTML = localStorage.low;
    document.getElementById('lst_updated').innerHTML = time;
// if there is no local data, data in cache, access network, access the data base
} else {
    // fetch the weather data form my mi-linux API for a given city
    fetch('https://mi-linux.wlv.ac.uk/~1916829/week7_workings/html_javaScript/my-api.php?city=Sheffield')

        .then(response => response.json())
        .then(response => {
            // display whole API response in brower console (take a look at it!)
        console.log(response);

        // including city name 
        document.querySelector('#city').innerHTML = response.city;

        // including the country name
        document.querySelector('#country').innerHTML = response.country;
        
        // getting the description
        document.querySelector('#description').innerHTML = response.description;
        
        // getting the tempreture
        document.querySelector('#tempreture').innerHTML = Math.round(response.temperature) + '\u00B0';

        // getting the high tempreture
        document.querySelector('#high').innerHTML = 'H: ' + Math.round(response.tem_max) + '\u00B0';

        // getting the low  tempreture
        document.querySelector('#low').innerHTML = 'L: ' + Math.round(response.tem_min) + '\u00B0';

        // getting the time
        document.querySelector('#time').innerHTML = response.time;
        
        // save the new data to browser, with new timestamp
        localStorage.time = time.innerHTML;
        localStorage.city = city.innerHTML;
        localStorage.country = country.innerHTML;
        localStorage.description = description.innerHTML;
        localStorage.temperature = tempreture.innerHTML;
        localStorage.high = high.innerHTML;
        localStorage.low = low.innerHTML;
        })
        .catch(err => {
            // display errors on console
            console.log(err)
        });
}

