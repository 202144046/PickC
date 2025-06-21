
# 💻 PickC - AI 기반 PC 견적 추천 챗봇

**PickC**는 사용자의 예산과 용도에 맞춰 자동으로 PC 견적을 추천해주는 AI 기반 챗봇입니다.  
Google Gemini API를 통해 자연어 기반 요청을 분석하고, MySQL에 저장된 실제 부품 정보를 활용하여 최적의 견적을 제공합니다.

---

## 🔧 주요 기능

- 💬 **자연어 입력을 통한 견적 요청**  
  예 : `"100만원대 게임용 PC 추천해줘"`

- ⚙️ **MySQL 부품 데이터베이스 기반 견적 생성**

- 📊 **추천 부품 표 출력 및 총 가격 자동 계산**

- ➕ **기존 견적 기반 개선 요청 처리**

- 🖥️ **React 기반 직관적인 프론트엔드 UI**

---

## 🏗️ 프로젝트 구조

```
PickC/
├── pickc-api/             # FastAPI 백엔드 서버
│   ├── main.py            # API 서버 진입점
│   ├── db.py              # MySQL 연동 및 부품 조회 로직
│   └── .env               # 환경 변수 (Gemini API 키, DB 접속 정보 등)
│
├── pickc-chatbot/         # React 프론트엔드 클라이언트
│   ├── src/
│   │   ├── App.jsx        # 주요 컴포넌트
│   │   └── assets/logo.png
│   └── index.html
│
└── README.md              # 프로젝트 설명 파일
```

---

## ⚙️ 기술 스택

| 영역       | 기술 구성                                 |
|------------|--------------------------------------------|
| 백엔드     | FastAPI, Python, Uvicorn                  |
| AI         | Google Gemini 1.5 Flash API               |
| 데이터베이스| MySQL + PyMySQL                           |
| 프론트엔드 | React + TailwindCSS                       |

---

## 🚀 실행 방법

### 📦 백엔드 실행
```bash
cd pickc-api
uvicorn main:app --reload
```

### 🌐 프론트엔드 실행
```bash
cd pickc-chatbot
npm install
npm run dev
```

---

## 📁 데이터베이스 구성

총 10개의 부품 테이블을 구성하여 속성별로 저장합니다.  
예 : `cpu`, `gpu`, `ram`, `ssd`, `hdd`, `mainboard`, `psu`, `case`, `cpu_cooler`, `cooler`

### ✅ 예시 - `cpu` 테이블

| name          | brand | core | boost   | price   | socket | igpu | etc                     |
|---------------|-------|------|---------|---------|--------|------|--------------------------|
| Ryzen 5 5600  | AMD   | 6    | 4.4GHz  | 170000  | AM4    | N    | 가성비 게임용 대표 CPU |

---

## ✅ 향후 개선 예정 기능

- 💾 견적 결과 PDF / Excel 다운로드 기능
- 👤 로그인 및 사용자 맞춤 견적 저장 기능
- 📦 부품 재고 반영 기능

---

## 📧 문의

- **개발자** : 김민재  
- **이메일** : [minjae54920@gmail.com](mailto:minjae54920@gmail.com)

---

> 본 프로젝트는 인공지능 기반 챗봇과 실시간 데이터 연동 기술을 통해  
> **사용자의 효율적인 PC 구매 의사결정**을 돕는 것을 목표로 합니다.
