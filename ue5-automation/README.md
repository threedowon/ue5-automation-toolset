# Unreal Engine 5 Python Automation

Unreal Engine 5 프로젝트를 위한 Python 자동화 도구입니다.

## 기능

### 현재 지원하는 기능
- 📁 **폴더 구조 자동 생성**: Unreal 프로젝트에 표준 폴더 구조를 자동으로 생성합니다.

### 향후 추가 예정
- 추가 자동화 기능들이 계속 추가될 예정입니다.

## 설치 및 실행

### 요구사항
- Python 3.7 이상
- tkinter (Python 기본 포함)

### 실행 방법

#### 방법 1: GUI 애플리케이션 실행 (권장)
```bash
python gui/main.py
```

#### 방법 2: 직접 스크립트 실행
```bash
python scripts/folder_creator.py
```

## 사용 방법

### GUI 사용
1. `python gui/main.py` 실행
2. "찾아보기..." 버튼을 클릭하여 Unreal 프로젝트의 Content 폴더 선택
3. 최상위 폴더 이름 입력 (기본값: DOWON)
4. "📁 폴더 구조 생성" 버튼 클릭
5. 실행 결과를 하단 로그 영역에서 확인

### 생성되는 폴더 구조
```
Content/
└── DOWON/
    ├── Blueprints/
    ├── UI/
    ├── Temp/
    ├── Assets/
    │   ├── Meshes/
    │   ├── Textures/
    │   ├── Materials/
    │   ├── Animations/
    │   ├── Sounds/
    │   └── FX/
    └── Maps/
        ├── Levels/
        └── SubLevels/
```

## 프로젝트 구조

```
ue5-automation/
├── scripts/              # 자동화 스크립트들
│   └── folder_creator.py
├── gui/                  # GUI 애플리케이션
│   └── main.py
├── requirements.txt
└── README.md
```

## 새로운 기능 추가하기

1. `scripts/` 폴더에 새로운 Python 스크립트 생성
2. `gui/main.py`의 `functions_frame`에 새로운 버튼 추가
3. 해당 기능을 실행하는 메서드 구현

## 라이선스

이 프로젝트는 개인 사용 목적으로 제작되었습니다.

