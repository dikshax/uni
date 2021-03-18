fetch('https://mi-linux.wlv.ac.uk/~1916829/week7_workings/html_javaScript/my-api.php?city=Sheffield')

        .then(response => response.json())
        .then(response => {
            // display whole API response in brower console (take a look at it!)
        console.log(response);

        // including city name 
        document.querySelector('#city').innerHTML = response.city;

        // including the country name
        document.querySelector('#country').innerHTML = response.country;
        
        // getting the icon
        document.querySelector('#pic').innerHTML = response.description;
        
        // getting the tempreture
        document.querySelector('#tempreture').innerHTML = Math.round(response.temperature) + '\u00B0';

        // getting the high tempreture
        document.querySelector('#high').innerHTML = 'H: ' + Math.round(response.tem_max) + '\u00B0';

        // getting the low  tempreture
        document.querySelector('#low').innerHTML = 'L: ' + Math.round(response.tem_min) + '\u00B0';
        
        })

        .catch(err => {
            // display errors on console
            console.log(err)
        })