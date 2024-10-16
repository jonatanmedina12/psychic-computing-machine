import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración para evitar advertencias de copia
pd.options.mode.chained_assignment = None


def cargar_datos(ruta_archivo):
    try:
        return pd.read_excel(ruta_archivo)
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None


def preparar_datos(df, columnas):
    columnas_existentes = [col for col in columnas if col in df.columns]
    df_analisis = df[columnas_existentes].copy()

    for col in df_analisis.columns:
        try:
            df_analisis[col] = pd.to_numeric(df_analisis[col])
        except ValueError:
            print(f"No se pudo convertir la columna '{col}' a numérica. Se mantiene como está.")

    return df_analisis


def crear_matriz_correlacion(df):
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    plt.savefig('matriz_correlacion.png')
    plt.close()


def crear_histogramas(df):
    df.hist(figsize=(15, 15), bins=20)
    plt.suptitle('Histogramas de las variables', y=1.02)
    plt.tight_layout()
    plt.savefig('histogramas.png')
    plt.close()


def crear_boxplots(df):
    plt.figure(figsize=(15, 10))
    df.boxplot()
    plt.title('Boxplots de las variables')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('boxplots.png')
    plt.close()


def crear_pairplot(df):
    if len(df.columns) <= 5:
        sns.pairplot(df)
        plt.suptitle('Pairplot de las variables', y=1.02)
        plt.tight_layout()
        plt.savefig('pairplot.png')
        plt.close()
    else:
        print("Pairplot no generado debido a la gran cantidad de variables.")


def crear_grafico_medias(df):
    plt.figure(figsize=(12, 6))
    df.mean().plot(kind='bar')
    plt.title('Media de cada variable')
    plt.ylabel('Valor medio')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('media_variables.png')
    plt.close()


def crear_matriz_dispersion(df):
    if len(df.columns) > 4:
        sns.pairplot(df.iloc[:, :4])
        plt.suptitle('Matriz de dispersión (primeras 4 variables)', y=1.02)
        plt.tight_layout()
        plt.savefig('matriz_dispersion.png')
        plt.close()


def analisis_estadistico(df):
    print("\nEstadísticas resumidas:")
    print(df.describe())
    print("\nValores faltantes por columna:")
    print(df.isnull().sum())


def main():
    ruta_archivo = r'D:\Repositorios\psychic-computing-machine\app\static\RESUMEN DE GRUPOS.xlsx'
    columnas = [
        'Identific_Numerica', 'Discrim_NUmerica', 'NUm_faltante', 'Suma_resta', 'Log_inicial',
        'PRETEST CONTROL', 'PRETEST EXPERIMENTAL',
        'POSTEST CONTROL', 'POSTEST INTERVENCION'
    ]

    df = cargar_datos(ruta_archivo)
    if df is None:
        return

    df_analisis = preparar_datos(df, columnas)

    crear_matriz_correlacion(df_analisis)
    crear_histogramas(df_analisis)
    crear_boxplots(df_analisis)
    crear_pairplot(df_analisis)
    crear_grafico_medias(df_analisis)
    crear_matriz_dispersion(df_analisis)

    print("Análisis completado. Se han generado los siguientes archivos:")
    print("- matriz_correlacion.png")
    print("- histogramas.png")
    print("- boxplots.png")
    print("- media_variables.png")
    if len(df_analisis.columns) <= 5:
        print("- pairplot.png")
    if len(df_analisis.columns) > 4:
        print("- matriz_dispersion.png")

    analisis_estadistico(df_analisis)

