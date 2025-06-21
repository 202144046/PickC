import os
import time
import google.generativeai as genai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# ░▒█ PickC AI 챗봇 API ▒░
# Gemini 1.5 Flash 기반 견적 추천 FastAPI 백엔드

# ───────────────────────────────
# ① 환경변수 로드 (.env 파일에서 API 키 불러오기)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ② Gemini 모델 구성 (1.5 Flash 사용)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ③ FastAPI 앱 생성
app = FastAPI()

# 헬스체크 엔드포인트
@app.get("/")
async def root():
    return {"message": "PickC API 서버 정상 작동 중"}

# ④ CORS 설정 (모든 도메인에서 요청 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ───────────────────────────────
# ⑤ 메인 챗봇 응답 엔드포인트
@app.post("/chat")
async def chat(req: Request):
    # 사용자 입력 파싱
    data = await req.json()
    user_input = data.get("message", "").strip()

    # 부품 및 벤치마크 관련 DB 접근 함수 import
    from db import (
        get_cpus, get_mainboards, get_gpus, get_rams, get_ssds,
        get_psus, get_pc_cases, get_cpu_coolers, get_system_coolers, get_hdds,
        get_cpu_score, get_gpu_score
    )

    # ───────────────────────────────
    # Step 1: 기본 구성 부품 선택 (임시로 랜덤 1개씩)
    cpu = get_cpus(limit=1)[0]
    mobo = get_mainboards(limit=1)[0]
    ram = get_rams(limit=1)[0]

    # Step 2: 나머지 부품은 사용자의 입력 키워드 기반으로 필터링
    usage_keyword = user_input

    gpu_list = [g for g in get_gpus(limit=20) if usage_keyword in g.get("application", "")]
    ssd_list = [s for s in get_ssds(limit=20) if usage_keyword in s.get("application", "")]
    hdd_list = [h for h in get_hdds(limit=20) if usage_keyword in h.get("application", "")]
    psu_list = [p for p in get_psus(limit=20) if usage_keyword in p.get("application", "")]
    case_list = [c for c in get_pc_cases(limit=20) if usage_keyword in c.get("application", "")]
    sys_cooler_list = [s for s in get_system_coolers(limit=20) if usage_keyword in s.get("application", "")]

    # 조건에 맞는 부품이 없을 경우 기본 1개로 대체
    gpu = gpu_list[0] if gpu_list else get_gpus(limit=1)[0]
    ssd = ssd_list[0] if ssd_list else get_ssds(limit=1)[0]
    hdd = hdd_list[0] if hdd_list else get_hdds(limit=1)[0]

    # TDP 기반으로 적절한 파워 서플라이 선택 (20% 여유 잡음)
    total_tdp = cpu.get("tdp", 0) + gpu.get("tdp", 0)
    required_wattage = int(total_tdp / 0.8)
    suitable_psus = [p for p in get_psus(limit=20) if p.get("wattage", 0) >= required_wattage]
    psu = suitable_psus[0] if suitable_psus else get_psus(limit=1)[0]

    case = case_list[0] if case_list else get_pc_cases(limit=1)[0]
    sys_cooler = sys_cooler_list[0] if sys_cooler_list else get_system_coolers(limit=1)[0]

    # 최종 부품 구성 리스트
    parts_info = [
        ("CPU", cpu),
        ("메인보드", mobo),
        ("RAM", ram),
        ("GPU", gpu),
        ("SSD", ssd),
        ("HDD", hdd),
        ("시스템 쿨러", sys_cooler),
        ("파워", psu),
        ("케이스", case),
    ]

    # ───────────────────────────────
    # Step 3: 마크다운 표 생성 + 가격 합산
    parts_markdown = "| 부품 | 제품명 | 가격 |\n|------|--------|------|\n"
    total_price = 0
    for part_name, item in parts_info:
        parts_markdown += f"| {part_name} | {item['name']} | ₩{item['price']:,} |\n"
        total_price += item["price"]
    parts_markdown += f"| - | 총액 | ₩{total_price:,} |"

    # 입력 없을 경우 오류 응답
    if not user_input:
        return {"reply": "❗ 메시지를 입력해주세요."}

    # ───────────────────────────────
    # Step 4: 벤치마크 점수 계산 및 등급 매핑
    cpu_score = get_cpu_score(cpu["name"])
    gpu_score = get_gpu_score(gpu["name"])

    if "게임" in user_input:
        system_score = int(cpu_score * 0.3 + gpu_score * 0.7)
    elif "작업" in user_input:
        system_score = int(cpu_score * 0.7 + gpu_score * 0.3)
    else:
        system_score = int((cpu_score + gpu_score) / 2)

    if system_score >= 25000:
        grade = "★★★★★"
    elif system_score >= 20000:
        grade = "★★★★☆"
    elif system_score >= 15000:
        grade = "★★★☆☆"
    elif system_score >= 10000:
        grade = "★★☆☆☆"
    else:
        grade = "★☆☆☆☆"

    benchmark_summary = f"이 구성의 예상 성능은 {grade} 등급입니다. (총합 점수: {system_score})"

    # ───────────────────────────────
    # Step 5: Gemini 응답 구성 및 호출
    system_instruction = (
        "너는 사용자의 예산과 목적에 따라 컴퓨터 부품을 추천해주는 AI 챗봇이야.\n"
        "항상 친절하고 간결하게, 한국어로 대답해줘.\n"
        "추천 구성은 CPU, 메인보드, GPU, RAM, SSD, PSU, 케이스 순서로 말해줘.\n"
        "다음 형식을 반드시 지켜서 응답해줘:\n"
        "- 부품 정보는 마크다운 표 형식으로 출력할 것\n"
        "- 표의 헤더는 '부품', '제품명', '가격'\n"
        "- 마지막 행에는 전체 부품 가격의 총액을 표시할 것\n"
        "- 총액 행의 부품 열에는 '-' 와 같은 더미 텍스트를 넣고, '제품명' 열에 '총액', '가격' 열에 합계 표시\n"
        "- 일반 설명 문구는 표 바깥에 작성할 것\n"
        "- 각 부품별 추가 설명은 필요 없고 전체 구성에 대한 설명만 짧게 표 밑에 출력할 것\n"
        "- 모든 텍스트는 가독성이 좋게 출력할 것\n"
        "- '추가 설명 :' 같은 문구는 붙이지 말 것"
    )

    full_prompt = (
        f"{system_instruction}\n\n"
        f"추천 구성 :\n{parts_markdown}\n\n{benchmark_summary}\n\n"
        f"질문 : {user_input}"
    )

    start_time = time.time()

    try:
        # Gemini API 호출
        response = model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                temperature=0.9
            )
        )
        reply = response.text

    except Exception as e:
        # 오류 발생 시 텍스트 반환
        reply = f"❌ Gemini 오류 발생: {str(e)}"

    execution_time = time.time() - start_time

    return {
        "reply": reply,
        "response_time" : f"{execution_time:.2f}초",
        "model" : "gemini-1.5-flash"
    }
