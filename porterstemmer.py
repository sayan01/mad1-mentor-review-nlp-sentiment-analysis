import string
from collections import defaultdict
from nltk.stem import PorterStemmer

def preprocess_text(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    text = text.lower()
    return text

def build_word_frequency_dict(text):
    word_freq = defaultdict(int)
    stemmer = PorterStemmer()

    words = text.split()
    for word in words:
        root_word = stemmer.stem(word)
        word_freq[root_word] += 1

    return word_freq


from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "happy"
    elif polarity < 0:
        return "angry"
    else:
        return "neutral"


def main():
    file_path = input("Enter the path to the text file(review): ") or "reviews"

    try:
        with open(file_path, 'r') as file:
            happy_count = 0
            angry_count = 0
            content = file.read()

            for line in content.split('\n'):
                sentiment = analyze_sentiment(line)
                if sentiment == "happy":
                    happy_count += 1
                elif sentiment == "angry":
                    angry_count += 1

            preprocessed_content = preprocess_text(content)
            word_freq_dict = build_word_frequency_dict(preprocessed_content)
            sorted_freq_dict = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)
            common_file_path = input("Enter common words file path(common): ") or "common"
            with open(common_file_path, 'r') as common_file:
                common = common_file.read().split('\n')
            filtered_freq_dict = [(k,v) for k, v in sorted_freq_dict if v > 1 and k not in common]

            print("Top Frequently used Words in Reviews")
            print("-"*31)

            for word, freq in filtered_freq_dict[:10]:
                print(f"{word}: {freq}")

            print("Sentiment Analysis Summary:")
            print("-"*31)
            print(f"Happy reviews: {happy_count}")
            print(f"Angry reviews: {angry_count}")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
