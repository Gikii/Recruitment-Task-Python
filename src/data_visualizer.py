import matplotlib.pyplot as plt

def create_population_chart(cities: dict, path: str = "data/population_chart.png") -> None:
    if not cities:
        print("No cities found")
        return

    city_name = list(cities.keys())
    counts = list(cities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(city_name, counts, color='skyblue', edgecolor='navy')

    plt.title("Population by city", fontsize=14)
    plt.xlabel("City", fontsize=12)
    plt.ylabel("Population", fontsize=12)

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig(path)
    plt.close()
    print(f"Saved chart {path}")

def create_average_age_chart(city_averages: dict, path: str = "data/average_age_chart.png") -> None:
    if not city_averages:
        print("No data found")
        return
    city_name = list(city_averages.keys())
    values = list(city_averages.values())

    plt.figure(figsize=(10, 6))

    plt.bar(city_name, values, color='forestgreen', edgecolor='darkgreen')

    plt.title("Average age in cities", fontsize=14)
    plt.xlabel("City", fontsize=12)
    plt.ylabel("Average age", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig(path)
    plt.close()
    print(f"Saved chart {path}")