import openai
import config 
from flask import Flask, render_template, request, jsonify

#initialize Flask
app = Flask(__name__)
#API key
openai.api_key = config.api_key


# function to generate song recommendations based on user input
def generate_SongRecommendations(artist_name, song_name):
    prompt = f"Based on the song '{song_name}' by {artist_name}, recommend five similar songs based on genre and instrumentals. output only song name and artist name"
    response = openai.chat.completions.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}]
    )
    recommendations = response.choices[0].message.content
    return recommendations


def generate_AlbumRecommendations(album_name, artist_name):
    prompt = f"Based on the album '{album_name}' by {artist_name}, recommend five similar albums based on genre and instrumentals. output only album name and artist name"
    
    response = openai.chat.completions.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}]
    )
    recommendations = response.choices[0].message.content
    return recommendations 


# Flask route for the homepage
@app.route('/')
def index():
    return render_template('homepage.html')


# Handle recommendations request
@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    # Get form data
    artist_name = request.form['artist']
    song_name = request.form['song']
    
    # Get recommendations
    recommendations = generate_SongRecommendations(artist_name, song_name)
    

    # Pass recommendations to the HTML page
    return render_template('demo.html', recommendations = recommendations)

if __name__ == '__main__':
    app.run(debug=True)
    
# Getting song recommendations
artist = input("Enter artist name: ")
song = input("Enter song name: ")

recommendations = generate_SongRecommendations(artist, song)
print("Song Recommendations:")
print(recommendations)

# Getting album recommenndations
artist = input("\nEnter artist name: ")
album = input("Enter album name: ")

recommendations = generate_AlbumRecommendations(artist, album)
print("\nSong Recommendations: ")
print(recommendations)

