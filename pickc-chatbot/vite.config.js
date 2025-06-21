// 📦 Vite 설정 파일
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// ✅ Vite 프로젝트 구성 정의
export default defineConfig({
  // 🔌 개발 서버 설정
  server: {
    host: '0.0.0.0', // 모든 네트워크 인터페이스에서 접근 가능하도록 설정 (로컬 IP 접근 허용)
    port: 5173,       // 개발 서버 포트 번호 (기본값: 5173)

    // ✅ CORS 및 외부 접근을 위한 도메인 화이트리스트
    allowedHosts: ['minjae.mercusysddns.com'], // 해당 도메인만 접근 허용

    // 🔓 개발 중 임시로 전체 도메인 허용할 때 사용
    // allowedHosts: 'all',
  },

  // 🔧 사용 플러그인 목록
  plugins: [react()], // React 프로젝트용 공식 Vite 플러그인
})
