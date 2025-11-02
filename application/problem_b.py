import pulp as pl
import numpy as np
import matplotlib.pyplot as plt


def resolver_problema(problem_name):
    """Define e resolve o problema de programação linear."""

    # Modelo
    model = pl.LpProblem(problem_name, pl.LpMaximize)

    # Variáveis
    x1 = pl.LpVariable("x1", lowBound=0)
    x2 = pl.LpVariable("x2", lowBound=0)

    # Função objetivo
    model += 2 * x1 + x2

    # Restrições
    model += -2*x1 + x2 <= 2
    model += 2*x1 + x2 <= 4

    # Resolver
    model.solve(pl.PULP_CBC_CMD(msg=False))

    # Resultados
    resultado = {
        "problem_name": problem_name,        
        "status": pl.LpStatus[model.status],
        "x1": x1.value(),
        "x2": x2.value(),
        "z": pl.value(model.objective)
    }

    return resultado


def plotar_regiao_viavel(result):
    """Plota a região viável e destaca o ponto ótimo."""

    # Recebe a solução ótima
    x1_opt, x2_opt, z_opt, status, problem_name = result["x1"], result["x2"], result["z"], result["status"], result["problem_name"]

    # Limites do gráfico
    x_min, x_max = 0, 6
    y_min, y_max = 0, 4.5

    # Espaço bidimensional (grade de pontos)
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = np.linspace(y_min, y_max, 400)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Região viável
    feasible = (Y <= 2*X + 2) & (Y <= -2*X + 4)

    plt.figure(problem_name, figsize=(7, 6))
    plt.imshow(feasible.astype(int), extent=(x_min, x_max, y_min, y_max), origin="lower",
               cmap="Greens", alpha=0.3)

    # Restrições
    plt.plot(x_vals, 2 * x_vals + 2, "orange", label=r"$-2x_1 + x_2 \leq 2$")
    plt.plot(x_vals, -2 * x_vals + 4, "purple", label=r"$2x_1 + x_2 \leq 4$")

    # Solução ótima
    if status == "Optimal":
        plt.plot(x1_opt, x2_opt, "ro", markersize=10, label="Ótimo")
        plt.text(x1_opt + 0.1, x2_opt + 0.1, f"({x1_opt:.1f}, {x2_opt:.1f})\nZ={z_opt:.1f}")

    # Estética
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.title("Região viável e solução ótima")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    """Executa o problema e plota os resultados."""
    
    problem_name = "Problema_B"
    result = resolver_problema(problem_name)

    print("Problema:", result["problem_name"])
    print("Status:", result["status"])
    print("x1 =", result["x1"])
    print("x2 =", result["x2"])
    print("z* =", result["z"])

    plotar_regiao_viavel(result)


if __name__ == "__main__":
    main()
