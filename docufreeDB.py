# mariadb 모듈 선언
import mariadb

# connection을 선언하기 위한 파라미터값 user, password, host, port, database
docufreeUser={'user':"docufreeUser", 'password':"docufreeMaria1!", 'host':"35.233.216.2", 'port':3306, 'database':"docufree"}

try:
    # mairadb connection 선언
    conn=mariadb.connect(
        user=docufreeUser['user'],
        password=docufreeUser['password'],
        host=docufreeUser['host'],
        port=docufreeUser['port'],
        database=docufreeUser['database']
)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")


# DB에 데이터를 검색할 때 사용되는 함수
def select(query, values):
    # 전역에 선언되어 있는 connection 가져옴
    global conn
    # 커서를 취득
    cur=conn.cursor(buffered=True)
    # 쿼리 실행, values는 query값에 있는 sql query식의 바인딩 값
    # 문자열 포맷팅으로 설정, values는 튜플 값으로 입력
    cur.execute(query, values)

    print(cur.fetchone())

    # 쿼리 실행 결과 값 저장
    result = cur.fetchone()
    # DB connect 종료
    conn.close()

    # 쿼리 실행 결과 값이 존재하면 True, 존재하지 않으면(None) False 반환
    if (cur.fetchone()):
        return True
    elif (cur.fetchone()==None):
        return False


# DB에 데이터를 삽입할 때 사용되는 함수
def insert(query, values):
    # 전역에 선언되어 있는 connection 가져옴
    global conn
    try:
        # 커서를 취득
        cur=conn.cursor(buffered=True)
        # 쿼리 실행, values는 query값에 있는 sql query식의 바인딩 값
        # 문자열 포맷팅으로 설정
        # values는 튜플 값으로 입력되면 execute, 리스트 값으로 입력되면 executemany
        if (isinstance(values, tuple)):
            cur.execute(query, values)
        elif (isinstance(values, list)):
            cur.executemany(query, values)

        # 쿼리를 커밋
        conn.commit()
        # DB connect 종료
        conn.close()
        # True 반환
        return True
    except Exception as e:
        # 예외 발생 시 쿼리 롤백
        conn.rollback()
        raise e

# DB에 데이터를 수정할 때 사용하는 함수
def update(query, values):
    # 전역에 선언되어 있는 connection 가져옴
    global conn
    try:
        # 커서를 취득
        cur=conn.cursor(buffered=True)
        # 쿼리 실행, values는 query값에 있는 sql query식의 바인딩 값
        # 문자열 포맷팅으로 설정 
        # values는 튜플 값으로 입력되면 execute, 리스트 값으로 입력되면 executemany
        if (isinstance(values, tuple)):
            cur.execute(query, values)
        elif (isinstance(values, list)):
            cur.executemany(query, values)

        # 쿼리를 커밋
        conn.commit()
        # DB connect 종료
        conn.close()
        # True 반환
        return True
    except Exception as e:
        # 예외 발생 시 쿼리 롤백
        conn.rollback()
        raise e
