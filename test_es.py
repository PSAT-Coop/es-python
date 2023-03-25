### elastic_search + python test code


from elasticsearch import Elasticsearch

# Elasticsearch 서버에 연결
es_host = "http://localhost:9200"
es = Elasticsearch([es_host]) ##자신의 로컬 내 es 주소를 적음 된다.

# Elasticsearch 버전 확인
print(es.info())

# 인덱스 생성 -> 인덱스가 이미 존재할 경우에(여기서는  my_index) 실행되지 않게
if not es.indices.exists(index='my_index'):
        es.indices.create(index='my_index')

        # 문서 추가
        doc = {'title': 'Elasticsearch Python Test', 'content': 'This is a test document.'}
        es.index(index='my_index', body=doc)

        # 검색
        res = es.search(index='my_index', body={'query': {'match': {'content': 'test'}}})
        print(res['hits']['hits'])

