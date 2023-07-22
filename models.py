from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # SQLAlchemyのインスタンスを作成します。これを使ってデータベース操作を行います。

class Task(db.Model):  # データベースのテーブルを表すクラスを定義します。このクラスの各インスタンスはテーブルの一行を表します。
    id = db.Column(db.Integer, primary_key=True)  # idという名前の列を作成します。これは整数型で、各行の主キー（一意な識別子）になります。
    content = db.Column(db.String(80), nullable=False)  # contentという名前の列を作成します。これは最大80文字の文字列型で、null（値がない状態）は許可されません。
