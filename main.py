import argparse
import json
from network_analysis import load_data, analyze, generate_response


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze network performance data")
    parser.add_argument("--input", default="input.csv", help="CSV file with network metrics")
    parser.add_argument("--output", default="responses.json", help="File to write JSON results")
    args = parser.parse_args()

    df = load_data(args.input)
    results = analyze(df)
    summary = generate_response(results)

    with open(args.output, "w") as fh:
        json.dump({"results": results, "summary": summary}, fh, indent=2)

    print(summary)


if __name__ == "__main__":
    main()
