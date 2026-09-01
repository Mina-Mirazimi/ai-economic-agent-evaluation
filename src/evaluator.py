import re

def normalize(text):
    return re.sub(r"[^a-z0-9.\-]+", " ", str(text).lower()).strip()

def score_response(reference, response):
    ref, resp = normalize(reference), normalize(response)
    return {"reference_match": float(ref == resp or ref in resp)}
