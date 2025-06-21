import ReactMarkdown from "react-markdown";
import { useState } from "react";
import PickCLogo from "./assets/logo.jpeg"; // 🖼️ 로고 이미지 경로

// 📦 PickC 메인 컴포넌트
export default function App() {
  // ✅ 상태 정의
  const [message, setMessage] = useState("");               // 사용자 입력
  const [reply, setReply] = useState("");                   // Gemini 응답
  const [benchmark, setBenchmark] = useState("");           // 벤치마크 점수 요약
  const [loading, setLoading] = useState(false);            // 로딩 상태
  const [error, setError] = useState("");                   // 오류 메시지
  const [previousReplies, setPreviousReplies] = useState([]); // 이전 견적 저장

  // 📤 API 전송 함수
  const handleSend = async () => {
    if (loading || !message.trim()) return;

    setLoading(true);
    setReply("");
    setError("");

    // 🔁 기존 응답이 있을 경우 맥락 포함 요청
    const promptMessage = reply
      ? `다음은 이전에 생성된 견적입니다:\n${reply}\n\n위의 견적을 기반으로 아래 요청을 반영해 개선해줘:\n${message}`
      : message;

    try {
      const res = await fetch("http://minjae.mercusysddns.com:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: promptMessage,
          context: reply ? reply : null
        }),
      });
      const data = await res.json();
      setReply(data.reply || "응답을 받아오지 못했습니다.");
      setBenchmark(data.benchmark || "");
    } catch {
      setError("서버 연결에 실패했습니다.");
    } finally {
      setLoading(false);
    }

    // 🗂️ 이전 견적 저장
    if (reply) {
      const newReply = {
        replyText: reply,
        userPrompt: message,
        benchmarkText: benchmark,
      };
      setPreviousReplies([...previousReplies, newReply]);
    }

    setMessage(""); // 입력 초기화
  };

  // ⌨️ 엔터 입력 처리
  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (
        document.activeElement.tagName === "TEXTAREA" ||
        document.activeElement.tagName === "INPUT"
      ) {
        handleSend();
      }
    }
  };

  // 💬 UI 렌더링
  return (
    <div className="min-h-screen flex flex-col px-4 pt-6 pb-6 font-['Pretendard'] bg-white">
      
      {/* 더미 영역 (레이아웃 용 여백 확보용) */}
      <div className="h-12 w-full max-w-3xl mx-auto mt-8 opacity-0 select-none pointer-events-none">더미 영역</div>
      <div className="h-12 w-full max-w-3xl mx-auto mt-8 opacity-0 select-none pointer-events-none">더미 영역</div>

      {/* 🖼️ 로고 표시 */}
      <div className="flex flex-col items-center">
        <div className="flex items-center gap-3 mb-4">
          <img src={PickCLogo} alt="PickC 로고" className="h-[100px]" />
        </div>
      </div>

      {/* 출력 영역 */}
      <div className="w-full max-w-3xl mx-auto mb-20">
        <div className="border border-black rounded-lg pt-4 px-4 pb-6 h-[480px] overflow-y-auto flex flex-col">

          {/* 안내 메시지 */}
          {!reply && !loading && (
            <p className="text-2xl text-center font-extrabold text-black leading-relaxed mb-1 pl-2">
              안녕하세요. PickC 입니다. 원하시는 내용을 입력해주세요.
            </p>
          )}

          {/* 오류 메시지 */}
          {error && <p className="mt-4 text-center text-red-500">{error}</p>}

          {/* 로딩 중 메시지 */}
          {loading && (
            <p className="mt-4 text-center text-blue-500 font-semibold text-lg">견적을 생성 중 입니다...</p>
          )}

          {/* 응답 메시지 표시 */}
          {reply && (
            <div className="mt-2 p-2 bg-blue-50 rounded-lg text-blue-900 whitespace-pre-line shadow-inner space-y-4">
              
              {/* 이전 견적 목록 */}
              {previousReplies.map((prev, index) => {
                const lines = prev.replyText.split("\n");
                const tableLines = lines.filter((line) => line.includes("|"));
                const firstTableIndex = lines.findIndex((line) => line.includes("|"));
                const lastTableIndex = tableLines.length > 0
                  ? lines.lastIndexOf(tableLines[tableLines.length - 1])
                  : -1;
                const intro = firstTableIndex > 0 ? lines.slice(0, firstTableIndex).join("\n").trim() : "";
                const outro = lastTableIndex !== -1 ? lines.slice(lastTableIndex + 1).join("\n").trim() : "";

                return (
                  <div key={index} className="bg-gray-100 p-4 rounded mb-4 relative">
                    <h3 className="font-semibold text-gray-700 mb-2">📦 {index + 1}번째 견적</h3>
                    
                    {/* 설명 텍스트 (표 위/아래) */}
                    {intro && <ReactMarkdown>{intro}</ReactMarkdown>}

                    {/* 견적 표 출력 */}
                    {tableLines.length > 0 && (
                      <table className="w-full text-center border border-gray-300 bg-white mb-4">
                        <thead>
                          <tr>
                            {tableLines[0]
                              .split("|")
                              .filter((col) => col.trim())
                              .map((col, i) => (
                                <th key={i} className="px-4 py-2 border-b font-semibold text-center">
                                  {col.trim()}
                                </th>
                              ))}
                          </tr>
                        </thead>
                        <tbody>
                          {tableLines.slice(2).map((row, rowIndex) => (
                            <tr key={rowIndex}>
                              {row
                                .split("|")
                                .filter((cell) => cell.trim())
                                .map((cell, cellIndex) => (
                                  <td key={cellIndex} className="px-4 py-2 border-t text-center">
                                    {cell.trim()}
                                  </td>
                                ))}
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    )}

                    {outro && <ReactMarkdown>{outro}</ReactMarkdown>}

                    {/* 사용자 요청 표시 */}
                    {prev.userPrompt && (
                      <>
                        <p className="text-sm text-right text-gray-500 mt-4 italic">요청사항 : {prev.userPrompt}</p>
                        {prev.benchmarkText && (
                          <p className="text-sm text-right text-gray-600 italic mt-1">{prev.benchmarkText}</p>
                        )}
                      </>
                    )}
                  </div>
                );
              })}

              {/* 🔄 현재 응답 표시 */}
              <div>
                <h3 className="font-semibold text-blue-700 mb-2">📦 새 견적</h3>
                <ReactMarkdown>{reply}</ReactMarkdown>
                {benchmark && (
                  <div className="mt-4 text-sm text-right text-gray-600 italic">
                    {benchmark}
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* 입력 영역 */}
      <div className="w-full max-w-3xl mx-auto mt-12">
        <div className="border border-black rounded-lg flex items-center px-4 py-3 mt-6 gap-2">
          <input
            type="text"
            className="flex-1 px-2 py-6 text-2xl font-extrabold text-black border-none focus:outline-none placeholder-black bg-transparent"
            placeholder={reply ? "추가 요청 사항을 입력해주세요. (예 : CPU는 라이젠으로 해줘)" : "예 : 100만원대 게이밍 PC 견적 추천해줘."}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button
            onClick={handleSend}
            className="w-40 h-24 ml-4 px-4 py-4 text-2xl font-bold rounded-xl bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 text-white shadow-lg transform hover:scale-105 hover:brightness-110 transition-all duration-300 ease-in-out"
          >
            전송
          </button>
        </div>
      </div>
    </div>
  );
}
