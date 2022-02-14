import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

class MyImputer(SimpleImputer):

    """
    Subclass of SimpleImputer that allows feature names to be maintained
    """

    def transform(self, X, y=None):

        feature_names = X.columns
        
        trans = super().transform(X)

        return pd.DataFrame(trans, columns = feature_names)

    def fit_transform(self, X, y=None):

        feature_names = X.columns
        
        trans = super().fit_transform(X)

        return pd.DataFrame(trans, columns = feature_names)

def read_data(path):

    # read in data
    df = pd.read_csv(path)
    # remove unwanted ID columns
    df = df.drop(columns=['index','PLAYER'])

    X = df.drop(columns = ['next_3P%', '3pt_dif'])
    y1, y2 = df['next_3P%'], df['3pt_dif']
    return df, X, y1, y2

def pipeline(features):

    numerical_x = features.select_dtypes(include=['float64','int64']).columns
    categorical_x = features.select_dtypes(include=['object', 'bool']).columns

    numeric_transformer = Pipeline(steps=[
        ('imputer', MyImputer(strategy='mean')),
        ('scaler', StandardScaler())])

    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    if len(numerical_x) > 0 and len(categorical_x) > 0:

        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', categorical_transformer, categorical_x),
                ('num', numeric_transformer, numerical_x)
                ]
            )
    elif len(numerical_x) > 0 : 
        
        preprocessor = numeric_transformer
    
    else:
        preprocessor = categorical_transformer

    return preprocessor

def model_train(model, X, y, preprocessor, param_grid=None):
    """
    Create and train, plot predicted values with residuals
    """
    # create pipeline
    reg = Pipeline(steps=[('preprocessor', preprocessor),
                      ('model', model)])

    if param_grid is None:
        model = reg
    
    else:
        # grid search
        model = GridSearchCV(reg, param_grid)

    # fit model
    model.fit(X,y)

    # print scores
    print(scores(model, X, y))

    return model

def resid_plot(model,X,y):
    # Plot residuals
    X_p = model.predict(X)
    resid = y - X_p
    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(y=resid, x=X_p,  color='black')
    ax.set_xlabel('Predicted Y')
    ax.set_ylabel('Residuals')
    plt.show()
    return None



def scores(pipe, X, Y):
    """
    Display training and test error
    """
    Y_p = pipe.predict(X) 
    r2 = r2_score(Y,Y_p)
    mse = mean_squared_error(Y,Y_p)
    mae = mean_absolute_error(Y,Y_p)
    score_string = 'rsquared:\t{0:0.3f}\nMean squared error:\t{1:0.6f}\nMean absolute error:\t{2:0.4f}'.format(r2,mse,mae)

    return score_string

# def scores(pipe, X_train, X_test, Y_train, Y_test):
#     """
#     Display training and test error
#     """
#     # predicted Y value
#     Y_trainp = pipe.predict(X_train) 
#     Y_testp = pipe.predict(X_test)
#     # training error 
#     print('Training Error:')
#     print('rsquared:\t{0:0.3f}'.format(r2_score(Y_train,Y_trainp)))
#     print('Mean squared error:\t{0:0.6f}'.format(mean_squared_error(Y_train,Y_trainp)))
#     print('Mean absolute error:\t{0:0.4f}'.format(mean_absolute_error(Y_train,Y_trainp)))
#     print()
#     # test error
#     print('Test Error:')
#     print('rsquared:\t{0:0.3f}'.format(r2_score(Y_test,Y_testp)))
#     print('Mean squared error:\t{0:0.6f}'.format(mean_squared_error(Y_test,Y_testp)))
#     print('Mean absolute error:\t{0:0.4f}'.format(mean_absolute_error(Y_test,Y_testp)))
#     return None