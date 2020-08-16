from google.cloud import language_v1
from google.cloud.language_v1 import enums


def analyze_sentiment(text_content):
    client = language_v1.LanguageServiceClient()
    sentence_scores = {}
    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    return str(response.document_sentiment.score)
    # Get sentiment for all sentences in the document
    # for index, sentence in enumerate(response.sentences):
    #     sentence_scores[index] = sentence.sentiment.score
