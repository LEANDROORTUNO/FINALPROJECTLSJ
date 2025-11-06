from pathlib import Path
from typing import Tuple
from CodigoProyecto.LectorCsv import read  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def make_plot_3d(data) -> Tuple[plt.Figure, plt.Axes]:
    fig = plt.figure(figsize=(10, 8)) 
    ax: Axes3D = fig.add_subplot(111, projection='3d')
    ax.scatter(data.x, data.y, data.z, c=data.z, cmap='viridis', marker='o')  
    ax.set_title("Scatter Plot")
    ax.set_xlabel(data.xName)
    ax.set_ylabel(data.yName)
    ax.set_zlabel(data.zName)
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
    fig.tight_layout()
    return fig, ax

def show_plot(fig: plt.Figure) -> None:
    pass 

def save_plot(fig: plt.Figure, filename: str | Path) -> None:
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(filename, format="png", dpi=150)

def main() -> None:
    import sys
    if len(sys.argv) < 2:
                                       
        print("Usage: poetry run python CodigoProyecto/GenerarGrafico.py <file.csv>")
        sys.exit(2)

    csv_path = Path(sys.argv[1])
    data = read(csv_path)
    fig, _ = make_plot_3d(data)
                   
    save_plot(fig, "GraficosPoetry/GraficoTabla1Cam.png")
    print(f"✅ Gráfico guardado exitosamente en: GraficosPoetry/GraficoTabla1Cam.png")

# main
if __name__ == "__main__":
    main()


