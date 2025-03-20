# train_yolov8.py

import os
from ultralytics import YOLO

def main():
    """
    Script para entrenar y evaluar un modelo YOLOv8 utilizando la librería ultralytics.
    Asegúrate de que la estructura de carpetas y el archivo data.yaml estén correctos.
    """
    # Asegúrate de que estás en la carpeta correcta donde se encuentra data.yaml
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, "data.yaml")

    # 1. Crear o cargar el modelo (en este ejemplo, partimos de yolov8n.pt)
    model = YOLO("yolov8n.pt")  # Puedes cambiar a yolov8s.pt, yolov8m.pt, etc.

    # 2. Entrenar el modelo
    # Ajusta los parámetros de epochs, imgsz, batch, etc., según tus necesidades.
    model.train(
        data=data_file,       # archivo YAML con rutas y clases
        epochs=50,            # número de épocas
        imgsz=640,            # tamaño de la imagen para entrenamiento
        batch=8,              # tamaño de batch
        name="yolov8_vehicle",# nombre del experimento
        project="runs",       # carpeta donde se guardarán los resultados
        pretrained=True       # si usas pesos pre-entrenados
    )

    # 3. Validar/Evaluar el modelo en el conjunto de validación
    # Por defecto, el entrenamiento ya realiza validación después de cada época,
    # pero podemos forzar una evaluación adicional con el mejor modelo guardado.
    best_weights_path = os.path.join("runs", "detect", "yolov8_vehicle", "weights", "best.pt")
    model = YOLO(best_weights_path)
    metrics = model.val(data=data_file)
    print("===== Resultados de Validación =====")
    print(metrics)

    # 4. (Opcional) Prueba con el conjunto de test y guarda las predicciones
    test_images_dir = os.path.join(current_dir, "test", "images")
    predictions = model.predict(
        source=test_images_dir,
        conf=0.25,        # umbral de confianza
        save=True,        # guarda los resultados en runs/predict
        name="yolov8_vehicle_test"
    )

    print("===== Inferencia en conjunto de test finalizada =====")
    print(f"Predicciones guardadas en: runs/detect/yolov8_vehicle_test")

#if __name__ == "__main__":
   # main()
