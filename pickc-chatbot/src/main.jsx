// 📍 React 진입점 (main.jsx)
// 앱 전체를 HTML의 root 요소에 렌더링함

import React from 'react';
import ReactDOM from 'react-dom/client'; // React 18 이상부터 사용되는 새로운 렌더링 API
import App from './App';                 // App 컴포넌트 import
import './index.css';                    // Tailwind CSS 포함된 전역 스타일시트

// ✅ 실제 DOM에 React 앱 렌더링 (React 18 방식)
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* App 컴포넌트를 StrictMode로 감싸서 렌더링 */}
    <App />
  </React.StrictMode>
);
