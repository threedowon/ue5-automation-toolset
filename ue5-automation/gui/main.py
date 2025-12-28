"""
Unreal Engine 5 Python Automation GUI
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys

# scripts 폴더를 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.folder_creator import create_folder_structure


class UnrealAutomationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unreal Engine 5 Python Automation")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # 변수
        self.project_content_path = tk.StringVar()
        self.root_folder_name = tk.StringVar(value="DOWON")
        
        self.setup_ui()
    
    def setup_ui(self):
        # 메인 프레임
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 그리드 가중치 설정
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # 제목
        title_label = ttk.Label(
            main_frame, 
            text="Unreal Engine 5 Python Automation",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # 프로젝트 Content 경로 선택
        ttk.Label(main_frame, text="프로젝트 Content 경로:").grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        path_frame.columnconfigure(0, weight=1)
        
        self.path_entry = ttk.Entry(path_frame, textvariable=self.project_content_path, width=50)
        self.path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        ttk.Button(
            path_frame, 
            text="찾아보기...", 
            command=self.browse_folder
        ).grid(row=0, column=1)
        
        # 최상위 폴더 이름
        ttk.Label(main_frame, text="최상위 폴더 이름:").grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        
        root_name_entry = ttk.Entry(main_frame, textvariable=self.root_folder_name, width=20)
        root_name_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # 구분선
        separator = ttk.Separator(main_frame, orient=tk.HORIZONTAL)
        separator.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=20)
        
        # 기능 버튼 영역
        functions_frame = ttk.LabelFrame(main_frame, text="자동화 기능", padding="10")
        functions_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        functions_frame.columnconfigure(0, weight=1)
        
        # 폴더 생성 버튼
        folder_btn = ttk.Button(
            functions_frame,
            text="📁 폴더 구조 생성",
            command=self.create_folders,
            width=30
        )
        folder_btn.grid(row=0, column=0, pady=5)
        
        # 추후 추가될 기능들을 위한 플레이스홀더
        # 예: ttk.Button(functions_frame, text="다른 기능", command=self.other_function).grid(row=1, column=0, pady=5)
        
        # 로그 출력 영역
        log_frame = ttk.LabelFrame(main_frame, text="실행 결과", padding="10")
        log_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=15,
            wrap=tk.WORD,
            font=("Consolas", 9)
        )
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 초기 메시지
        self.log("✨ Unreal Engine 5 Python Automation에 오신 것을 환영합니다!\n")
        self.log("프로젝트 Content 경로를 선택하고 원하는 기능을 실행하세요.\n")
    
    def browse_folder(self):
        """폴더 선택 다이얼로그"""
        folder = filedialog.askdirectory(title="프로젝트 Content 폴더 선택")
        if folder:
            self.project_content_path.set(folder)
            self.log(f"📂 선택된 경로: {folder}\n")
    
    def log(self, message):
        """로그 메시지 출력"""
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        self.root.update()
    
    def create_folders(self):
        """폴더 구조 생성 실행"""
        project_path = self.project_content_path.get().strip()
        root_name = self.root_folder_name.get().strip()
        
        if not project_path:
            messagebox.showerror("오류", "프로젝트 Content 경로를 선택해주세요.")
            return
        
        if not os.path.exists(project_path):
            messagebox.showerror("오류", "선택한 경로가 존재하지 않습니다.")
            return
        
        if not root_name:
            messagebox.showerror("오류", "최상위 폴더 이름을 입력해주세요.")
            return
        
        # 로그 영역 초기화
        self.log_text.delete(1.0, tk.END)
        
        self.log("=" * 60 + "\n")
        self.log("폴더 구조 생성 시작...\n")
        self.log("=" * 60 + "\n\n")
        
        success, message = create_folder_structure(project_path, root_name)
        
        self.log(message + "\n\n")
        
        if success:
            messagebox.showinfo("완료", "폴더 구조가 성공적으로 생성되었습니다!")
        else:
            messagebox.showerror("오류", "폴더 생성 중 오류가 발생했습니다.")


def main():
    root = tk.Tk()
    app = UnrealAutomationGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

