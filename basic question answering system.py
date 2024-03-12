import spacy

# Load the medium spaCy model
nlp = spacy.load("en_core_web_md")

# Expanded information paragraph
info_paragraph = """
Dr. Amos Chege is the lecturer for the BCT Natural Language Processing course, which is renowned for its comprehensive curriculum and hands-on learning approach. The course covers various topics, including machine learning, natural language understanding, and text analysis. Meru University of Science and Technology, where the course is offered, is located in Meru County. This institution is celebrated for its commitment to innovation and excellence in science and technology education. The campus is situated in a region known for its serene environment and conducive learning atmosphere.
"""

# Function to preprocess text and find the most relevant information in the paragraph
def find_relevant_info(question, paragraph):
    # Preprocess the paragraph into sentences
    paragraph_doc = nlp(paragraph)
    sentences = [sent.text for sent in paragraph_doc.sents]
    
    # Process the question
    question_doc = nlp(question)
    
    # Initialize variables to find the most similar sentence
    max_similarity = 0
    answer = "I'm sorry, I don't have the information to answer that question."
    
    # Compare the question to each sentence in the paragraph
    for sentence in sentences:
        sentence_doc = nlp(sentence)
        similarity = question_doc.similarity(sentence_doc)
        if similarity > max_similarity:
            max_similarity = similarity
            answer = sentence
    
    return answer

# Example questions
questions = [
    "What is the name of the BCT Natural Language Processing lecturer?",
    "In which county is Meru University of Science and Technology located?",
    "What topics does the BCT Natural Language Processing course cover?"
]

# Get answers from the QA system
for question in questions:
    answer = find_relevant_info(question, info_paragraph)
    print("Question:", question)
    print("Answer:", answer)
    print()
