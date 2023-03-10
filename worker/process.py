import traceback

from openpyxl import load_workbook
from PyQt5.QtCore import QThread, pyqtSignal

from error import simpleError, exceptError, baseError

class step1ProcessWorker(QThread):
    # 0: 阶段 1:进度 
    signalProgress = pyqtSignal(str, int)
    # 0: baseError
    signalError = pyqtSignal(baseError)

    def runParams(self, **params):
        self.params = params
    
    def run(self):
        self.params = {
            "source_file": self.step1SourceFileChooseRV.text(),
            "source_sheet": self.step1SourceDataSheetSelect.currentData()
        }

        try:
            sfile = load_workbook(filename=self.params["source_file"])
            sheet = sfile[self.params["source_sheet"]]
        except:
            self.signalError(exceptError(traceback.format_exc(), reason="源文件打开失败"))
            return

        # 将相关的业务需求【配置数据】处理好，然后导出的操作将按照【配置数据】将excel写入到新的sheet

        {
            "row_delete": ["row1", "row2"],
            "时间处理":1234,
            "QuDao": {
                "福多多": 11245
            }
        }

