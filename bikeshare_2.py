import time as time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#description to method get_filters()
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    go_on_city = 1
    city_list = []
    while go_on_city == 1:
        city_input = input("Please enter your city: ")
        for city, city_csv in CITY_DATA.items():
            city_list.append(city)
            #print(city_list)
        if city_input in city_list:
            go_on_city = 0
        else:
            print("Please only get the cities: chicago, new york city, washington.")
            go_on_city = 1

    # TO DO: get user input for month (all, january, february, ... , june)
    go_on_month = 1
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    while go_on_month == 1:
        month = input("Please enter your month: ")
        if month in months:
            go_on_month = 0
        elif month == "all":
            go_on_month = 0
        else:
            print("Please enter a valid month or all.")
            go_on_month = 1

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    go_on_weekday = 1
    weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    while go_on_weekday == 1:
        weekday = input("Please enter your day: ")
        if weekday in weekdays:
            go_on_weekday = 0
        elif weekday == "all":
            go_on_weekday = 0
        else:
            print("Please enter a valid day or all.")
            go_on_weekday = 1

    print('-'*40)
    return city_input, month, weekday

#-------------------------------------------------------------------------------

#method load_data load all data out of csv
def load_data(city, month, weekday):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    data = pd.read_csv(CITY_DATA.get(city))

#1-Step: change in datetime
    data['Start Time'] = pd.to_datetime(data['Start Time'])
#2-Step: create & fill rows month & weekdays
    data['month'] = data['Start Time'].dt.month_name()
    data['weekdays'] = data['Start Time'].dt.day_name()
#3-Step: filter with user-input month & weeekday
    #print(month)
    #data = data[data['month']==month]
    #data = data['weekday']==weekday
    if month != 'all':
        data = data[data.month.eq(month)]
    if weekday != 'all':
        data = data[data.weekdays.eq(weekday)]

    #print(data.head())

    return data
    #return df

#-------------------------------------------------------------------------------

#method time_stats show time relevant data
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('Most common week: {}'.format(df['weekdays'].mode()[0]))

    # TO DO: display the most common start hour
    print('Most common start hour: {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most commonly used end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    #df['com_station'] = (df['Start Station'] + ' - ' + df['End Station'])
    print('Most frequent combination station: {}'.format((df['Start Station'] + ' -> ' + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = float(df['Trip Duration'].sum())
    #print(total_time)
    #Week
    weeks = total_time // ( 7 * 24 * 3600)
    rest_time = total_time % ( 7 * 24 * 3600)
    #Day
    day = rest_time // (24 * 3600)
    rest_time = rest_time % (24 * 3600)
    #Hour
    hour = rest_time // 3600
    rest_time %= 3600
    #Minute
    minutes = rest_time // 60
    rest_time %= 60
    #Seconds
    seconds = rest_time
    print("Total travel time: w:d:h:m:s-> %d:%d:%d:%d:%d" % (weeks, day, hour, minutes, seconds))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean(axis = 0)
    #print(mean_travel_time)
    #Week
    weeks = mean_travel_time // ( 7 * 24 * 3600)
    rest_time = mean_travel_time % ( 7 * 24 * 3600)
    #Day
    day = rest_time // (24 * 3600)
    rest_time = rest_time % (24 * 3600)
    #Hour
    hour = rest_time // 3600
    rest_time %= 3600
    #Minute
    minutes = rest_time // 60
    rest_time %= 60
    #Seconds
    seconds = rest_time
    print("Mean travel time: w:d:h:m:s-> %d:%d:%d:%d:%d" % (weeks, day, hour, minutes, seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    for key, value in (df['User Type'].value_counts()).items():
        print('Count user types: ', key, ': ', value)

    # TO DO: Display counts of gender
    #print(df.isnull().any())
    print('\n')
    for key, value in (df['Gender'].value_counts()).items():
        print('Count gender types: ', key, ': ', value)

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\n')
    print('Oldest birth: {}'.format(int(df['Birth Year'].min())))
    print('Youngest birth: {}'.format(int(df['Birth Year'].max())))
    print('Most common birth: {}'.format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------

def main():
    while True:
        city, month, day = get_filters()
        #city = 'chicago'
        #month = 'all'
        #day = 'all'
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
