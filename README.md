# contrib extension

## Introduction

자신이 직접 라이브러리를 구현할때 contrib 형태의 라이브러리 관리를 사용한다면 contrib extension 라이브러리는 자신의 라이브러리의 root에서 하위 라이브러리를 접근하는 데에 도움을 줄 수 있습니다.

If you use library management in the form of a content library when you implement your own library, the content extension library can help you access sub libraries from the root of your library.

## Installation

```bash
pip install contrib-extension
```

## Use

```python
"""   
    - test
        - __init__.py
        - test.py # main
        - post.py
            - __category__ = "board"
            - __id__ = "post"
            - set(self) -> return "ok"
        - contrib
            - __init__.py
            - download.py 
            - __category__ = "board_ext"
            - __id__ = "download"
            - do(self) -> return "what?"
            - upload
            - __init__.py
                - __category__ = "board_ext"
                - __id__ = "upload"
            - upload.py
            - setting.py
                - __category__ = "board"
                - __id__ = "upload"
"""
from contrib_extension import Extension

class test:
    def __init__(self):
        self._ext_ = Extension(use_lib_name=test)
        print(self._ext_)
        """
        {
            "board_ext":{
                "download":<module>,
                "upload":<module>
            },
            "board":{
                "upload":<module>
            }
        }
        """
        self._ext_.importlib("post", False)
        print(self._ext_.get_info())
        """
        {
            "board_ext":{
                "download":<module>,
                "upload":<module>
            },
            "board":{
                "upload":<module>,
                "post":<module>
            }
        }
        """
        print(self._ext_)
        """
        {
            "board_ext":{
                "download":<module>,
                "upload":<module>
            },
            "board":{
                "upload":<module>,
                "post":<module>
            }
        }
        """

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
```

## About

이 프로젝트는 다른 프로젝트에 도움을 주기 위해 진행되었습니다. 지속적으로 업데이트를 통해 좀 더 나은 형태로 나아가겠습니다. 더 좋은 아이디어가 있다면 언제든지 연락바랍니다.

This project was undertaken to help other projects. We'll continue to update and move on to a better shape. Feel free to contact me if you have a better idea.

## Version

- v0.0.1.1909230047-rc
  - 미작동 오류 해결(Fix Error)

- v0.0.1.1908252311-rc
  - Private 프로젝트에서 분리(Detach from Private project)
  - 프로젝트 정리(Project theorem)

## License

MIT 라이선스로 공개되었습니다.

Released under the MIT license.
