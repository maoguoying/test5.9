import requests
import json
import unittest
from test_case import public1
list=[]
class Material(unittest.TestCase):
    def test_Material_Collection(self):
        headers={"Authorization":public1.token_syjc(),
        "Content-Type":"application/json"}
        url="http://10.1.0.213:30114/user/permission-collect-materials"
        payload={
        "materialsUuid":"TI_SN74LVTH541NS",
        "platformType":
        {
        "value":"1"
        }
        }
        data_json=json.dumps(payload)
        response=requests.post(url=url,data=data_json,headers=headers)
        # response = requests.post(url=url, json=payload, headers=headers)
        print(response.json())
        list.append(response.json())
        print(list)
        print(list[0]["msg"])
        self.assertEqual(list[0]["msg"],"SUCCESS")

# # 构造测试集
# def suite():
#     suite=unittest.TestSuite()
#     suite.addTest(Material("test_Material_Collection"))
#     return suite

# 测试
if __name__ == "__main__":
    unittest.main()



