import os
import time
import markdown
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from flask import Flask, render_template_string

DOCS_DIR = os.path.abspath("./docs")

def ensure_docs_dir():
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)

def generate_docs_for_script(script_path, ext):
    fname = os.path.basename(script_path)
    doc_file = os.path.join(DOCS_DIR, fname + ".md")
    with open(script_path, encoding="utf-8", errors="ignore") as f:
        code = f.read()
    if ext == ".ps1":
        functions = [line.split()[1] for line in code.splitlines() if line.strip().lower().startswith("function ")]
    elif ext == ".py":
        functions = [line.split()[1].split("(")[0] for line in code.splitlines() if line.strip().startswith("def ")]
    else:
        functions = []
    md = f"# {fname}\n\n**Auto-generated documentation for {fname}.**\n\n"
    md += "## Functions\n"
    md += "\n".join(f" - {fn}" for fn in functions) if functions else " - *(None found)*"
    md += f"\n\n_Last updated: {time.ctime()}_\n"
    with open(doc_file, "w", encoding="utf-8") as df:
        df.write(md)
    print(f"✅ Documented {fname} -> {doc_file}")

def generate_docs_for_all():
    ensure_docs_dir()
    for root, dirs, files in os.walk("."):
        if any(blk in root for blk in ["venv", ".venv", "site-packages", "__pycache__", ".git"]):
            continue
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext in [".ps1", ".py"]:
                script_path = os.path.join(root, fname)
                doc_file = os.path.join(DOCS_DIR, fname + ".md")
                if not os.path.exists(doc_file) or os.path.getmtime(script_path) > os.path.getmtime(doc_file):
                    generate_docs_for_script(script_path, ext)

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            ext = os.path.splitext(event.src_path)[1].lower()
            if ext in [".ps1", ".py"]:
                generate_docs_for_script(event.src_path, ext)
    def on_created(self, event):
        if not event.is_directory:
            ext = os.path.splitext(event.src_path)[1].lower()
            if ext in [".ps1", ".py"]:
                generate_docs_for_script(event.src_path, ext)

def start_watcher():
    observer = Observer()
    handler = ChangeHandler()
    observer.schedule(handler, path=".", recursive=True)
    observer.start()
    return observer

app = Flask(__name__)
@app.route("/")
def index():
    ensure_docs_dir()
    files = sorted([f for f in os.listdir(DOCS_DIR) if f.endswith(".md")])
    html = "<h2>ExoSuite Docs Index</h2><ul>"
    for fname in files:
        html += f'<li><a href=\"/docs/{fname}\">{fname}</a></li>'
    html += "</ul>"
    return html

@app.route("/docs/<filename>")
def show_doc(filename):
    doc_path = os.path.join(DOCS_DIR, filename)
    if not os.path.isfile(doc_path):
        return "Document not found.", 404
    with open(doc_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
    template = \"\"\"
    <html>
    <head>
      <title>{{filename}}</title>
      <style>
        body { font-family: Arial, sans-serif; background: #222; color: #ddd; margin: 2em;}
        a { color: #61dafb; }
        pre, code { background: #1a1a1a; color: #9dfcce; padding: 0.5em; border-radius: 6px; }
        h2 { color: #56e2f2; }
        .back { margin-bottom: 1em; }
      </style>
    </head>
    <body>
      <div class="back"><a href="/">← Back to Index</a></div>
      <h2>{{filename}}</h2>
      <div>{{content|safe}}</div>
    </body>
    </html>
    \"\"\"
    return render_template_string(template, filename=filename, content=html_content)

if __name__ == "__main__":
    print("🔄 Generating docs for all scripts...")
    generate_docs_for_all()
    print("🚦 Watching for changes and serving docs dashboard at http://localhost:5000")
    observer = start_watcher()
    try:
        app.run(port=5000, debug=False)
    finally:
        observer.stop()
        observer.join()
