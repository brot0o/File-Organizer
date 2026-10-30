from pathlib import Path

file=Path("new_object.txt")

#target_path=Path("new_object.txt")

if file.exists():
    target_path=input("Digite o novo nome do arquivo (com extensão): ")
    file.rename(target_path)
    print(f"Arquivo {file.name} renomeado para {target_path}")
else:
    print(f"Arquivo {file.name} não encontrado.")