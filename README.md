# 出勤管理

この Django プロジェクトでは、簡単な出勤管理アプリケーションを提供します。

## セットアップ

1. （任意）仮想環境を作成して有効化します。
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. 必要なパッケージをインストールします。
   ```bash
   pip install django
   ```
3. マイグレーションファイルを作成してデータベースを初期化します。
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   `no such table: django_session` と表示された場合は、上記のマイグレーションを実行していない可能性があります。
4. 開発サーバーを起動します。
   ```bash
   python manage.py runserver
   ```
5. （任意）管理サイトにアクセスするためのスーパーユーザーを作成します。
   ```bash
   python manage.py createsuperuser
   ```

デフォルトのデータベースはプロジェクト直下の `db.sqlite3` を使用します。
