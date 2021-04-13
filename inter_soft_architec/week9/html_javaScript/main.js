// Register service worker
// in here the s_worker.js is get accessed and get registered
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register('s_worker.js').then(function(registration) {
        // Registration was successful
        console.log('ServiceWorker registration successful');
      }, function(err) {
        // registration failed :(
        console.log('ServiceWorker registration failed: ', err);
      });
    });
  }

// check brower cache first, see if there is fresh and less than 10 seconds data, if yeah then use it

if(localStorage.when != null && parseInt(localStorage.when) + 10000 > Date.now()){
    let time = Math.round((Date.now() - localStorage.when)/1000) + "seconds(s)";
    document.getElementById('city').innerHTML = localStorage.city;
    document.getElementById('country').innerHTML = localStorage.country;
    document.getElementById('description').innerHTML = localStorage.description;
    document.getElementById('tempreture').innerHTML = localStorage.temperature;
    document.getElementById('high').innerHTML = localStorage.high;
    document.getElementById('low').innerHTML = localStorage.low;
    document.getElementById('lst_updated').innerHTML = time;

// if there is no local data, no data in cache, access network, access the data base, i mean get the data from my data base in mi-linux account
} else {
    // fetch the weather data form my mi-linux API for a given city
    fetch('https://mi-linux.wlv.ac.uk/~1916829/fully_off/html_javaScript/my-api.php?city=Sheffield')

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
        
        
        // now that you got the data from mi-linux
        // save the new data to browser, with new timestamp
        localStorage.time = response.time;
        localStorage.city = response.city;
        localStorage.country = response.country;
        localStorage.description = response.description;
        localStorage.temperature = response.temperature;
        localStorage.high = response.high;
        localStorage.low = response.low;
        })
        .catch(err => {
          // if fetching data from network/ mi-linux failled
          // access the data from cache and display

          if(localStorage.when != null){
            // get the data from cache
            let time = Math.round((Date.now() - localStorage.when)/1000) + "seconds(s)";
            document.getElementById('city').innerHTML = localStorage.city;
            document.getElementById('country').innerHTML = localStorage.country;
            document.getElementById('description').innerHTML = localStorage.description;
            document.getElementById('tempreture').innerHTML = localStorage.temperature;
            document.getElementById('high').innerHTML = localStorage.high;
            document.getElementById('low').innerHTML = localStorage.low;
            document.getElementById('lst_updated').innerHTML = time;

          } else {
            // display errors on console
            console.log(err)
          }
        });
}

