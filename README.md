# Back-End
SKT FLY AI 6기 패기반 TEAM3

## 개발환경 설정
1. 깃허브 레포지토리 클론
    
    ```python
    git clone https://github.com/SKT-FLY-AI-project/Back-End
    ```
    
2. 가상환경 생성
    
    ```python
    cd Back-End
    python -m venv venv
    ```
    
3. 가상환경 활성화
    
    ```python
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows
    ```
    
4. FastAPI 설치
    
    ```python
    pip install fastapi uvicorn
    ```
    
5. 서버 실행
    
    ```python
    uvicorn main:app --reload
    ```
    
6. 웹 브라우저에서 확인: [127.0.0.1:8000](http://127.0.0.1:8000/)
