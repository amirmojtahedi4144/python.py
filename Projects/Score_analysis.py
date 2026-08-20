##############  WELCOME TO MY SCORE ANALYSIS #############
import pandas as pd

print("=" * 60)
print("           STUDENT SCORE ANALYSIS SYSTEM")
print("=" * 60)


def create_file():
    with open("grades.csv", "w", encoding="utf-8") as file:
        file.write("Name,Math,Science,English\n")
        file.write("Alice,85,90,88\n")
        file.write("Bob,78,82,80\n")
        file.write("Charlie,92,95,94\n")
        file.write("David,70,75,72\n")
        file.write("Eva,88,85,90\n")


def load_data():
    try:
        return pd.read_csv("grades.csv")
    except FileNotFoundError:
        print("File not found!")
        exit()


def analyze(df):
    df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

    df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

    # Grade
    def grade(avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    df["Grade"] = df["Average"].apply(grade)

    # Pass / Fail
    df["Status"] = df["Average"].apply(
        lambda x: "Pass" if x >= 60 else "Fail"
    )
    df["Rank"] = df["Average"].rank(
        ascending=False,
        method="dense"
    ).astype(int)

    return df


def report(df):

    print("\nStudent Table")
    print("-" * 60)
    print(df)
    print("\nFirst Three Students")
    print("-" * 60)
    print(df.head(3))

    print("\nInformation")
    print("-" * 60)
    df.info()

    print("\nStatistics")
    print("-" * 60)
    print(df.describe())

    print("\nAverage Score Of Each Subject")
    print("-" * 60)
    print(df[["Math", "Science", "English"]].mean())

    print("\nHighest Scores")
    print("-" * 60)
    print(df[["Math", "Science", "English"]].max())

    print("\nLowest Scores")
    print("-" * 60)
    print(df[["Math", "Science", "English"]].min())

    top_student = df.loc[df["Average"].idxmax()]
    weak_student = df.loc[df["Average"].idxmin()]

    print("\nTop Student")
    print("-" * 60)
    print(top_student)

    print("\nLowest Student")
    print("-" * 60)
    print(weak_student)

    print("\nGrade Distribution")
    print("-" * 60)
    print(df["Grade"].value_counts())

    print("\nRanking")
    print("-" * 60)
    print(df.sort_values("Rank")[["Rank", "Name", "Average"]])


def save(df):
    df.to_csv("final_report.csv", index=False)
    print("\nReport saved as final_report.csv")


def main():
    create_file()

    df = load_data()

    df = analyze(df)

    report(df)

    save(df)

    print("\n" + "=" * 60)
    print("Analysis Completed Successfully")
    print("=" * 60)

if __name__ == "__main__":
    main()