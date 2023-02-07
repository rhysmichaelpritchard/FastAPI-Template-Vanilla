from app import main

def test_get_probe_question_likes():
    response = main.get_probe_question("likes")
    assert response == {"model_name": "likes" ,"question": "What do you like about your new car?"}
    response = main.get_probe_question("dislikes")
    assert response == {"model_name": "dislikes" ,"question": "What do you dislike about your new car?"}