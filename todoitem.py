# モジュールをインポート
from datetime import datetime, timedelta

class ToDoItem(object):
    """
    ToDo項目を保存するためのクラス
    """

def __init__(self, title, description, duedate, addedate=None):
    """
    ToDo項目インスタンスを初期化する
    """
    if not addedate:
        addedate = datetime.now()
    self.title = title # タイトル
    self.description = description # 解説
    self.duedate = duedate # 締切り日
    self.addedate = addedate # 追加日
    self.finished = False # 終了フラグ
    self.finisheddate = None # 終了日

def finish(self, date = None):
    """
    ToDo項目を終了する
    """
    self.finished = True
    if not date:
        date = datetime.now()
    self.finisheddate = date

def __repr__(self):
    """
    ToDo項目の表示形式文字列を作る
    """
    return "<ToDoItem {}, {}>".format(self.title, self.duedate.strftime('%Y/%m/%d %H:%M'))