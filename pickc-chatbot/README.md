# 🖥️ PickC Chatbot - 프론트엔드 클라이언트

**PickC**의 프론트엔드 클라이언트는 사용자의 자연어 요청을 입력받고 AI가 생성한 PC 견적을 직관적인 UI로 출력합니다.  
React와 TailwindCSS 기반으로 구성되었으며, Vite 개발 서버를 통해 빠른 개발 환경을 제공합니다.

---

## 📁 주요 파일 설명

### 루트 디렉토리
- `index.html`  
  → HTML 진입점으로, React가 마운트될 `#root` DOM을 포함합니다.

- `vite.config.js`  
  → 개발 서버 설정 및 React 플러그인 등록 (포트, 호스트, CORS 등 포함)

- `tailwind.config.js`  
  → TailwindCSS 경로 및 테마 커스터마이징 설정 파일입니다.

---

### 📂 src 폴더
- `main.jsx`  
  → React 앱의 엔트리포인트로, `App.jsx`를 `#root`에 렌더링합니다.

- `App.jsx`  
  → 메인 컴포넌트로 챗봇 UI, 사용자 입력창, 출력 결과 등을 포함합니다.

- `index.css`  
  → TailwindCSS 초기화 및 사용자 정의 유틸리티 스타일이 포함된 CSS 진입점입니다.

- `assets/` 폴더  
  → 프로젝트에 사용되는 로고 및 아이콘 이미지 저장소입니다.
    - `logo.jpeg` : PickC 텍스트 및 심볼 로고
    - `miniLogo.jpeg` : 브라우저 탭 파비콘 및 심플 아이콘

---

## ⚙️ 기술 스택

- React
- TailwindCSS
- Vite

---

## 🚀 개발 실행 방법

1. 의존성 설치
```bash
npm install
```

2. 개발 서버 실행
```bash
npm run dev
```

---

## 📧 문의

- **개발자** : 김민재  
- **이메일** : [minjae54920@gmail.com](mailto:minjae54920@gmail.com)

---

> 본 프론트엔드는 사용자의 입력을 직관적으로 처리하고 결과를 실시간으로 확인할 수 있도록 돕습니다.
