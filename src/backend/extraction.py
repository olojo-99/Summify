import spacy
import pytextrank
from spacy.tokens import Span

# Define decorator for converting to singular version of words
@spacy.registry.misc("plural_scrubber")
def plural_scrubber():
    def scrubber_func(span: Span) -> str:
        return span.lemma_
    return scrubber_func


# Load a spaCy model
nlp = spacy.load("en_core_web_lg")


# Exclude stopwords that could be generated due to gpt3 completion
nlp.Defaults.stop_words |= {"transcript", "passage", "extract",
                            "term", "video", "segment",
                            "text", "paragraph", "paper",
                            "course", "lesson", "college",
                            "university", "lecture", "class", 
                            "theory", "principle", "concept"}

# Add TextRank component to pipeline with stopwords
nlp.add_pipe("textrank", config={
                        "stopwords": {token:["NOUN"] for token in nlp.Defaults.stop_words},
                        "scrubber": {"@misc": "plural_scrubber"}})


def text_rank(text):
    # Perform fact extraction on overall summary and segment summaries
    doc = nlp(text)

    # Create unique list of top 5 ranked phrases
    phrases = {phrase.text for phrase in doc._.phrases[:5]}

    return phrases