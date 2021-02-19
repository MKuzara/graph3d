from ursina import Path, FileBrowser as Browser
import os

FILE_DATA = ''

class FileBrowser(Browser):

    def __init__(self, *args, **kwargs):
        cwd = os.getcwd()
        super().__init__(
            start_path=Path(cwd),
            *args, **kwargs
        )

        def open(self):
            super().open()
            print(self.path)

        def on_submit(self):
            with open(self.path, 'r') as f:
                global FILE_DATA
                FILE_DATA = f.read()
            print(FILE_DATA)