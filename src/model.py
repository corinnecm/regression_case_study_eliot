import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import accuracy_score, recall_score, precision_score

from cleanup import df, df_full, df_test, prices



model = smf.ols(formula = 'SalePrice ~ YearMade**2 + UsageBand + YearMade*UsageBand + ProductSize + auctioneerID + ProductGroup + sale_year + sale_month + fiBaseModel', data=df)

fit = model.fit()

print(fit.summary())

predictions = model.predict(df_test)

print(predictions)

pd.scatter_matrix(df)
plt.show()
