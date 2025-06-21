import pymysql

# 📦 데이터베이스 연결 설정 정보
db_config = {
    "host": "localhost",        # 데이터베이스 호스트 주소
    "port": 3306,               # 포트 번호 (기본 : 3306)
    "user": "root",             # DB 사용자명
    "password": "비밀번호",     # 비밀번호 
    "database": "pickc_db",     # 사용할 데이터베이스 이름
    "charset": "utf8mb4",       # 문자 인코딩
    "cursorclass": pymysql.cursors.DictCursor  # 결과를 딕셔너리로 반환
}

# ✅ DB 연결 함수
def get_connection():
    """
    MySQL 데이터베이스에 연결하여 Connection 객체를 반환
    """
    return pymysql.connect(**db_config)

# 🔍 부품별 조회 함수들
def get_cpus(limit=10):
    """
    CPU 부품 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM cpu LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_cpu_coolers(limit=10):
    """
    CPU 쿨러 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM cpu_cooler LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_gpus(limit=10):
    """
    GPU 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM gpu LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_hdds(limit=10):
    """
    HDD 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM hdd LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_mainboards(limit=10):
    """
    메인보드 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM mainboard LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_pc_cases(limit=10):
    """
    PC 케이스 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM pc_case LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_psus(limit=10):
    """
    파워서플라이(PSU) 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM psu LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_rams(limit=10):
    """
    RAM 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM ram LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_ssds(limit=10):
    """
    SSD 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM ssd LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

def get_system_coolers(limit=10):
    """
    시스템 쿨러 정보를 최대 'limit'개까지 조회
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM system_cooler LIMIT %s"
            cursor.execute(sql, (limit,))
            return cursor.fetchall()
    finally:
        conn.close()

# 🧠 벤치마크 점수 조회 함수
def get_cpu_score(name):
    """
    CPU 이름으로 벤치마크 점수를 조회. 없을 경우 기본값 10000 반환.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT score FROM cpu_benchmark WHERE name = %s"
            cursor.execute(sql, (name,))
            result = cursor.fetchone()
            return result["score"] if result else 10000
    finally:
        conn.close()

def get_gpu_score(name):
    """
    GPU 이름으로 벤치마크 점수를 조회. 없을 경우 기본값 10000 반환.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT score FROM gpu_benchmark WHERE name = %s"
            cursor.execute(sql, (name,))
            result = cursor.fetchone()
            return result["score"] if result else 10000
    finally:
        conn.close()
