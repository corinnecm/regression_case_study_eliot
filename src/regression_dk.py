
'saledate'
- Year
- Month

'YearMade' drop year 1000

'auctioneerID' drop na

'MachineHoursCurrentMeter' drop na

'fiBaseModel' drop na

'ProductSize', Unknown, Keep
'ProductGroup' - No NA

from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression


def crossVal(X, y):

    kf = KFold(n_splits=5)

    results = []

    # For each fold:
    for train_index, test_index in kf.split(X):
        #print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # train the model with the (k-1) other folds,
        linear = LinearRegression()
        linear.fit(X_train, y_train)

        # use the trained model to predict the target values of each example in the current fold,
        test_predicted = linear.predict(X_test)

        # calculate the RMSE of the current fold's predicted values,
        # k_rmse = rmse(y_test, test_predicted)
        # np.sqrt(mean_squared_error(true, predicted))

        k_rmse = rmse(y_train, train_predicted)

        # store the RMSE for this fold.
        results.append(k_rmse)

    # Average the k results of your error metric. Return the average error metric.
    return np.mean(k_rmse)
