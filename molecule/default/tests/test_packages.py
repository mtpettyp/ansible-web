import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu-jammy-web')

"""Role testing packages using testinfra."""


@pytest.mark.parametrize("package", [
    ("nginx"),
    ("cron")
])
def test_packages(host, package):
    """Test that the appropriate packages were installed."""
    assert host.package(package).is_installed
