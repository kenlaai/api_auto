import pytest
from common.all_api import AllApi
from tools.get_log import get_log


@pytest.mark.account
class TestOpenAccount(object):

    def test_openAccount(self):
        res = AllApi().send_request(file_path="open_account.yaml", api_name="获取账户列表")

        get_log().info(res)
        assert res['code'] == 0 and res['success'] == True

