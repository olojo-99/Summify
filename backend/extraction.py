import spacy
import pytextrank

# Load a spaCy model
nlp = spacy.load("en_core_web_lg")

# Exclude stopwords that could be generated due to completion prompt
nlp.Defaults.stop_words |= {"transcript", "passage", "extract", "video"}

# Add TopicRank component to pipeline with stopwords
nlp.add_pipe("topicrank", config={"stopwords": {token:["NOUN"] for token in nlp.Defaults.stop_words} })

def topic_rank(text):
    # Perform fact extraction on overall summary and segment summaries
    doc = nlp(text)

    # Create list of top 3 ranked phrases
    phrases = [phrase.text for phrase in doc._.phrases[:3]]

    return phrases