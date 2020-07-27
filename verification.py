import random


class randomCode(object):
    """
    生成验证码
    code_length: 验证码的长度
    """

    def __init__(self, code_length):
        self.code_length = code_length

    def __str__(self):
        return "%s" % self.generate

    @property
    def generate(self):
        while True:
            check_code = str()
            for i in range(self.code_length):
                current_code = random.randint(0, 4)

                # 生成数字和大写字母的组合
                if current_code == i:
                    check_code += str(chr(random.randint(65, 90)))
                else:
                    check_code += str(random.randint(0, 9))

            # 判断生成的验证码是否是数字和字母的组合
            if not check_code.isalpha() and not check_code.isnumeric():
                return check_code
            else:
                continue
