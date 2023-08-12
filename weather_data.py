import argparse

from Reports import Reports

def read_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", required=False, help="Annual Report")
    parser.add_argument("-a", required=False, help="Monthly Report")
    parser.add_argument("-c", required=False, help="Bar Chart Report")

    return parser.parse_args()

def report_generator(args, weather):
    if args.e:
        year = int(args.e)
        weather.annual_report(year)
    if args.a:
        year, month = int(args.a[:4]), int(args.a[5:])
        weather.monthly_report(year, month)
    if args.c:
        year, month = int(args.c[:4]), int(args.c[5:])
        weather.bar_chart_report(year, month)


if __name__ == "__main__":
    args = read_arguments()
    weather = Reports()

    report_generator(args, weather)