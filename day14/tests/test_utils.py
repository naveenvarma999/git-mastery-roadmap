from utils import add_task


def test_add_task():
    assert add_task("Learn Git") == "Learn Git"