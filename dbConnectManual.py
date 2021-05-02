# docufreeDB.py 파일을 같은 폴더에 위치시킬 것
# docufreeDB 와 datetime을 import 시킬 것
import docufreeDB
import datetime

# DB에서 SELECT를 하고 싶을 시 docufreeDB.select() 함수 사용
# select() 함수 반환값으로 True 또는 False 
# 사용 예시
# MD5 = '098f6bcd4621d373cade4e832627b4f6'
# docufreeDB.select("SELECT * FROM hashtable WHERE md5 = %s", (MD5, ))

# DB에 INSERT를 하고 싶을 시 docufreeDB.insert() 함수 사용
# insert() 함수 반환값으로 True
# sql query식의 바인딩 된 값으로 튜플 값(), 리스트 값[] 으로 입력 가능
# 사용 예시
# values = ('MD5 hash value1', 'SHA1 ahsh value1', 'SHA256 hash value1', 'SHA512 hash value1', 'HAS160 hash value1', 'filename.확장자명', '확장자명', datetime.datetime.now())
# docufreeDB.insert("INSERT INTO hashtable (md5, sha1, sha256, sha512, has160, name, extension, created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", values)
# 사용 예시2
# values = [
#   ('MD5 hash value1', 'SHA1 ahsh value1', 'SHA256 hash value1', 'SHA512 hash value1', 'HAS160 hash value1', 'filename.확장자명', '확장자명', datetime.datetime.now()),
#   ('MD5 hash value2', 'SHA1 ahsh value2', 'SHA256 hash value2', 'SHA512 hash value2', 'HAS160 hash value2', 'filename.확장자명', '확장자명', datetime.datetime.now())]
# docufreeDB.insert("INSERT INTO hashtable (md5, sha1, sha256, sha512, has160, name, extension, created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", values)

# DB에 저장된 데이터를 수정하고 싶을 시 docufreeDB.update() 함수 사용
# update() 함수 반환값으로 True
# sql query식의 바인딩 된 값으로 튜플 값(), 리스트 값[] 으로 입력 가능
# 사용 예시
# docufreeDB.update("UPDATE hashtable SET name=%s WHERE id=%s", ('test.hwp', 6))

