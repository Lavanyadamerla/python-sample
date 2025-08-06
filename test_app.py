from app import greet

def test_greet():
    result = greet("Lavanya")
    print("Test greet output:", result)
    assert result == "Hello, Lavanya!"
