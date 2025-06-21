/** @type {import('tailwindcss').Config} */
// 📦 Tailwind CSS 구성 파일

export default {
  // ✅ Tailwind가 CSS 클래스를 추출할 파일 경로 지정
  content: [
    "./index.html",                // HTML 진입점
    "./src/**/*.{js,ts,jsx,tsx}",  // src 폴더 내 모든 JS/TS/JSX/TSX 파일
  ],

  theme: {
    // ✅ 테마 커스터마이징 (여기서 색상, 폰트, 크기 등을 확장 가능)
    extend: {
      // 예: colors: { primary: '#1e40af' }
    },
  },

  // ✅ 플러그인 배열 (폼, 타이포그래피 등 필요 시 추가)
  plugins: [],
};
