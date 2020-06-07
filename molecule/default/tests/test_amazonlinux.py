import pytest

testinfra_hosts = ["amazonlinux"]


@pytest.mark.parametrize("name", [
    ("automake"),
    ("bison"),
    ("gcc"),
    ("gzip"),
    ("gdbm-devel"),
    ("libffi-devel"),
    ("libyaml-devel"),
    ("make"),
    ("ncurses-devel"),
    ("openssl-devel"),
    ("readline-devel"),
    ("tar"),
    ("zlib-devel"),
])
def test_amazon_ruby_build_dependencies(host, name):
    pkg = host.package(name)
    assert pkg.is_installed
