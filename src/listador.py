from pathlib import Path

pasta = Path(r"C:\Users\André\Downloads")

# lista todos os arquivos que terminam com .jpg
if pasta.exists():
    for arquivo_jpg in pasta.glob("*.jpg"):
        print(f"Encontrado: {arquivo_jpg.name} ({arquivo_jpg.stat().st_size} bytes)")
else:
    print(f"A pasta {pasta} não existe.")
