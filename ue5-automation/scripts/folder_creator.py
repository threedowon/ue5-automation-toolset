"""
Unreal Engine 5 폴더 구조 자동 생성 스크립트
"""
import os


def create_folder_structure(project_content: str, root: str = "DOWON"):
    """
    Unreal Engine 프로젝트 Content 폴더에 폴더 구조를 생성합니다.
    
    Args:
        project_content: Unreal 프로젝트의 Content 폴더 경로
        root: 최상위 폴더 이름 (기본값: "DOWON")
    
    Returns:
        tuple: (성공 여부, 메시지)
    """
    # ---------------------------------------------------
    # 📁 생성할 폴더 목록 (ROOT 기준 상대 경로)
    # ---------------------------------------------------
    FOLDERS = [
        "Blueprints",
        "UI",
        "Temp",
        os.path.join("Assets", "Meshes"),
        os.path.join("Assets", "Textures"),
        os.path.join("Assets", "Materials"),
        os.path.join("Assets", "Animations"),
        os.path.join("Assets", "Sounds"),
        os.path.join("Assets", "FX"),
        os.path.join("Maps", "Levels"),
        os.path.join("Maps", "SubLevels"),
    ]

    # ---------------------------------------------------
    # 🛠 폴더 생성 함수
    # ---------------------------------------------------
    def ensure(path: str):
        if not os.path.exists(path):
            os.makedirs(path)
            return f"📁 Created: {path}"
        else:
            return f"✔ Exists:  {path}"

    try:
        messages = []
        messages.append("🚀 Creating DOWON Content Folder Tree...\n")

        base = os.path.join(project_content, root)
        messages.append(ensure(base))

        for folder in FOLDERS:
            messages.append(ensure(os.path.join(base, folder)))

        messages.append("\n🎉 Done! Folder structure created!")
        return True, "\n".join(messages)
    
    except Exception as e:
        return False, f"❌ Error: {str(e)}"

