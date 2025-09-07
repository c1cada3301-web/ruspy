from ruspy.transpiler import transpile_file
import os

def test_batch(tmp_path):
    src1 = tmp_path / "test1.py"
    src2 = tmp_path / "test2.py"
    out1 = tmp_path / "out1.py"
    out2 = tmp_path / "out2.py"
    src1.write_text("функция сумма(а, б):\n    вернуть а + б\n", encoding="utf-8")
    src2.write_text("функция приветствие(имя):\n    печать('Привет,', имя)\n", encoding="utf-8")
    transpile_file(str(src1), str(out1))
    transpile_file(str(src2), str(out2))
    assert out1.read_text(encoding="utf-8").strip() == "def sum(a, b):\n    return a + b"
    assert out2.read_text(encoding="utf-8").strip() == "def greeting(name):\n    print('Hello,', name)"
