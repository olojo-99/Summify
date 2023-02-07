import spacy
import pytextrank

# Load a spaCy model
nlp = spacy.load("en_core_web_lg")

# Add TopicRank component to pipeline
# Exclude stopwords that could be generated due to completion prompt -> NLTK Stopwords
nlp.add_pipe("topicrank", config={"stopwords": {"transcript":["NOUN"], "passage":["NOUN"], "extract":["NOUN"]}})

def topic_rank(text):
    # Perform fact extraction on overall summary and segment summaries
    doc = nlp(text)

    # Create list of top 3 ranked phrases
    phrases = [phrase.text for phrase in doc._.phrases[:3]]

    return phrases