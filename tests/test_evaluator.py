from src.evaluator import score_response

def test_numeric_match():
    assert score_response("40000", "40000")["reference_match"] == 1.0

def test_text_match():
    assert score_response("parallel trends", "The key assumption is parallel trends.")["reference_match"] == 1.0
