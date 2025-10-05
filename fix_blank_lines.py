import re
import sys
from pathlib import Path

DEF_CLASS_RE = re.compile(r'^(def|class)\s')
IF_MAIN_RE = re.compile(r"^if\s+__name__\s*==\s*['\"]__main__['\"]\s*:")

def fix_file(path: Path):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)
    new_lines = []

    for line in lines:
        if DEF_CLASS_RE.match(line) or IF_MAIN_RE.match(line):
            i = len(new_lines) - 1
            blank_count = 0
            while i >= 0 and new_lines[i].strip() == "":
                blank_count += 1
                i -= 1
            need = 2 - blank_count
            if need > 0 and len(new_lines) > 0:
                new_lines.extend(["\n"] * need)
        new_lines.append(line)

    new_text = "".join(new_lines)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(f"Fixed: {path}")
    else:
        print(f"No changes: {path}")

def main(targets):
    for t in targets:
        p = Path(t)
        if p.is_dir():
            for py in p.rglob("*.py"):
                fix_file(py)
        elif p.is_file() and p.suffix == ".py":
            fix_file(p)
        else:
            print(f"Skipping (not a .py file): {p}")

if __name__ == "__main__":
    targets = sys.argv[1:] or ["brain_games"]
    main(targets)
