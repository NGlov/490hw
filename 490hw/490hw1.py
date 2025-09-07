import requests

url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

UCID = "nlg"
SECTION = "101"

studentinfo = {
    "UCID": "nlg",
    "first_name": "Nekhi",
    "last_name": "Glover",
    "github_username": "NGlov",
    "discord_username": "ihkenn",
    "favorite_cartoon": "Gravity Falls",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Red dead redemption 2",
    "section": "101"
}

response = requests.post(url, json=studentinfo)
print("Status: ", {response.status_code})
print(response.text)

