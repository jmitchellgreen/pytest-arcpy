class TestData:
    def test_exists(self, exists):
        assert exists == True

    def test_is_wgs84(self, get_wkid):
        assert get_wkid == 4326
