from elasticsearch import Elasticsearch

# Elasticsearch 서버에 연결
es_host = "http://localhost:9200"
es = Elasticsearch([es_host])

# 인덱스 생성
if not es.indices.exists(index='my_index'):
    es.indices.create(index='my_index')

# 문서 추가
doc = {'title': 'Example Document', 'content': 'This is an example document.'}
es.index(index='my_index', body=doc)