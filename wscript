# -*- Python -*-
import os
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
    conf.env.append_value('CCFLAGS', '-g')
    conf.env.append_value('CCFLAGS', '-Wall')

    if False:
        lua = conf.find_program('lua', var='LUA')
        conf.check_cc(header_name='lua.h', uselib_store='LUA')
        conf.check_cc(lib='lua', uselib_store='LUA')
    if False:
        lua_path = os.path.normpath(os.path.join(os.path.dirname(lua), '..'))
        conf.env['CPPPATH_LUA'] = [os.path.join(lua_path, 'include')]
        conf.env['LIBPATH_LUA'] = [os.path.join(lua_path, 'lib')]
        conf.env['LIB_LUA'] = ['lua']
    if True:
        conf.env['LUA'] = os.path.join(conf.cwd, 'lua', 'lua')
        conf.env['CPPPATH_LUA'] = [os.path.join(conf.cwd, 'lua')]
        conf.env['LIBPATH_LUA'] = [os.path.join(conf.cwd, 'lua')]
        conf.env['LIB_LUA'] = ['lua']

def build(bld):
    lua_in_py_mod = bld.new_task_gen(
        features = 'cc cshlib pyext',
        source = ['src/luainpython.c', 'src/pythoninlua.c'],
        target = 'lua',
        uselib = 'LUA')
    bld.add_group('sep')
    py_in_lua_mod = bld.new_task_gen(
        features = 'copy',
        source = ['lua.so'],
        target = ['python.so'],
        )

def check(ctx):
    # PYTHONPATH=build/default python tests/test_lua.py
    # LUA_CPATH='build/default/?.so;;' lua tests/test_py.lua

    variant = 'default'

    env = os.environ.copy()
    pypath = env.get('PYTHONPATH', None)
    bpath = os.path.join(Build.bld.bldnode.abspath(), variant)
    env['PYTHONPATH'] = bpath + ':' + pypath if pypath else bpath
    luapath = env.get('LUA_CPATH', None)
    bpath += '/?.so'
    env['LUA_CPATH'] = bpath + ';' + luapath if luapath else bpath + ';;'

    Utils.exec_command(['python', 'tests/test_lua.py'],
                       env=env)
    Utils.exec_command(['lua', 'tests/test_py.lua'],
                       env=env)
