from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyse_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.2:
        label = 'positive'
    elif compound <= -0.2:
        label = 'negative'
    else:
        label = 'neutral'
    
    return label,compound
    