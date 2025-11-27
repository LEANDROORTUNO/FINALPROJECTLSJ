from pathlib import Path
from typing import Tuple, Dict, Any # Importamos Dict y Any para el tipado
import matplotlib.pyplot as plt
import numpy as np
import PeriodoT as PT
import Constante_k as CK
import CoefiA as CA
#poetry run python CodigoProyecto/GraficaMovArmonico.py

def generate_mas_data(A: float, k: float, m: float, t_max: float) -> Dict[str, Any]:
    """
    Genera y devuelve los datos del M.A.S. en un diccionario.
    """
    omega = np.sqrt(k / m)
    t = np.linspace(0, t_max, 500)
    x = A * np.cos(omega * t) 
    
    # Devolvemos un diccionario con las claves necesarias
    data = {
        't': t,
        'x': x,
        'tName': "Tiempo (s)",
        'xName': "Posición (m)",
        'm': m, # Agregamos la masa para el título
        'k': k  # Agregamos k para el título
    }
    
    return data

def make_plot(data: Dict[str, Any]) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['t'], data['x'], marker=None, color='red', linewidth=2)
    
    ax.set_title(f"Movimiento Armónico Simple (M={data['m']:.1f}kg, K={data['k']:.1f}N/m)", fontsize=14)
    ax.set_xlabel(data['tName'], fontsize=12)
    ax.set_ylabel(data['xName'], fontsize=12)
    
    ax.axhline(0, color='black', linestyle='-', linewidth=0.8) 
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
    
    fig.tight_layout()
    return fig, ax

# --- Las funciones save_plot y main quedan casi iguales ---
def save_plot(fig: plt.Figure, filename: str | Path) -> None:
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(filename, format="png", dpi=150)

# Parámetros del M.A.S.
A = CA.promedio()
k = CK.main()
m = 9.0
T= PT.periodoT()


def main() -> None:
    mas_data = generate_mas_data(A, k, m, T)
    fig, _ = make_plot(mas_data)
    
    output_filename = "GraficosPoetry/GraficoOscilaciones.png"
    save_plot(fig, output_filename)
    
    print(f"✅ Gráfico guardado exitosamente en: {output_filename}")
    
# main
if __name__ == "__main__":
    main()