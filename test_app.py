from app import app

def test_root():
    c = app.test_client()
    r = c.get("/")
    assert r.data == b"Hello Jenkins!"
