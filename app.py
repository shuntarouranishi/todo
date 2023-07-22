from flask import Flask, render_template, request, redirect, url_for
from models import db, Task

app = Flask(__name__)  # Flaskアプリケーションのインスタンスを作成します。
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # 使用するデータベースのURIを設定します。ここではSQLiteというデータベースを使い、そのファイルの場所を指定しています。
db.init_app(app)  # SQLAlchemyのインスタンスに、このFlaskアプリケーションを関連付けます。

@app.route('/', methods=['GET', 'POST'])  # ルート（http://localhost:5000/）に対するリクエストを処理する関数を定義します。GETリクエストとPOSTリクエストの両方を受け付けます。
def index():
    if request.method == 'POST':  # リクエストがPOSTの場合（つまり、新しいタスクが送信された場合）
        new_task = Task(content=request.form['content'])  # フォームから送信されたデータを使って新しいTaskインスタンスを作成します。
        db.session.add(new_task)  # 新しいタスクをデータベースセッションに追加します。しかし、まだデータベースには保存されません。
        db.session.commit()  # データベースセッションの変更を確定（コミット）します。これにより新しいタスクがデータベースに保存されます。
        return redirect(url_for('index'))  # ユーザーを同じページにリダイレクトします。
    tasks = Task.query.all()  # データベースからすべてのタスクを取得します。
    return render_template('index.html', tasks=tasks)  # 取得したタスクのリストをテンプレートエンジンに渡し、HTMLを生成して返します。

if __name__ == "__main__":
    app.run(debug=True)  # デバッグモードでアプリケーションを実行します。このモードでは、エラーメッセージが詳細に表示され、ソースコードが変更されると自動的にアプリケーションが再起動します。
