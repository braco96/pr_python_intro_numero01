import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


@pytest.mark.parametrize("v,tip,truth,rep", [
    (0, "int", False, "0"),
    (1, "int", True, "1"),
    ("", "str", False, ""),
    ("hola", "str", True, "hola"),
    ([], "list", False, "[]"),
    ([1], "list", True, "[1]"),
])
def test_describe_value(v, tip, truth, rep):
    t, b, s = mod.describe_value(v)
    assert t == tip
    assert b == truth
    assert s == rep
