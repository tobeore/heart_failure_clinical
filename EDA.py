import pandas as pd
import matplotlib.pyplot as plt

def descriptive_statistical_analysis(numbers):
    """calculates mean, median and mode using python Panda library
    parameter
    *********
    A set of numerical data

    Returns
    *******
    mean, median, mode

    Example
    *******
    numbers = [5,6,1,2,5,3,7,4,8]
    >>>> measures_of_location(numbers)
    (4.555555555555555, 5.0, 5)

     numbers = [5,6,10,2.5,50,3,7,4,8]
    >>>> measures_of_location(numbers)
    (10.61111111111111, 6.0, 2.5)

        """
    import pandas as pd
    methods = {}
    for column in numbers.columns:
        methods[column] = {"mean": [numbers[column].mean()],
                           "median":[ numbers[column].median()],
                           "mode": [numbers[column].mode()[0]],
                           "var": [numbers[column].var()],
                           "std_dev": [numbers[column].std()],
                           "min": [numbers[column].min()],
                           "max":[numbers[column].max()],
                           "count":[numbers[column].count()],
                           "25%":[numbers[column].quantile(0.25)],
                           "50%":[numbers[column].quantile(0.50)],
                           "75%":[numbers[column].quantile(0.75)],
                           "skewness":[numbers[column].skew()],
                           "kurtosis":[numbers[column].kurtosis()]}
    data_method = pd.DataFrame(methods)
    return data_method
                    
    

def check_missing_values(numbers):
    """Checks for missing values in a dataset using python pandas library
        parameter
        *********
        A set of  data

        Returns
        *******
        missing(sum of the values of missing numbers and their index)
    """
    
    missing = numbers.isna().sum().to_frame().rename(columns={0: "Missing Num"})
    missing["index"] = missing.index.map(lambda x: ",".join(map(str, numbers.loc[numbers[x].isna()].index.values)))
    return missing

def graph(numbers):
    """creates a bar chart
        *********
        A set of  data

        Returns
        *******
        None
    """
    
    numbers.plot(kind="bar")
    plt.xlabel("values")
    plt.ylabel("frequency")
    plt.show()


    return None
     




                