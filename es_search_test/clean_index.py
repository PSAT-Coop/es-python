
from elasticsearch import Elasticsearch

# Elasticsearch 서버에 연결
es_host = "http://localhost:9200"
es = Elasticsearch([es_host])

# 인덱스 삭제
if es.indices.exists(index='my_index'):
    es.indices.delete(index='my_index')

# 인덱스 생성
es.indices.create(index='my_index')


# from elasticsearch import Elasticsearch

# # Elasticsearch 서버에 연결
# es_host = "http://localhost:9200"
# es = Elasticsearch([es_host])

# # my_index에 있는 모든 문서 삭제
# es.delete_by_query(index='my_index', body={'query': {'match_all': {}}})

