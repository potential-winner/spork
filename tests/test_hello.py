from spork.hello import hello_to

def test_hello_to_aziz():
    result = hello_to("aziz")
    assert result == "Hello, aziz"
