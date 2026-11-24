
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. .env 파일에서 API 키 불러오기
load_dotenv(r"D:\GPT_AGENT_2025\.env")

api_key = os.getenv("OPENAI_API_KEY")

# API 키 확인
if not api_key:
    raise ValueError("OPENAI_API_KEY를 찾을 수 없습니다.")

print("API 키 로드 성공!")

# 2. LangChain LLM 객체 생성
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=api_key
)

# 3. 초기 시스템 메시지 설정
messages = [
    SystemMessage(content="너는 사용자를 도와주는 상담사야.")
]

# 4. 사용자와 반복 대화
while True:
    user_input = input("사용자: ")

    # 종료 조건
    if user_input.lower() == "exit":
        print("챗봇을 종료합니다.")
        break

    # 사용자 메시지 저장
    messages.append(
        HumanMessage(content=user_input)
    )

    # LLM 호출
    ai_response = llm.invoke(messages)

    # AI 응답 저장
    messages.append(ai_response)

    # 응답 출력
    print("AI:", ai_response.content)
