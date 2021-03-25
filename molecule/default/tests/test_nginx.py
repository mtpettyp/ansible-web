import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu-focal-web')

"""Role testing nginx using testinfra."""


@pytest.mark.parametrize("site", [
    ("example.com")
])
def test_sites(host, site):
    """Validate that the nginx sites are setup """
    assert host.file(f"/etc/nginx/sites-available/{site}").exists
    assert host.file(f"/var/www/{site}/html/index.html").exists
