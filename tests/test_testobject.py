import vcr
import os
import pytest

from testobject import TestObject

@pytest.fixture
def to():
    username = os.environ.get('TO_USERNAME', None)
    api_key = os.environ.get('TO_API_KEY', None)

    return TestObject(username, api_key)

@vcr.use_cassette('tests/vcr_cassettes/all-devices.yml', filter_headers=['authorization'])
def test_get_devices(to):

    response = to.devices.get_devices()


    assert response, dict


@vcr.use_cassette('tests/vcr_cassettes/available-devices.yml', filter_headers=['authorization'])
def test_get_available_devices(to):

    response = to.devices.get_available_devices()


    assert response, dict


@vcr.use_cassette('tests/vcr_cassettes/device.yml', filter_headers=['authorization'])
def test_get_device(to):

    device_name = 'iPhone_5_free'

    response = to.devices.get_device(device_name)


    assert response, dict
    assert response['US']['id'] == device_name


@vcr.use_cassette('tests/vcr_cassettes/get-device-ids.yml', filter_headers=['authorization'])
def test_get_devices_ids(to):

    response = to.suites.get_devices_ids(14)

    assert response, dict

@vcr.use_cassette('tests/vcr_cassettes/update-suite.yml', filter_headers=['authorization'])
def test_update_suite(to):
    data = {}
    data['title'] = "MY NAME CHANGING SUITE"


    response = to.suites.update_suite(14, data)

    assert response, dict

@vcr.use_cassette('tests/vcr_cassettes/start-suite.yml', filter_headers=['authorization'])
def test_start_suite(to):
    report = {'className': 'TOSuiteTest', 'dataCenterId': 'US', 'methodName': 'testMethod', 'deviceId': 'iPhone_5_free'}
    data = [report]

    response = to.suites.start_suite(14, data)

    assert response, dict

@vcr.use_cassette('tests/vcr_cassettes/stop-suite.yml', filter_headers=['authorization'])
def test_stop_suite(to):

    response = to.suites.stop_suite(14, 17)

    assert response, dict

@vcr.use_cassette('tests/vcr_cassettes/stop-suite-test.yml', filter_headers=['authorization'])
def stop_suite_test(to):

    response = to.suites.stop_suite_test(14, 17, 63, True)

    assert response, dict

@vcr.use_cassette('tests/vcr_cassettes/skip-suite-test.yml', filter_headers=['authorization'])
def test_skip_test(to):

    response = to.suites.skip_suite_test(14, 11, 63)

    assert response, dict