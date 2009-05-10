# -*- Python -*-
import sys, os
import misc, Utils, Build, Options

srcdir = '.'
blddir = 'build'

def set_options(opt):
    opt.tool_options('python')
    opt.tool_options('compiler_cc')

def configure(conf):
    conf.check_tool('compiler_cc')
    conf.check_tool('python')
    conf.check_tool('misc')
    conf.check_python_version((2,4,2))
    conf.check_python_headers()
    conf.env.append_value('CCFLAGS', ['-g', '-Wall', '-O2'])

    # supposedly, this should throw ConfigurationError on failure
    # or something.
    r = conf.check_cfg(package='lua', atleast_version='5.1')
    if r is not None:
        conf.check_cfg(package='lua', args='--cflags', uselib_store='LUA')
        conf.check_cfg(package='lua', args='--libs', uselib_store='LUALIB')
    else:
        lua = conf.find_program('lua', var='LUA')
        lua_path = os.path.normpath(os.path.join(os.path.dirname(lua), '..'))
        conf.env['CPPPATH_LUA'] = [os.path.join(lua_path, 'include')]
        conf.env['LIBPATH_LUALIB'] = [os.path.join(lua_path, 'lib')]
        conf.env['LIB_LUALIB'] = ['lua']

    # I've never seen a shared library on OS X with extension .bundle;
    # that's used for an actual bundle of files (directory with a special
    # flag set). So use .so instead (could use .dylib, but Lua by default
    # looks for .so, and most everything else is ok with .so instead of .dylib)
    conf.env['macbundle_PATTERN'] = '%s.so'


def build(bld):
    lua_in_py_mod = bld.new_task_gen(
        features = 'cc cshlib pyext',
        source = ['src/luainpython.c', 'src/pythoninlua.c'],
        target = 'lua',
        uselib = 'LUA LUALIB')
    # We can't just copy the above .so, as that links in Lua, and you can
    # only have one version of Lua in your program
    py_in_lua_mod = bld.new_task_gen(
        features = 'cc cshlib pyembed',
        source = ['src/luainpython.c', 'src/pythoninlua.c'],
        target = 'python',
        uselib = ['LUA'])
    if sys.platform == 'darwin':
        py_in_lua_mod.mac_bundle = True


def check(ctx):
    # PYTHONPATH=build/default python tests/test_lua.py
    # LUA_CPATH='build/default/?.so;;' lua tests/test_py.lua

    variant = 'default'

    environ = os.environ.copy()
    pypath = environ.get('PYTHONPATH', None)
    bpath = os.path.join(Build.bld.bldnode.abspath(), variant)
    env['PYTHONPATH'] = bpath + ':' + pypath if pypath else bpath
    luapath = environ.get('LUA_CPATH', None)
    bpath += '/?.so'
    env['LUA_CPATH'] = bpath + ';' + luapath if luapath else bpath + ';;'

    Utils.exec_command(['python', 'tests/test_lua.py'],
                       env=environ)
    Utils.exec_command(['lua', 'tests/test_py.lua'],
                       env=environ)
