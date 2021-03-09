import re
from unittest import TestCase


class Asser(TestCase):

    def ass(self,first, second):
        """
        :param first: 预期结果
        :param second: 实际结果
        :return:
        """
        first_result = ''
        second_result = ''
        first_msg = re.finditer('[\u4e00-\u9fa50-9-~]', str(first))
        for c in first_msg:
            d = c.group()
            first_result += d
        second_msg = re.finditer('[\u4e00-\u9fa50-9-~]', str(second))
        for e in second_msg:
            f = e.group()
            second_result += f
        if len(first_result) == 0 and len(second_result) == 0:
            self.assertEqual(first=first,second=second)
        elif first_result in second_result:
            return True
        else:
            raise AssertionError("预期结果:{}!=实际结果:{}".format(first,second))

if __name__ == '__main__':
    # ass = Asser()
    aa = {'password': ['仅允许6-20个字符的密码'], 'password_confirm': ['仅允许6~20个字符的确认密码']}
    bb = {'password': ['仅允许6-20个字符的密码'], 'password_confirm': ['仅允许6~20个字符的确认密码']}
    first_result = ''
    second_result = ''
    first_msg = re.finditer('[\u4e00-\u9fa50-9-~]', str(aa))
    for c in first_msg:
        d = c.group()
        first_result += d
    second_msg = re.finditer('[\u4e00-\u9fa50-9-~]', str(bb))
    for e in second_msg:
        f = e.group()
        second_result += f

    if len(first_result) == 0 and len(second_result) == 0:
        print("都是字母")

    elif first_result in second_result:
        print(first_result,second_result)
        print('成功')
    else:
        print(first_result)
        print(second_result)
        raise AssertionError("预期结果:{}!=实际结果:{}".format(aa, bb))


