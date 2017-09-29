import vcr
import os
import pytest

from testobject import TestObject
from testobject import Devices

@pytest.fixture
def to():
    username = os.environ.get('TO_USERNAME', None)
    api_key = os.environ.get('TO_API_KEY', None)

    return TestObject(username, api_key)

@vcr.use_cassette('tests/vcr_cassettes/all-devices.yml')
def test_get_devices(to):

    response = to.devices.get_devices()


    assert response, dict


@vcr.use_cassette('tests/vcr_cassettes/available-devices.yml')
def test_get_available_devices(to):

    response = to.devices.get_available_devices()


    assert response, dict


@vcr.use_cassette('tests/vcr_cassettes/device.yml')
def test_get_device(to):

    device_name = 'iPhone_5_free'

    response = to.devices.get_device(device_name)


    assert response, dict
    assert response['US']['id'] == device_name