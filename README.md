# Spotify Play Count Fetcher

A simple script to fetch play count of all the songs available on a artist' page

# Usage

`python3 main.py [your-auth-token] [artist-id]` 

# References 

To get your authentication token, simply browse [this url](https://open.spotify.com/access_token) while being logged on your Spotify account and grab `accessToken`

To get your target's artist id, open the Spotify desktop app, right click on it's profile -> Share -> Copy Spotify URI and remove `spotify:artist:` you'll be left with something like `4FpJcNgOvIpSBeJgRg3OfN` which is your artist id. 
