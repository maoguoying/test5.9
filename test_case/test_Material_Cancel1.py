import json
import unittest
import requests
from test_case import public1


list=[]
class Materiala(unittest.TestCase):
    def test_materrial_Cancel(self):
        headers={"Authorization": public1.token_syjc(),
                 "Content-Type":"application/json"}
        url="http://ms-gateway.local.hxyd/userapi/user/materials/collection"
        payload={
            "materialsUuid": "TI_SN74LVTH541NS",
            "platformType": {
                "value": "1"
            }
        }
        data_json=json.dumps(payload)
        response=requests.delete(url=url,data=data_json,headers=headers)
        print(response.json())
        list.append(response.json())
        print(list)
        print(list[0]["msg"])
        self.assertEqual(list[0]["msg"],"SUCCESS")
        
# # 构造测试集 
# def suite():
#     suite=unittest.TestSuite()
#     suite.addTest(Material("test_materrial_Cancel"))
#     return suite

# 测试
if __name__ == "__main__":
    # unittest.main(defaultTest = 'suite')
    unittest.main()

