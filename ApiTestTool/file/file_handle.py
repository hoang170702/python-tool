def read_file_safe(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    return "\n".join(lines)
