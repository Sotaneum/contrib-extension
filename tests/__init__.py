from contrib_extension import Extension

class test:
    def __init__(self):
        self._ext_ = Extension(use_lib_name="test")
        print(self._ext_)
        self._ext_.importlib("post", False)
        print(self._ext_.get_info())
        print(self._ext_)

    def post(self, text):
        module = self._ext_.get_class("board","post")
        obj = module()
        print(obj.set())
        # ok
    
    def upload(self, data):
        module = self._ext_.get_class("board_ext","download")
        obj = module()
        print(obj.do())
        # what?

test()