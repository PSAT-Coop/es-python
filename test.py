
from elasticsearch import Elasticsearch

# Elasticsearch 서버에 연결
es = Elasticsearch(["http://localhost:9200"])

# Elasticsearch 버전 확인
print(es.info())

# 인덱스 생성
es.indices.create(index='my_index')

# 문서 추가
doc = {'title': 'Elasticsearch Python Test', 'content': 'This is a test document.'}
es.index(index='my_index', document=doc)

# 검색
res = es.search(index='my_index', body={'query': {'match': {'content': 'test'}}})
print(res['hits']['hits'])
