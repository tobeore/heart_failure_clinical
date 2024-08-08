import pandas as pd
from scipy.stats import mannwhitneyu, chi2_contingency

def feature_significance(numbers,target_column):
    significant_features = {}
    for col in numbers:
        # this performs Mann-Whitney u Test
        stat, p = mannwhitneyu(numbers[numbers[col],target_column])
        #stat,p = mannwhitneyu(numbers[numbers[target_column]==1][column],numbers[numbers[target_column]==0][column])
        if p < 0.05:
            significant_features[column] = p
            # a block of code to create a Chi square operation
            contingency = pd.crosstab(numbers[target_column],numbers[col])
            stat, p, dof, expected = chi2_contingency(contingency)
            if p < 0.05:
                significant_features[column] = p               
    return significant_features




def feature_importance(x_train,y_train):
    #creating a random forest classifier
    ran_class = RandomClassifier()
    ran_class.fit(x_train,y_train)
    
    #getting important features
    feature_importance = pd.DataFrame(ran_class.feature_importances_,index = X_train.columns, columns = ["Important"]).sort_values("Important", ascending = False)
    return feature_importance


def select_feature(significant_features,feature_importance):
    #uses the features base on Mann Whitney u and chi test result
    selected_features = [feature for feature in significant_features if feature in feature_importance.index]
    
    #this select features to be used based on the feature importance
    selected_features += list(feature_importance.head(n).index)
    return selected_features 
        