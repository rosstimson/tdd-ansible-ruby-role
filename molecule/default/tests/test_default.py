import re

def test_ruby_executable_file(host):
    exe = host.file("/usr/local/bin/ruby")
    assert exe.user == "root"
    assert exe.group == "root"
    assert exe.mode == 0o755


def test_ruby_command(host):
    cmd = host.check_output("/usr/local/bin/ruby -v")
    assert re.match("^ruby 2.7.1*", cmd)
