fetch('https://mi-linux.wlv.ac.uk/~1916829/week7_workings/html__javascript/my-api.php?city=London')

        .then(response => response.json())
        .then(response => {
            // display whole API response in brower console (take a look at it!)
        console.log(response);

        // including city name 
        document.querySelector('#city').innerHTML = response.name;

        // including the country name
        document.querySelector('#country').innerHTML = response.sys.country;
        
        // getting the icon
        document.querySelector('#pic').src = 'http://openweathermap.org/img/wn/' + response.weather[0].icon + '@4x.png';
        
        // getting the tempreture
        document.querySelector('#tempreture').innerHTML = Math.round(response.main.temp) + '\u00B0';

        // getting the high tempreture
        document.querySelector('#high').innerHTML = 'H: ' + Math.round(response.main.temp_max) + '\u00B0';

        // getting the low  tempreture
        document.querySelector('#low').innerHTML = 'L: ' + Math.round(response.main.temp_min) + '\u00B0';
        
        })

        .catch(err => {
            // display errors on console
            console.log(err)
        })