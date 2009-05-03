#!/usr/bin/python
from distutils.core import setup, Extension
import os

if os.path.isfile("MANIFEST"):
    os.unlink("MANIFEST")

# You may have to change these
LUA_LIBS = ["lua"]
LUA_INCDIR = ["/opt/local/include"]
LUA_LIBDIR = ["/opt/local/lib"]

setup(name="lunatic-python",
      version = "1.0",
      description = "Two-way bridge between Python and Lua",
      author = "Gustavo Niemeyer",
      author_email = "gustavo@niemeyer.net",
      url = "http://labix.org/lunatic-python",
      license = "LGPL",
      long_description =
"""\
Lunatic Python is a two-way bridge between Python and Lua, allowing these
languages to intercommunicate. Being two-way means that it allows Lua inside
Python, Python inside Lua, Lua inside Python inside Lua, Python inside Lua
inside Python, and so on.
""",
      ext_modules = [
                     Extension("lua",
                               ["src/pythoninlua.c", "src/luainpython.c"],
                               include_dirs=LUA_INCDIR,
                               library_dirs=LUA_LIBDIR,
                               libraries=LUA_LIBS),
                    ],
      )
