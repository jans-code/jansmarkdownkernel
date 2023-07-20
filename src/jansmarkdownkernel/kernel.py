#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""jansmarkdownkernel"""

import os
import shutil
from IPython.display import Markdown, display
from ipykernel.kernelbase import Kernel

class jansmarkdownkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.14.0'
    language = 'Markdown'
    language_version = '1.0'
    language_info = {
        'name': 'Markdown',
        'mimetype': 'text/x-markdown',
        'file_extension': '.md',
    }
    banner = "Markdown"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            stream_content = {'metadata': {}, 'data': {'text/markdown': code}}
            self.send_response(self.iopub_socket, 'display_data', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }