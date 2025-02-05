# Back-End
SKT FLY AI 6기 패기반 TEAM3

## 개발환경 설정
1. 깃허브 레포지토리 클론
    
    ```python
    cd Project
    git clone https://github.com/SKT-FLY-AI-project/Back-End
    ```
    - 프로젝트 구조
   ```
    project-root/
    │── Back-End/            # FastAPI 프로젝트 (백엔드)
    │   ├── app/
    │   ├── venv/            # 개발환경
    │   ├── main.py
    │   ├── requirements.txt
    │   ├── .gitignore
    │── Front-End/           # Flutter 프로젝트 (프론트엔드)
    │   ├── lib/
    │   ├── pubspec.yaml
    │   ├── android/
    │   ├── ios/
    │   ├── test/
    │   ├── ...
   ```
    
3. 가상환경 생성
    
    ```python
    cd Back-End
    python -m venv venv
    ```
    
4. 가상환경 활성화
    
    ```python
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows
    ```
    
5. FastAPI 설치
    
    ```python
    pip install fastapi uvicorn
    ```
    
6. 서버 실행
    
    ```python
    uvicorn main:app --reload
    ```
    
7. 웹 브라우저에서 확인: [127.0.0.1:8000](http://127.0.0.1:8000/)
