from elasticsearch import Elasticsearch

# Elasticsearch 서버에 연결
es_host = "http://localhost:9200"
es = Elasticsearch([es_host]) 

# 'my_index' 인덱스의 'content' 필드에서 'example'를 검색하는 쿼리 실행
res = es.search(index="my_index", q="content:example")
print(res['hits']['hits'])
