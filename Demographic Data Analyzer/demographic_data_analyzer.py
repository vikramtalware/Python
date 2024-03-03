import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    gender = df[df['sex'] == "Male"]
    average_age_men = gender['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = df[df['education'] == "Bachelors"].shape[0]
    percentage_bachelors = (bachelors_count / total_people) * 100
    percentage_bachelors = round(percentage_bachelors,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_count = higher_education.shape[0]
    higher_education_income_count = higher_education[higher_education['salary'] == '>50K'].shape[0]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_count = lower_education.shape[0]
    lower_education_income_count = lower_education[lower_education['salary'] == '>50K'].shape[0]

    # percentage with salary >50K
    higher_education_rich = (higher_education_income_count / higher_education_count) * 100
    higher_education_rich = round(higher_education_rich,1)
    lower_education_rich = (lower_education_income_count / lower_education_count) * 100
    lower_education_rich = round(lower_education_rich,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0]
    total_min_hour_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage = (num_min_workers / total_min_hour_workers) * 100
    rich_percentage = round(rich_percentage,1)

    # What country has the highest percentage of people that earn >50K?
    total_by_country = df['native-country'].value_counts()
    high_income_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    percentage_by_country = (high_income_country / total_by_country) * 100
    highest_earning_country = percentage_by_country.idxmax()
    highest_earning_country_percentage = round(percentage_by_country.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_income_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = high_income_india['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print(f"Number of each race:", race_count.to_frame(), sep='\n') 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }