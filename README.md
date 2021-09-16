# Spotify Song Recommender

This is a small app, build with Streamlit. It will recommend you another song similar to one you like</p> 


## How it works

You can tell it a song you like, it will then webscrape the BillBoards hot 100, if the song you choose is in there, it will recommend another song from the hot 100 that sounds similar (determined via Spotify Audio features and ML-Clustering). If your song is not there it will recommend one from Spotify determined in the same way.</p>

## Getting Started

If you want to host it on your local machine. [See Here](#executing-program)
### Dependencies

**Since this program used a Kaggle dataset that no longer is publicly available, it will not work.
You can however take another dataset or use the Spotify-API to scrape the data from there and rewrite the program slightly to make it work**

### Installing

If you want to run the program locally Install dependencies via 

``` pip install -r requirements.txt ```

### Executing program

Then once you have activated your virtual environment in the terminal
simply write

``` streamlit run spotify_info.py ```

A new browser window should automatically open and you should be able to see the streamlit interface.
You now can simply enter a song into the interface and press search. The recommended song should be given to you in a couple of seconds.

#### Please take notice that this AS IS will no longer work [see here](#dependencies)
## Help

**This project is abandoned**, if you want to modify it for your own dataset or usage, feel free to do so.
If you want/need help, you can always reach out to me.
## Authors

Maximilian Sören Pollak

[Github](https://github.com/maximiliansoerenpollak)  
[LinkedIn](https://linkedin.com/in/msoerenpollak)

## Version History

* 0.2
    * Fixed README
    * Added .gitignore
    * Added MIT License
* 0.1
    * Initial Commit

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [Ironhack-Project](https://github.com/ironhack-labs/lab-unsupervised-learning-intro)
