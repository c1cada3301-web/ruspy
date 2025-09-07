from ruspy.transpiler import transpile_file
import os

def test_simple(tmp_path):
    src = tmp_path / "input.py"
    out = tmp_path / "output.py"
    src.write_text("функция приветствие(имя):\n    печать('Привет,', имя)\n", encoding="utf-8")
    transpile_file(str(src), str(out))
    result = out.read_text(encoding="utf-8").strip()
    assert result == "def greeting(name):\n    print('Hello,', name)"
