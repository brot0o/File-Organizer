# .glob pesquisa com  eficiencia arquivos que correspondem a um padrão
# (nomes ou extensões semelhantes) em uma pasta, 
# mas não pesquisa em subpastas. 
# se você quiser pesquisar em subpastas também, 
# você pode usar o método .rglob().
from pathlib import Path

pasta = Path(r"C:\Users\André\Downloads")

# lista todos os arquivos que terminam com .jpg
if pasta.exists():
    for arquivo_jpg in pasta.glob("*.jpg"):
        print(f"Encontrado: {arquivo_jpg.name} ({arquivo_jpg.stat().st_size} bytes)")
else:
    print(f"A pasta {pasta} não existe.")
