import os

def unificar_clases():
    """
    Recorre todos los archivos .txt dentro de la carpeta 'labels'
    y cambia cualquier clase a '0' (asumiendo que tenemos una sola clase).
    """
    labels_dir = "labels"  # carpeta donde están los .txt

    # Verifica que exista la carpeta 'labels'
    if not os.path.isdir(labels_dir):
        print(f"No se encontró la carpeta: {labels_dir}")
        return

    # Recorre recursivamente la carpeta 'labels'
    for root, dirs, files in os.walk(labels_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                # Lee las líneas originales
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                nuevas_lineas = []
                for line in lines:
                    tokens = line.strip().split()
                    # Asegura que tenga al menos 5 valores (clase + 4 coords)
                    if len(tokens) < 5:
                        continue
                    # Reemplaza la clase original por '0'
                    nueva_linea = "0 " + " ".join(tokens[1:]) + "\n"
                    nuevas_lineas.append(nueva_linea)

                # Sobrescribe el archivo con la nueva clase
                with open(file_path, 'w') as f:
                    f.writelines(nuevas_lineas)

                print(f"Archivo actualizado: {file_path}")

if __name__ == "__main__":
    unificar_clases()
    print("Proceso completado: todas las clases se han establecido en '0'.")
