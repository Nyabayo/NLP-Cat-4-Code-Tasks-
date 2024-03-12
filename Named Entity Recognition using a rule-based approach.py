import spacy
from spacy.pipeline import EntityRuler

def create_custom_ner_model():
    # Load the existing spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Initialize the EntityRuler and define custom entity patterns
    patterns = [
        {"label": "ORG", "pattern": [{"LOWER": "openai"}]},
        {"label": "GPE", "pattern": [{"LOWER": "san"}, {"LOWER": "francisco"}]},
        {"label": "PERSON", "pattern": [{"LOWER": "elon"}, {"LOWER": "musk"}]},
        {"label": "PERSON", "pattern": [{"LOWER": "ernest"}, {"LOWER": "osindo"}]},  # Custom pattern for Ernest Osindo
        {"label": "ORG", "pattern": "ENOTECH"},  # Custom pattern for ENOTECH
        {"label": "GPE", "pattern": [{"LOWER": "meru"}, {"LOWER": "kenya"}]}  # Custom pattern for Meru, Kenya
    ]

    ruler = EntityRuler(nlp, overwrite_ents=True)
    ruler.add_patterns(patterns)
    
    # Add the EntityRuler to the pipeline
    nlp.add_pipe("entity_ruler").add_patterns(patterns)

    return nlp

def recognize_named_entities(text):
    # Utilize the custom NER model
    nlp = create_custom_ner_model()

    # Process the given text
    doc = nlp(text)

    # Extract and return entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example text for entity recognition
text = "Ernest Osindo founded ENOTECH, which is based in Meru, Kenya."

# Execute the function and print recognized entities
entities = recognize_named_entities(text)
print(entities)
