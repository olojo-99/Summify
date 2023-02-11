import spacy
import pytextrank
from spacy.tokens import Span

# define decorator for converting to singular version of words
@spacy.registry.misc("plural_scrubber")
def plural_scrubber():
    def scrubber_func(span: Span) -> str:
        return span.lemma_
    return scrubber_func


# Load a spaCy model
nlp = spacy.load("en_core_web_lg")


# Exclude stopwords that could be generated due to completion prompt
nlp.Defaults.stop_words |= {"transcript", "passage", "extract", "term", "video"}


# Add TopicRank component to pipeline with stopwords
nlp.add_pipe("topicrank", config={
                        "stopwords": {token:["NOUN"] for token in nlp.Defaults.stop_words},
                        "scrubber": {"@misc": "plural_scrubber"}})

def topic_rank(text):
    # Perform fact extraction on overall summary and segment summaries
    doc = nlp(text)

    # Create unique list of top 3 ranked phrases
    phrases = {phrase.text for phrase in doc._.phrases[:3]}

    return phrases