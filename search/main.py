import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()
es_password = os.getenv("ES_PASSWORD")

es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=('elastic', es_password))