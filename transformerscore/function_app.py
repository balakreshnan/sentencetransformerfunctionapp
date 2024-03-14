import azure.functions as func
import datetime
import json
import logging
import sentence_transformers
from sentence_transformers import SentenceTransformer
import json

app = func.FunctionApp()

def getSentence(name):
    returntext = "NA"
    try:
        model = SentenceTransformer("all-MiniLM-L6-v2")

        # Our sentences to encode
        sentences = [
            "This framework generates embeddings for each input sentence",
            "Sentences are passed as a list of string.",
            "The quick brown fox jumps over the lazy dog."
        ]
        embeddings = model.encode(sentences)

        returntext = str(embeddings)
        print(returntext)
    except Exception as e:
        returntext = str(e)

    return returntext

@app.route(route="http_trigger2", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    rstext = ""
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            rstext = getSentence(name)
            
    model = SentenceTransformer("all-MiniLM-L6-v2")

            # Our sentences to encode
    sentences = [
            "This framework generates embeddings for each input sentence",
            "Sentences are passed as a list of string.",
            "The quick brown fox jumps over the lazy dog."
        ]
    embeddings = model.encode(sentences)
    rstext = str(embeddings)
    print(str(embeddings))
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. Sentence Transformer output: {rstext}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )