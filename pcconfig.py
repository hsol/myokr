import pynecone as pc
import os
from dotenv import load_dotenv


def get_mysql_db_url():
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT")
    username = os.environ.get("DB_USERNAME")
    password = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")

    assert all(
        filter(lambda i: i is not None, (username, password, db_name))
    ), "DB 정보를 정확히 입력해주세요."

    return f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}"


load_dotenv()
config = pc.Config(
    app_name="app",
    deploy_url="https://my-o.kr",
    db_url=get_mysql_db_url(),
    env=os.environ.get("APP_ENVIRONMENT") or pc.Env.DEV,
    api_url=os.environ.get("API_URL") or pc.constants.API_URL,
)
