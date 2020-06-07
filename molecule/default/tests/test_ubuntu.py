import pytest

testinfra_hosts = ["ubuntu"]


@pytest.mark.parametrize("name", [
    "automake",
    "bison",
    "build-essential",
    "gzip",
    "libffi-dev",
    "libgdbm-dev",
    "libncurses-dev",
    "libreadline-dev",
    "libssl-dev",
    "libyaml-dev",
    "make",
    "tar",
    "zlib1g-dev",
])
def test_ubuntu_ruby_build_dependencies(host, name):
    pkg = host.package(name)
    assert pkg.is_installed
