import pytest

"""Role testing services using testinfra."""


@pytest.mark.parametrize("name", [
    ("nginx")
])
def test_services(host, name):
    """Validate that services are enabled and running """
    service = host.service(name)
    assert service.is_enabled
    assert service.is_running
