import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

df = pd.read_csv('deletion.tsv', delimiter='\t')

#drop whatever will not help
df = df.drop(['chr_start_end', 'id'], axis=1)

#split into labeled and unlabeled sets according to status value
labeled = df[df['status'].notnull()]
unlabeled = df[df['status'].isnull()]

#status column not needed
unlabeled = unlabeled.drop(['status'], axis=1)

#create the target column
target = labeled['status']
labeled = labeled.drop(['status'], axis=1)

#split labeled data into test and train sets
X_train, X_test, y_train, y_test = train_test_split(labeled, target, test_size=0.2,random_state=1020)

'Decision tree'
DT_model = tree.DecisionTreeClassifier()
DT_model.fit(X_train, y_train)
y_predicted = DT_model.predict(X_test)
DT_error_rate = np.sum(y_predicted != y_test)/y_test.shape[0]
print(f'Success rate DT: {1 - DT_error_rate}')
print(f'Success rate DT: {DT_model.score(X_test, y_test)}') #is the same as success rate, that's good
unlabeled_pred = DT_model.predict(unlabeled)

#write data into a file
with open('decision_tree.csv', 'w') as DT:
    DT.write(f'Success rate DT (labeled set): {DT_model.score(X_test, y_test)} \n')
    np.savetxt(DT, unlabeled_pred, delimiter=" ", fmt='%d')
    
'Random Forest'
RF_model = RandomForestClassifier()
RF_model.fit(X_train, y_train)
y_predicted = RF_model.predict(X_test)
print(f'Success rate RF: {RF_model.score(X_test, y_test)}') #is generally a bit better than DT but not in this case
unlabeled_pred = RF_model.predict(unlabeled)

#write data into a file
with open('random_forest.csv', 'w') as RF:
    RF.write(f'Success rate RF (labeled set): {RF_model.score(X_test, y_test)} \n')
    np.savetxt(RF, unlabeled_pred, delimiter=" ", fmt='%d')

'Neural Networks'
NN_model = MLPClassifier(activation='logistic', solver='adam',hidden_layer_sizes=(35,50),alpha=0.003, random_state=1020)
NN_model.fit(X_train, y_train)
y_predicted = NN_model.predict(X_test)
print(f'Success rate NN: {NN_model.score(X_test, y_test)}')
unlabeled_pred = NN_model.predict(unlabeled)

#write data into a file
with open('neural_network.csv', 'w') as NN:
    NN.write(f'Success rate NN (labeled set): {NN_model.score(X_test, y_test)} \n')
    np.savetxt(NN, unlabeled_pred, delimiter=" ", fmt='%d')

#success rates were good between 0.92 and 0.98
