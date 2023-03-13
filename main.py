
import sys
import os
import string
import re
import copy
import traceback
from decimal import Decimal

from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

from ui.window import Ui_MainWindow
from worker import process

from error import contentError, exceptError, simpleError

from openpyxl import load_workbook


class extraWidgets(object):
    # 基础消息框
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.infoIcon = QMessageBox.Icon(1)
        self.errorIcon = QMessageBox.Icon(3)
        self.questionIcon = QMessageBox.Icon(4)

    def errorMsg(self, emsg):
        baseBox = QMessageBox(self.mainwindow)
        baseBox.setIcon(self.errorIcon)
        baseBox.setText(str(emsg))
        baseBox.setDetailedText(emsg.detailedMSG)
        baseBox.exec()
  
    def fieleChoose(self):
        dlog_fileChoose = QFileDialog(self.mainwindow)
        dlog_fileChoose.setFileMode(QFileDialog.ExistingFiles)
        dlog_fileChoose.setViewMode(QFileDialog.Detail)
        # 设置文件过滤器
        dlog_fileChoose.setNameFilter("All Compressed Fsiles (*.xlsx)")

        if dlog_fileChoose.exec_():
            return dlog_fileChoose.selectedFiles()


class extraFunc:
    @staticmethod
    def guessSheetXY(sheet: any) -> dict:
        # 获取表格的title的最大探测行数
        maxRowDetection = 8
        maxColumnDetection = 8

        rowBegin = 1
        sheetXY = {}.fromkeys(("row", "column"), 0)
        while rowBegin <= maxRowDetection:
            columnBegin = 1
            for y in range(maxColumnDetection):
                if sheet.cell(row=rowBegin, column=columnBegin).value:
                    sheetXY["row"] = rowBegin
                    sheetXY["column"] = columnBegin
                    break
                columnBegin += 1
            if sheetXY["row"] and sheetXY["column"]:
                break
            rowBegin += 1
        return sheetXY

    @staticmethod
    def getRanged(desc: str)-> (range, str):
        if desc:
            if desc[0] in string.digits and '-' in desc:
                # 区间的规则
                try:
                    _r = desc.split("-")
                    assert len(_r) == 2, "规则长度错误"
                except Exception as e:
                    return None, exceptError(traceback.format_exc(), reason=str(e))
                else:
                    # 规则字符串中的w字符的处理
                    start_base = end_base = 1
                    start = _r[0]
                    end = _r[1]
                    if "w" in start or "W" in start:
                        start_base = 10000
                        start = start.replace("w", "").replace("W", "")
                    if "w" in end or "W" in end:
                        end_base = 10000
                        end = end.replace("w", "").replace("W", "")

                    # 规则区间数字大小限制
                    try:
                        assert int(float(start) *  start_base) < int(float(end) * end_base), "规则错误（a-b;a<b）"
                    except Exception as e:
                        return None, exceptError(traceback.format_exc(), reason=str(e))
                    
                    try:
                        assert (float(start) * start_base).is_integer() is True, "区间开始不能有小数"
                        assert (float(end) * end_base).is_integer() is True, "区间结束不能有小数"
                    except Exception as e:
                        return None, exceptError(traceback.format_exc(), reason=str(e))

                    return range(int(float(start) * start_base),  int(float(end) * end_base)), None
            else:
                # 金额base
                base = 1
                p = desc
                if  "w" in desc or "W" in desc:
                    base = 10000
                    p = p.replace("w", "").replace("W", "")
                # >,>=,<,<=,= 的情况
                matched = False
                if ">=" in desc and not matched:
                    matched = True
                    # 大于等于情况
                    p = p.replace(">=", "")
                    rge = range(int(float(p)* base) - 1, 100000000)

                if ">" in desc and not matched:
                    matched = True
                    # 大于情况
                    p = p.replace(">", "")
                    rge = range(int(float(p)* base) + 1, 100000000)

                if "<=" in desc and not matched:
                    matched = True
                    # 小于等于情况
                    p = p.replace("<=", "")
                    rge = range(0, int(float(p)* base) + 1)

                if "<" in desc and not matched:
                    matched = True
                    # 小于情况
                    p = p.replace("<", "")
                    rge = range(0, int(float(p)* base))

                if "=" in desc and not matched:
                    matched = True
                    # 等于的情况
                    p = p.replace("=", "")
                    rge =  range(int(float(p)* base), int(float(p)* base)+1)
                try:
                    assert (float(p) * base).is_integer() is True, "区间不能有小数"
                except Exception as e:
                    return None, exceptError(traceback.format_exc(), reason=str(e))
                return rge, None
        else:
            return None, simpleError("规则为空")

        return None, simpleError("规则格式未知")

class excelSourceProcess(extraFunc):
    def setup(self, s):
        # 额外的Widget初始化
        self.extr_widget = extraWidgets(self)

        self.configFileAnalysisDone = False

        self.step1ConfigFileChooseBT.clicked.connect(lambda: self.configFileHandler())
        self.step1SourceFileChooseBT.clicked.connect(lambda: self.sourceFileHandler())
        
        
        # 分析
        self.step1ProcessBT.clicked.connect(lambda: self.step1ProcessWorker())
        self.processWorkerThread = process.step1ProcessWorker()
        self.processWorkerThread.signalProgress.connect(self.handleProgress)
        self.processWorkerThread.signalError.connect(self.handleError)

        # 导出
        # self.step1ExportBT.clicked.connect(lambda: self.step1ExportWorker())
        # self.importThread = process.ImportThread()
        # self.importThread.signalProgress.connect(self.handleProgress)
        # self.importThread.signalError.connect(self.handleError)
    
    def handleError(self, error):
        self.extr_widget.errorMsg(error)
        return

    def handleProgress(self, stage, progress):
        self.progressBar.setValue(progress)


    def analysisConfigFile(self):
        excel_file = self.step1ConfigFileChooseRV.text()
        if not os.path.exists(excel_file):
            self.extr_widget.errorMsg(simpleError("配件、折扣信息配置Excel文件：【{}】不存在".format(excel_file)))
            return

        configs = {}.fromkeys(["peijian", "discount", "activity"], {})

        try:
            conf_excel = load_workbook(filename=excel_file, read_only=True)
        except Exception as e:
            except_error = exceptError(
                traceback.format_exc(),
                reason="配件、折扣信息配置Excel文件：【{}】打开失败".format(excel_file)
            )
            self.extr_widget.errorMsg(except_error)
            return
        else:
            self.comboBox_3.clear()
            self.comboBox.clear()
            self.comboBox_2.clear()
            # todo 默认按照预定的sheetname进行数据查找
            index = 0
            for sheet_name in conf_excel.sheetnames:
                self.comboBox_3.insertItem(index, sheet_name)
                self.comboBox_3.setItemData(index, sheet_name)
                self.comboBox.insertItem(index, sheet_name)
                self.comboBox.setItemData(index, sheet_name)
                self.comboBox_2.insertItem(index, sheet_name)
                self.comboBox_2.setItemData(index, sheet_name)
                index += 1
            # ======================================================================================================
            # 产品及配件价格表
            if "产品及配件价格表" not in conf_excel.sheetnames:
                self.extr_widget.errorMsg(simpleError("【产品及配件价格表】不存在，请检查"))
                return
            else:
                sheet_price = conf_excel["产品及配件价格表"]
                # 样例数据（配件价格表）
                # {
                #     "餐具": {"GuiGe": ["5套"], "JiaGe": 5},
                #     "数字蜡烛": {"GuiGe": ["数字0", "数字1"], "JiaGe": 5},
                # }
                valid_HPMC = ["餐具", "派对生日蜡烛", "生日蜡烛", "生日帽", "数字蜡烛", "运费/差价"]
                peijian_config = {}.fromkeys(valid_HPMC)
                guessXY = self.guessSheetXY(sheet_price)

                if guessXY["row"] and guessXY["column"]:
                    index = 1
                    while True:
                        HuoPinMingCheng = sheet_price.cell(row= guessXY["row"] + index, column=guessXY["column"] + 1).value
                        GuiGe = sheet_price.cell(row= guessXY["row"] + index , column=guessXY["column"] + 2).value
                        JiaGe = sheet_price.cell(row= guessXY["row"] + index, column=guessXY["column"] + 3).value
                        if HuoPinMingCheng and GuiGe and JiaGe:
                            if HuoPinMingCheng in peijian_config:
                                if peijian_config[HuoPinMingCheng] is None:
                                    peijian_config[HuoPinMingCheng] = {
                                        "GuiGe": [], "JiaGe": Decimal(0).quantize(Decimal("0.00"))
                                    }
                                    peijian_config[HuoPinMingCheng]["GuiGe"].append(GuiGe)
                                    peijian_config[HuoPinMingCheng]["JiaGe"]=Decimal(JiaGe).quantize(Decimal("0.00"))
                                else:
                                    peijian_config[HuoPinMingCheng]["GuiGe"].append(GuiGe)
                        else:
                            break
                        index += 1
                else:
                    self.extr_widget.errorMsg(simpleError("表格未找到任何值，可能是个空表格？"))
                    return
                configs["peijian"] = peijian_config
            # ======================================================================================================
            
            # ------------------------------------------佳满勇气--各渠道折扣--------------------------------------------
            # 佳满勇气--各渠道折扣
            # 折扣信息描述语言使用规则语言这一列
            # 样例数据（配件价格表）
            # {
            #     "福多多": [(<RangeObject>, "%90"), (<RangeObject>, "%78")],
            #     "蛋糕叔叔": [(<RangeObject>, "%78")]
            # }
            discount_config = {}
            if "佳满勇气--各渠道折扣" not in conf_excel.sheetnames:
                self.extr_widget.errorMsg(simpleError("【佳满勇气--各渠道折扣】不存在，请检查"))
                return
            else:
                sheet_discount = conf_excel["佳满勇气--各渠道折扣"]
                guessXY = self.guessSheetXY(sheet_discount)
                if guessXY["row"] and guessXY["column"]:
                    index1 = 1
                    while True:
                        QuDaoMingCheng = sheet_discount.cell(row=guessXY["row"] + index1, column=guessXY["column"]).value
                        GuiZeYuYan = sheet_discount.cell(row=guessXY["row"] + index1, column=guessXY["column"]+2).value
                        ZheKou = sheet_discount.cell(row=guessXY["row"] + index1, column=guessXY["column"]+3).value
                        
                        # 折扣没有填写，则默认没有折扣
                        if ZheKou is None:
                            ZheKou = 1.0

                        if QuDaoMingCheng:
                            range_obj, error_msg = self.getRanged(GuiZeYuYan)
                            if error_msg is not None:
                                self.extr_widget.errorMsg(error_msg)
                            else:
                                # 向数组中添加range对象和折扣信息
                                if QuDaoMingCheng in discount_config:
                                    discount_config[QuDaoMingCheng].append((range_obj,ZheKou))
                                else:
                                    discount_config[QuDaoMingCheng] = []
                                    discount_config[QuDaoMingCheng].append((range_obj,ZheKou))
                        else:
                            break
                        index1 += 1
                else:
                    self.extr_widget.errorMsg(simpleError("表格未找到任何值，可能是个空表格？"))
                    return

                configs["discount"] = discount_config

            # ------------------------------------------佳满勇气--各渠道折扣--------------------------------------------


            # ¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥各渠道活动¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
            # 各渠道活动
            # ¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥各渠道活动¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
            conf_excel.close()

        self.configFileAnalysisDone = True
        return configs

    def step1ProcessWorker(self):
        if self.configFileAnalysisDone:
            params = {
                "source_file": self.step1SourceFileChooseRV.text(),
                "source_sheet": self.step1SourceDataSheetSelect.currentData(),
                "guessSheetXY": self.guessSheetXY,
                "configs": self.analysisConfigFile()
            }
            self.processWorkerThread.runParams(**params)
            self.processWorkerThread.start()
        else:
            self.extr_widget.errorMsg(simpleError("配件信息配置分析出错，请检查后在继续"))
            return

    def step1ExportWorker(self): pass

    def configFileHandler(self):
        filename = self.extr_widget.fieleChoose()
        if filename:
            self.step1ConfigFileChooseRV.setText(filename[0])
        self.analysisConfigFile()

    def sourceFileHandler(self):
        filename = self.extr_widget.fieleChoose()
        if filename:
            self.step1SourceFileChooseRV.setText(filename[0])
        
        if not os.path.exists(self.step1SourceFileChooseRV.text()):
            self.extr_widget.errorMsg(simpleError("Excel文件：【{}】不存在".format(self.step1SourceFileChooseRV.text())))
            return

        sfile = load_workbook(filename=self.step1SourceFileChooseRV.text(), read_only=True)
        self.step1SourceDataSheetSelect.clear()
        self.step1SourceDataSheetSelect.insertItem(0, "选择月份数据")
        self.step1SourceDataSheetSelect.setItemData(0, None)
        index = 1
        for sname in sfile.sheetnames:
            self.step1SourceDataSheetSelect.insertItem(index, sname)
            self.step1SourceDataSheetSelect.setItemData(index, sname)
            index += 1
        self.step1SourceDataSheetSelect.setCurrentIndex(0)
        sfile.close()

class toolWindow(QMainWindow, Ui_MainWindow, excelSourceProcess):
    def __init__(self, parent=None):
        super(toolWindow, self).__init__()
        # 配置信息模版
        self.templateconfig = {}.fromkeys(("sid","sp","sn"))

        # 公司订单数据
        self.sourceExcels = ""
        self.sourceConfigs = []
        self.thirdExcels = []
        self.thirdConfigs = []

        # 初始化window对象
        self.setupUi(self)
        self.setup(self)

        # 额外的Widget初始化
        self.extr_widget = extraWidgets(self)

        self.sourceFileChooseBT.clicked.connect(lambda: self.sourceFileChooseHandler())
        # signal `currentTextChanged`
        self.sourceWS.currentTextChanged.connect(lambda text: self.workSheetChangeHandler(text, filesource="source"))

        self.thirdFileChooseBT.clicked.connect(lambda: self.thirdFileChooseHandler())
        self.thirdWS.currentTextChanged.connect(lambda text: self.workSheetChangeHandler(text, filesource="third"))

        # beginAnalysisBT
        # exportResultBT
        # self.scene_export_bt.clicked.connect(lambda: self.startExportThread())

        # # 计时器
        # self.timeThread = timeWorker.TimeThread()
        # self.timeThread.timer.connect(self.handleTime)
        # # 进度条设置区间数
        # self.analysisProgressBar.setMaximum(100)
        # self.analysisProgressBar.setMinimum(0)

    def sourceFileChooseHandler(self):
        # sourceWS
        filename = self.extr_widget.fieleChoose()

        if filename:
            self.sourceFileChooseReView.setText(filename[0])

        try:
            swb = load_workbook(filename=filename[0], read_only=True)
        except:
            pass
        else:
            self.sourceWS.clear()
            self.sourceWS.insertItem(0, "选择WorkSheet")
            self.sourceWS.setItemData(0, None)
            index = 1
            for sn in swb.sheetnames:
                self.sourceWS.insertItem(index, sn)
                self.sourceWS.setItemData(index, sn)
                index += 1 
            self.sourceWS.setCurrentIndex(0)
            swb.close()

    def workSheetChangeHandler(self, sheet_name, filesource=""):
        if sheet_name:
            if sheet_name  == "选择WorkSheet":
                return 
            sourcefilename = self.sourceFileChooseReView.text()
            swb = load_workbook(filename=sourcefilename, read_only=True)
            if sheet_name in swb.sheetnames:
                sheet = swb[sheet_name]

                guessXY = sefl.guessSheetXY(swb, sheet_name)
                
                if guessXY["row"] and guessXY["column"]:
                    # 每次选择都要清空数据
                    self.sourceOrderIDColumn.clear()
                    self.sourceOrderIDColumn.insertItem(0, "请选择列信息")
                    self.sourceOrderIDColumn.setItemData(0, None)
                    self.sourceOrderPriceColumn.clear()
                    self.sourceOrderPriceColumn.insertItem(0, "请选择列信息")
                    self.sourceOrderPriceColumn.setItemData(0, None)
                    self.sourceOrderNumberColumn.clear()
                    self.sourceOrderNumberColumn.insertItem(0, "请选择列信息")
                    self.sourceOrderNumberColumn.setItemData(0, None)
                    # 明确不是想要信息的字段
                    blocked = ["物流公司", "下单时间",  "配送方式", "物流单号", "手机", "订单来源", "订单类型", "省", "市", "客服备注", "应收邮资" 
                                "追加备注", "订单状态",  "标记", "发货仓库"]
                    

                    titles = []
                    while True:
                        value = sheet.cell(row=guessXY["row"], column=guessXY["column"]).value
                        if value:
                            if value not in blocked:
                                titles.append(value)
                        else:
                            break
                        guessXY["column"] = guessXY["column"] + 1
                    
                    index = 1
                    for t in titles:
                        # 填充订单-选择框
                        self.sourceOrderIDColumn.insertItem(index, t)
                        self.sourceOrderIDColumn.setItemData(index, t)

                        # 填充单价-选择框
                        self.sourceOrderPriceColumn.insertItem(index, t)
                        self.sourceOrderPriceColumn.setItemData(index, t)

                        # 填充数量-选择框
                        self.sourceOrderNumberColumn.insertItem(index, t)
                        self.sourceOrderNumberColumn.setItemData(index, t)
                        index += 1

            swb.close()

    def thirdFileChooseHandler(self):
        # thirdWS
        filename = self.extr_widget.fieleChoose()

        if filename:
            self.thirdFileChooseReView.setText(filename[0])

        try:
            twb = load_workbook(filename=filename[0], read_only=True)
        except:
            pass
        else:
            self.thirdWS.clear()
            self.thirdWS.insertItem(0, "选择WorkSheet")
            self.thirdWS.setItemData(0, None)
            index = 1
            for sn in twb.sheetnames:
                self.sourceWS.insertItem(index, sn)
                self.sourceWS.setItemData(index, sn)
                index += 1 
            self.thirdWS.setCurrentIndex(0)

            twb.close()


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon(":/image/icon/main.png"))
    w = toolWindow()
    w.show()
    sys.exit(app.exec_())