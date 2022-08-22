import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu-focal-web')

"""Role testing nginx using testinfra."""


@pytest.mark.parametrize("site", [
    ("example.com")
])
def test_static_sites(host, site):
    """Validate that the static nginx sites are setup """
    assert host.file(f"/etc/nginx/sites-available/{site}").exists
    assert host.file(f"/var/www/{site}/html/index.html").exists
    assert host.file(f"/etc/nginx/sites-available/{site}") \
               .contains("try_files $uri $uri/ =404;")


@pytest.mark.parametrize("site", [
    ("proxied.example.com")
])
def test_proxy_sites(host, site):
    """Validate that the proxied nginx sites are setup """
    assert host.file(f"/etc/nginx/sites-available/{site}").exists
    assert host.file(f"/etc/nginx/sites-available/{site}") \
               .contains("proxy_pass http://127.0.0.1:8009/;")
