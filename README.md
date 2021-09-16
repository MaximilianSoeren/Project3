<h1 align="center"><project-name>Spotify Song Recommender</h1>

<p align="center"><project-description>This is a small app, build with streamlit. It will reccomend you another song similar to one you like</p> 

<h2 align="center">How it works</h2>
<p align="center"><how-it-works>You can tell it a song you like, it will then webscrape the BillBoards hot 100, if the song you choose is in there, it will recommend another song from the hot 100 that sounds similar (determined via Spotify Audio features and ML-Clustering). If your song is not there it will recommend one from Spotify determined in the same way.</p>

## Sections

- [Installation]

- [Try it out](<Homepage url>)


## Screenshots

![Home Page](/screenshots/1.png "Home Page")

![](/screenshots/2.png)

![](/screenshots/3.png)

## Available Commands

In the project directory, you can run:

### `npm start" : "react-scripts start"`,

The app is built using `create-react-app` so this command Runs the app in Development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser. You also need to run the server file as well to completely run the app. The page will reload if you make edits.
You will also see any lint errors in the console.

### `"npm run build": "react-scripts build"`,

Builds the app for production to the `build` folder. It correctly bundles React in production mode and optimizes the build for the best performance. The build is minified and the filenames include the hashes. Your app will be ready to deploy!

### `"npm run test": "react-scripts test"`,

Launches the test runner in the interactive watch mode.

### `"npm run dev": "concurrently "nodemon server" "npm run start"`,

For running the server and app together I am using concurrently this helps a lot in the MERN application as it runs both the server (client and server) concurrently. So you can work on them both together.

### `"serve": "node server"`

For running the server file on you can use this command.

### `npm run serve`

## Built With

- JavaScript
- Node
- NPM
- Webpack
- HTML
- CSS

## Future Updates

- [ ] Reliable Storage

## Author

**Rohit Jain**

- [Profile](https://github.com/rohit19060 "Rohit jain")
- [Email](mailto:rohitjain19060@gmail.com?subject=Hi "Hi!")
- [Website](https://kingtechnologies.in "Welcome")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
# Spotify-Song-Recommender


Webscraping  is wshere data gets scraped from Billboard Top100 

Ml is where the Machine Learning Model was trained and saved. 

Spotify_Info is where all the rest is.
  -Website rendering
  -All Functions needed to retrieve clusters of new songs / old songs
  -Functions to grab the correct Values
  
