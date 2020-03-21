from spork.hello import hello_to, hello_world_and_to

def test_hello_to_aziz():
    result = hello_to("aziz")
    assert result == "Hello, aziz"

def test_hello_world_and_to_aziz():
    result = hello_world_and_to("aziz")
    assert result == "Hello, World and aziz"
