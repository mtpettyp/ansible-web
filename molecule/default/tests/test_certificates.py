import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu-jammy-web')

"""Role testing services using testinfra."""


@pytest.mark.parametrize("site", [
    ("example.com")
])
def test_certificates(host, site):
    """Validate that the letsencrypt certificates are set up """
    assert host.file(f"/etc/letsencrypt/live/{site}/fullchain.pem").exists
    assert host.file(f"/etc/letsencrypt/live/{site}/privkey.pem").exists

    site_conf = host.file(f"/etc/nginx/sites-available/{site}")
    assert site_conf.exists
    assert site_conf.contains(
        f"/etc/letsencrypt/live/{site}/fullchain.pem")
    assert site_conf.contains(f"/etc/letsencrypt/live/{site}/privkey.pem")


def test_cron(host):
    """Validate that the letsencrypt certificates are configured to renew """
    crontab = host.file("/var/spool/cron/crontabs/root")
    assert crontab.exists
    assert crontab.contains("@weekly certbot renew && service nginx reload")
