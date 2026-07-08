import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set style for a clean corporate look
sns.set_theme(style="whitegrid")
plt.rcParams["font.family"] = "sans-serif"


def plot_digital_adoption():
    """Generates the historical Digital Adoption Growth Rate line chart."""
    years = ["2021", "2022", "2023", "2024", "2025"]
    growth_rates = [15, 11, 8, 6, 4]

    plt.figure(figsize=(8, 4))
    plt.plot(
        years,
        growth_rates,
        marker="o",
        color="#c19a27",
        linewidth=2.5,
        markersize=8,
    )

    # Adding labels and formatting
    for i, txt in enumerate(growth_rates):
        plt.annotate(
            f"{txt}%",
            (years[i], growth_rates[i]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontweight="bold",
        )

    plt.title(
        "Meridian Historical Digital Adoption YoY Growth Rate (Stagnation Trend)",
        fontsize=12,
        pad=15,
        fontweight="bold",
    )
    plt.ylabel("YoY Growth Rate (%)")
    plt.ylim(0, 18)
    plt.tight_layout()
    plt.savefig("../data/digital_adoption_trend.png", dpi=300)
    plt.show()


def plot_financial_contribution():
    """Generates a breakdown bar chart of the $310M annual value opportunity."""
    data = {
        "Initiative": [
            "AI Underwriting",
            "Branch Optimization",
            "Embedded Finance",
        ],
        "Value ($M)": [140, 95, 75],
    }
    df = pd.DataFrame(data)

    plt.figure(figsize=(7, 4))
    colors = ["#112233", "#224466", "#c19a27"]
    bars = plt.bar(
        df["Initiative"], df["Value ($M)"], color=colors, width=0.6
    )

    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            yval + 3,
            f"${yval}M",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    plt.title(
        "Annual Value Creation Attribution (Total: $310M)",
        fontsize=12,
        pad=15,
        fontweight="bold",
    )
    plt.ylabel("Value Contribution ($ Millions)")
    plt.ylim(0, 160)
    plt.tight_layout()
    plt.savefig("../data/financial_attribution.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    # Ensure directories exist and run plots
    import os

    os.makedirs("../data", exist_ok=True)
    plot_digital_adoption()
    plot_financial_contribution()
