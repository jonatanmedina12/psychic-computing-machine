# Análisis de Datos de Excel

Este proyecto proporciona un script de Python para analizar y visualizar datos de un archivo Excel. Está diseñado específicamente para trabajar con un conjunto de datos que incluye variables como 'Identific_Numerica', 'Discrim_NUmerica', 'NUm_faltante', entre otras.

## Características

- Carga de datos desde un archivo Excel
- Conversión automática de tipos de datos
- Generación de varios gráficos de análisis:
  - Matriz de correlación
  - Histogramas
  - Boxplots
  - Gráfico de medias
  - Matriz de dispersión (para las primeras 4 variables)
  - Pairplot (si hay 5 o menos variables)
- Análisis estadístico básico
- Detección de valores faltantes

## Requisitos

- Python 3.6+
- pandas
- numpy
- matplotlib
- seaborn
- openpyxl

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/jonatanmedina12/psychic-computing-machine.git
   cd psychic-computing-machine
   ```

2. Instala las dependencias:
   ```
   pip install pandas numpy matplotlib seaborn openpyxl
   ```

## Uso

1. Coloca tu archivo Excel en el directorio del proyecto o actualiza la ruta en el script.

2. Modifica la variable `ruta_archivo` en la función `main()` del script para que apunte a tu archivo Excel:

   ```python
   ruta_archivo = 'ruta/a/tu/archivo.xlsx'
   ```

3. Ejecuta el script:

   ```
   python analisis_excel.py
   ```

4. Los gráficos generados se guardarán como archivos PNG en el mismo directorio que el script.

## Estructura del Proyecto

```
.
├── analisis_excel.py
├── README.md
└── datos/
    └── tu_archivo_excel.xlsx
```

## Resultados

El script generará los siguientes archivos:

- `matriz_correlacion.png`: Muestra las correlaciones entre variables.
- `histogramas.png`: Distribuciones de cada variable.
- `boxplots.png`: Muestra la distribución y valores atípicos de cada variable.
- `media_variables.png`: Gráfico de barras con la media de cada variable.
- `matriz_dispersion.png`: Gráfico de dispersión para las primeras 4 variables (si hay más de 4).
- `pairplot.png`: Matriz de gráficos de dispersión (si hay 5 o menos variables).

Además, imprimirá en la consola:
- Estadísticas resumidas de cada variable.
- Recuento de valores faltantes por columna.

## Contribuir

Si deseas contribuir a este proyecto, por favor:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`).
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`).
4. Haz push a la rama (`git push origin feature/AmazingFeature`).
5. Abre un Pull Request.

## Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.

