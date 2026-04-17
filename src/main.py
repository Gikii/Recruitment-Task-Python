import argparse

from src.data_handler import load_data, save_to_csv
from src.data_processor import DataProcessor
from src.data_visualizer import create_average_age_chart, create_population_chart


def main():
    #Initialize the argument parser to handle command-line inputs
    parser = argparse.ArgumentParser(description='')

    #Available command-line arguments
    parser.add_argument("-i", "--input", required=True, help="Input file "
                                                             "in JSON format")

    parser.add_argument("-f", "--filter", type=int, default=0,
                        help="Filter by age")

    parser.add_argument("-o", "--output", help="Path to output file "
                                               "in CSV format")

    parser.add_argument("-p", "--plot", action="store_true",
                        help="Create chart")

    args = parser.parse_args()

    print(f"Loading {args.input}...")

    users = load_data(args.input)
    if not users:
        print("No users found")
        return

    processor = DataProcessor(users)
    if (args.filter):
        filtered_users = processor.filter_by_age(args.filter)
        if not filtered_users:
            print("No user matched filter")
            return
        #Update the processor to work with the filtered subset
        processor = DataProcessor(filtered_users)

    statistics = processor.calculate_statistics()
    city_averages = processor.get_average_age_by_city()

    print(f"Average age: \t{statistics['average_age']}")

    print("\nUsers in cities:")
    for city, count in statistics['cities'].items():
        print(f" - {city}: {count}")

    print("\nAverage age in cities:")
    for city, avg in city_averages.items():
        print(f" - {city}: {avg:.1f}")

    print(
        f"Oldest: \t{statistics['oldest_user'].name} ({statistics['oldest_user'].age}, "
        f"{statistics['oldest_user'].city})")
    print(
        f"Youngest: \t{statistics['youngest_user'].name} ({statistics['youngest_user'].age}, "
        f"{statistics['youngest_user'].city})")

    # Export the processed data to CSV if an output path is specified
    if args.output:
        save_to_csv(processor.users, args.output)

    # Generate visual charts if the --plot flag is enabled
    if args.plot:
        create_population_chart(statistics['cities'])
        create_average_age_chart(city_averages)


if __name__ == "__main__":
    main()
