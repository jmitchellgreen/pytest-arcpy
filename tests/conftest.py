import pytest
import arcpy


pytest_plugins = "pytester"


@pytest.fixture
def data():
    return r"C:\Users\jmgreen\Documents\coding\pytest-arcpy\tests\data\point.shp"


@pytest.fixture
def exists(data):
    return arcpy.Exists(data)


@pytest.fixture
def describe(data):
    return arcpy.da.Describe(data)


@pytest.fixture
def get_spatial_attribute(describe):
    return describe["spatialReference"]


@pytest.fixture
def get_wkid(get_spatial_attribute):
    return get_spatial_attribute.factoryCode
