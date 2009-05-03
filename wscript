srcdir = '.'
blddir = 'build'

def set_options(opt):
    opt.tool_options('python')
    opt.tool_options('compiler_cc')

def configure(conf):
    conf.check_tool('compiler_cc')
    conf.check_tool('python')
    conf.check_python_version((2,4,2))
    conf.check_python_headers()
    conf.env.append_value('CCFLAGS', '-g')
    conf.env.append_value('CCFLAGS', '-Wall')
    conf.env['CPPPATH_LUA'] = ['/opt/local/include']
    conf.env['LIBPATH_LUA'] = ['/opt/local/lib']
    conf.env['LIB_LUA'] = ['lua']

def build(bld):
    bld.new_task_gen(
        features = 'cc cshlib pyext',
        source = ['src/luainpython.c', 'src/pythoninlua.c'],
        target = 'lua',
        uselib = 'LUA')
