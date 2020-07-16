import language_processer
import web_scraper as scraper
import player_data

templates = {
    "very_negative": [
        "Wouldn't touch {PLAYER} with a ten foot pole this week."
    ],
    "negative": [
        "{PLAYER} is not a strong play this week."
    ],
    "neutral": [
        "I could take or leave {PLAYER} this week, nothing to write home about."
    ],
    "high": [
        "High on {PLAYER} this week, just a feeling."
    ],
    "very_high": [
        "High on {PLAYER} this week, just a feeling."
    ],
}

def generate_tweet(player, horoscope, templates=templates):
    formatted_horoscope = scraper.formatted_horoscope(horoscope)
    score = language_processer.get_sentiment_score(formatted_horoscope)

    print(player)
    print(score)
    print(horoscope)

    if score <= -0.5:
        return templates["very_negative"]
    elif score <= -0.25:
        return templates["negative"]
    elif score <= 0.25:
        return templates["neutral"]
    elif score <= 0.5:
        return templates["high"]
    else:
        return templates["very_high"]


print(generate_tweet(player_data.get_player_data()[22][0], player_data.get_player_data()[22][1], templates))