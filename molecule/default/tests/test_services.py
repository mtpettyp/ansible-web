import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu-focal-web')

"""Role testing services using testinfra."""


@pytest.mark.parametrize("name", [
    ("nginx"),
    ("cron")
])
def test_services(host, name):
    """Validate that services are enabled and running """
    service = host.service(name)
    assert service.is_enabled
    assert service.is_running
