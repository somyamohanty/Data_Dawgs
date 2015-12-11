#####################################################################
# Author: Siddhant Sutar
# Description: Cross-validation analysis for linear regression model. 
#####################################################################
 
# train = training data-set
# test = testing data-set
# genres = sparse feature matrix for genres, genres_list = list of feature names for genres
# actors = sparse feature matrix for actors, actors_list = list of feature names for actors
# directors = sparse feature matrix for directors, directors_list = list of feature names for directors

actual = {}
predicted = {}
y = train.imdbRating
model = LinearRegression()
train = train.fillna('')
for index, row in test.iterrows():
    features = []
    g = str(row["Genre"]).split(', ')
    a = str(row["Cast"]).split(', ')
    d = str(row["Director"]).split(', ')
    for each in g:
        if each in genres_list:
            features.append(genres[:, genres_list.index(str(each))+1].toarray().flatten())
    for each in a:
        if each in actors_list:
            features.append(actors[:, actors_list.index(str(each))+1].toarray().flatten())
    for each in d:
        if each in directors_list:
            features.append(directors[:, directors_list.index(str(each))+1].toarray().flatten())
    X = csr_matrix(features).transpose()
    if X.shape[0] != 0:
        model.fit(X, y)
        actual[row["Title"]] = row["imdbRating"]
        predicted[row["Title"]] = model.predict(np.ones(len(features)))[0]