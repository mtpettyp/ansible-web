import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu-jammy-web')

"""Role testing nginx using testinfra."""


def test_crontab(host):
    """Validate that the crontab is setup """
    crontab = host.file("/var/spool/cron/crontabs/root")
    assert crontab.exists
    assert crontab.contains('PATH="/usr/sbin:/usr/local/bin"')
    assert crontab.contains("@weekly certbot renew && service nginx reload")
