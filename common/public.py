import base64
from pathlib import Path

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA



class Public(object):
    def get_object_path(self):
        #
        current_file_path = Path(__file__).resolve()
        #
        project_root = current_file_path.parent.parent
        return str(project_root)





    # def get_rsa_public_key(self, operate_type, password, last_ip=None, is_auth: bool = False):
    #     """
    #
    #     :param operate_type: #加密操作类型
    #     register通行证注册、login通行证登录、forget通行证忘记密码、modify通行证修改密码、tradeLogin交易账号登录、
    #     tradeSet交易账号设置密码、tradeForget交易账号忘记密码、tradeModify交易账号修改密码、tradeVerify交易账号密码校验
    #     :param password:加密的密码(明文)
    #     :param last_ip:获取公钥所需的ip地址
    #     :param is_auth:布尔类型，默认鉴权，True、False
    #     :return:
    #     """
    #     if last_ip is not None:
    #         # 获取rsa公钥
    #         get_rsa_data = {"operateType": operate_type, 'ip': last_ip}
    #     else:
    #         get_rsa_data = {"operateType": operate_type}
    #     # self.case('获取RSA公钥', get_rsa_data, file_name="public").run()
    #     if is_auth:
    #         self.case('登录后获取RSA公钥', get_rsa_data, file_name="public").run()
    #     else:
    #         self.case('登录前获取RSA公钥', get_rsa_data, file_name="public").run()
    #     # rsa_public_key = VariablesGlobal.get("${RsaPublicKey}")
    #     # # 加密后的密码
    #     # e_password = rsa_encrypt(rsa_public_key, password)
    #     # VariablesGlobal.set_init_data("e_password", e_password)
    #     # return e_password



if __name__ == "__main__":
    res = Public().get_rsa_public_key1()
