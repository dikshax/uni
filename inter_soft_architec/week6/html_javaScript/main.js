fetch('https://api.openweathermap.org/data/2.5/weather?q=Sheffield,uk&appid=a9674e7298c06e2d719d1133e6178cba&units=metric')

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