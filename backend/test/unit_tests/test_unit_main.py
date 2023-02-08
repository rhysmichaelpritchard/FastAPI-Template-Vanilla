from app import main

def test_get_probe_question_likes():
    response = main.get_probe_question("option_1")
    assert response == {"option": "option_1" ,"question": "You chose Option 1!"}
    response = main.get_probe_question("option_2")
    assert response == {"option": "option_2" ,"question": "You chose Option 2!"}