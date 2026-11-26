from filewatch import scan_folder

def test_added(tmp_path):
    (tmp_path / "a.txt").write_text("hi")
    old = scan_folder(tmp_path)
    (tmp_path / "b.txt").write_text("new")
    new = scan_folder(tmp_path)
    assert "b.txt" in [f for f in new if f not in old]

def test_modified(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("hi")
    old = scan_folder(tmp_path)
    p.write_text("changed")
    new = scan_folder(tmp_path)
    assert new["a.txt"] != old["a.txt"]

def test_deleted(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("hi")
    old = scan_folder(tmp_path)
    p.unlink()
    new = scan_folder(tmp_path)
    assert "a.txt" not in new

def test_no_changes(tmp_path):
    (tmp_path / "a.txt").write_text("hi")
    old = scan_folder(tmp_path)
    new = scan_folder(tmp_path)
    assert old == new

def test_subfolder(tmp_path):
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "b.txt").write_text("hi")
    data = scan_folder(tmp_path)
    assert any("b.txt" in k for k in data)