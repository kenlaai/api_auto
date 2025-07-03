import allure
from api_auto.common.all_api import AllApi
from api_auto.tools.get_log import logs


@allure.story("开户")
class TestOpenAccount(object):

    def test_openAccount(self):
        res = AllApi().send_request(file_path="open_account.yaml", api_name="获取账户列表")

        logs.logger.info(res)
        assert res['code'] == 0 and res['success'] == True

