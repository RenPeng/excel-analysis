class baseError(object):
    etype = "default"
    def __init__(self, reason):
        # 错误消息主要提示信息
        self.reason = reason

    def __str__(self):
        return "{} Error: {}".format(self.etype.upper(), self.reason)

    @property
    def detailedMSG(self):
        return ""

class simpleError(baseError):
    etype = "simple"

    def __init__(self, reason):
        # 简单错误只有描述
        super(simpleError,self).__init__(reason)


class contentError(baseError):
    etype = "conent"

    def __init__(self, reason, content):
        # 内容错误只返回的内容和期待的不一致
        super(contentError, self).__init__(reason)

        self.content = content

    @property
    def detailedMSG(self):
        if type(self.content) == str:
            return self.content
        elif type(self.content) == dict:
            return json.dumps(self.content)
        else:
            return str(self.content)

class exceptError(baseError):
    etype = "except"

    def __init__(self, traceback, reason=""):
        # 异常错误只有异常的tracebak内容
        default_reason = "程序在运行过程中发生了未知的异常"
        if not reason:
            self.except_reason = default_reason
        else:
            self.except_reason = reason
        
        self.traceback = traceback
        super(exceptError, self).__init__(self.except_reason)

    @property
    def detailedMSG(self):
        return self.traceback