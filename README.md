PickC - PC 견적 추천 챗봇

PickC는 사용자의 예산과 용도에 맞춰 자동으로 PC 견적을 추천해주는 AI 기반 챗봇입니다.
Google Gemini API를 활용하여 자연어 기반의 사용자 요청을 분석하고, MySQL에 저장된 부품 정보를 기반으로 최적의 PC 구성을 제공합니다.

⸻

💡 주요 기능
	•	💬 자연어 입력을 통한 견적 요청 (예 : “100만원대 게임용 PC 추천해줘”)
	•	⚙️ 실제 부품 데이터베이스(MySQL) 기반 견적 생성
	•	📊 추천 부품을 표 형식으로 출력하며, 총 견적 금액 자동 계산
	•	➕ 추가 요청 시 기존 견적을 기반으로 개선하여 재추천
	•	🖥️ React 기반 프론트엔드 UI 제공

⸻

🏗️ 프로젝트 구조

PickC/
├── pickc-api/           # FastAPI 백엔드 서버
│   ├── main.py           # API 서버 진입점
│   ├── db.py             # MySQL 연동 및 부품 조회 로직
│   └── .env              # 환경 변수 (Gemini API 키, DB 접속 정보 등)
│
├── pickc-chatbot/       # React 프론트엔드 클라이언트
│   ├── src/
│   │   ├── App.jsx       # 주요 컴포넌트
│   │   └── assets/logo.png
│   └── public/index.html
│
└── README.md            # 프로젝트 설명 파일


⸻

⚙️ 기술 스택
	•	백엔드 : FastAPI, Python, Uvicorn
	•	AI : Google Gemini 1.5 Flash API
	•	DB : MySQL + PyMySQL
	•	프론트엔드: React + TailwindCSS

⸻

🚀 실행 방법

📦 백엔드 서버 실행

cd pickc-api
uvicorn main:app --reload

🌐 프론트엔드 실행

cd pickc-chatbot
npm run dev

⸻

📁 데이터베이스 구성 (예시)

cpu, gpu, ram, ssd, mainboard, psu, case, cooler 등 총 8개 테이블에 부품별 속성 저장.

cpu 테이블 예시

name	brand	core	boost	price	socket	igpu	etc
Ryzen 5 5600	AMD	6	4.4GHz	170000	AM4	N	가성비 게임용 대표 CPU


⸻

✅ 개선 예정
	•	견적 사양 다운로드(PDF/Excel)
	•	로그인 및 사용자 맞춤 견적 저장 기능
	•	부품 재고 반영

⸻

📧 문의
	•	개발자 : 김민재
	•	이메일 : minjae54920@gmail.com

⸻

본 프로젝트는 인공지능 기반 챗봇 기술과 실시간 데이터베이스 연동을 통해 사용자의 편리한 PC 구매 결정을 돕는 데 목적이 있습니다.
