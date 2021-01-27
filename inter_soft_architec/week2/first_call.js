fetch('https://api.openweathermap.org/data/2.5/weather?q=Herat,&appid=a9674e7298c06e2d719d1133e6178cba')

        .then(response => response.json())
        .then(response => {
            // display whole API response in brower console (take a look at it!)
        console.log(response);

        // copy one element of response to our HTML paragraph
        document.querySelector('#country').innerHTML = response.sys.country;

        // copying the country to the h2 of the page
        document.querySelector('#weather').innerHTML = response.weather[0].description;

        // copying the sunset
        document.querySelector('#sunrise').innerHTML = response.sys.sunrise;

        // copying the sunset
        document.querySelector('#sunset').innerHTML = response.sys.sunset;

        })

        .catch(err => {
            // display errors on console
            console.log(err)
        })