# 📦 PickC API - FastAPI 백엔드 서버

이 디렉터리는 **PickC** 프로젝트의 백엔드 서버 구성 요소로, FastAPI를 기반으로 사용자 요청을 처리하고 MySQL 데이터베이스에서 PC 부품 정보를 조회합니다.

---

## 📁 포함 파일

- `main.py`  
  → FastAPI 서버의 진입점입니다. `/chat` 엔드포인트를 통해 챗봇과의 대화를 처리합니다.

- `db.py`  
  → MySQL 데이터베이스와의 연동 로직이 포함되어 있으며, 각 부품 테이블로부터 데이터를 조회하는 기능을 수행합니다.

- `.env`  
  → 환경 변수 파일로, 아래 정보를 포함해야 합니다.
    - `GEMINI_API_KEY` : Google Gemini API 키
    - `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` : MySQL 접속 정보

---

## ⚙️ 실행 방법

1. 의존성 설치
```bash
pip install fastapi uvicorn pymysql python-dotenv google-generativeai
```

2. `.env` 파일 설정
```env
GEMINI_API_KEY=your_gemini_api_key
```

3. `db.py` 파일 설정
```python
db_config = {
    "host": "localhost",        # 데이터베이스 호스트 주소
    "port": 3306,               # 포트 번호
    "user": "root",             # DB 사용자명
    "password": "your_password",# 비밀번호
    "database": "pickc_db",     # 사용할 데이터베이스 이름
    "charset": "utf8mb4",       # 문자 인코딩
    "cursorclass": pymysql.cursors.DictCursor  # 결과를 딕셔너리로 반환
}
```

4. 서버 실행
```bash
uvicorn main:app --reload
```

---

## 🔗 주요 기술 스택

- FastAPI (백엔드 프레임워크)
- PyMySQL (MySQL 연동)
- Google Generative AI API (Gemini 1.5 Flash)

---

## 📧 문의

- **개발자** : 김민재  
- **이메일** : [minjae54920@gmail.com](mailto:minjae54920@gmail.com)
