from sklearn import tree

#[height, weight, shoe size]
X = [[181, 180, 44], [177, 170, 43], [160, 140, 38], [152, 92, 36], [123, 14, 23],
	[123, 33, 45], [192, 111, 23], [121, 42, 92], [191, 233, 94], [123,23, 34], 
	[181, 85, 43]]

Y = ['female', 'female', 'female', 'female', 'female', 'female', 'male',
	 'male', 'male', 'male', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[183, 143, 38]])

print prediction