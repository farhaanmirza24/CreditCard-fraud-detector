from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
import numpy as np
from sklearn.ensemble import VotingClassifier

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
import pandas as pd

# Create your views here.
from Remote_User.models import ClientRegister_Model,detect_fraudulent_cc_transactions,detection_ratio,detection_accuracy

def login(request):


    if request.method == "POST" and 'submit1' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            enter = ClientRegister_Model.objects.get(username=username,password=password)
            request.session["userid"] = enter.id

            return redirect('ViewYourProfile')
        except:
            pass

    return render(request,'RUser/login.html')

def Register1(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city)

        return render(request, 'RUser/Register1.html')
    else:
        return render(request,'RUser/Register1.html')

def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'RUser/ViewYourProfile.html',{'object':obj})


def Detection_Of_Fraudulent_CreditCard_Transactions(request):

        if request.method == "POST":

            Fid= request.POST.get('Fid')
            Trans_Date= request.POST.get('Trans_Date')
            CC_No= request.POST.get('CC_No')
            CC_type= request.POST.get('CC_type')
            Trans_Type= request.POST.get('Trans_Type')
            Amount= request.POST.get('Amount')
            Firstname= request.POST.get('Firstname')
            Lastname= request.POST.get('Lastname')
            Gender= request.POST.get('Gender')
            Age= request.POST.get('Age')
            lat= request.POST.get('lat')
            lon= request.POST.get('lon')
            Transid= request.POST.get('Transid')


            df = pd.read_csv('Datasets.csv', encoding='latin-1')

            def apply_response(Label):
                if (Label == 0):
                    return 0  # Fraudulent Not Found
                elif (Label == 1):
                    return 1  # Fraudulent Found

            df['results'] = df['Label'].apply(apply_response)

            cv = CountVectorizer()

            X = df['Fid']
            y = df["results"]

            print("X Values")
            print(X)
            print("Labels")
            print(y)

            cv = CountVectorizer(lowercase=False, strip_accents='unicode', ngram_range=(1, 1))
            X = cv.fit_transform(X)

            #X = cv.fit_transform(X)

            models = []
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
            X_train.shape, X_test.shape, y_train.shape

            print("Naive Bayes")
            from sklearn.naive_bayes import MultinomialNB
            NB = MultinomialNB()
            NB.fit(X_train, y_train)
            predict_nb = NB.predict(X_test)
            naivebayes = accuracy_score(y_test, predict_nb) * 100
            print(naivebayes)
            print(confusion_matrix(y_test, predict_nb))
            print(classification_report(y_test, predict_nb))
            models.append(('naive_bayes', NB))


            # SVM Model
            print("SVM")
            from sklearn import svm
            lin_clf = svm.LinearSVC()
            lin_clf.fit(X_train, y_train)
            predict_svm = lin_clf.predict(X_test)
            svm_acc = accuracy_score(y_test, predict_svm) * 100
            print(svm_acc)
            print("CLASSIFICATION REPORT")
            print(classification_report(y_test, predict_svm))
            print("CONFUSION MATRIX")
            print(confusion_matrix(y_test, predict_svm))
            models.append(('svm', lin_clf))


            print("Random Forest Classifier")
            from sklearn.ensemble import RandomForestClassifier
            rf_clf = RandomForestClassifier()
            rf_clf.fit(X_train, y_train)
            rfpredict = rf_clf.predict(X_test)
            print("ACCURACY")
            print(accuracy_score(y_test, rfpredict) * 100)
            print("CLASSIFICATION REPORT")
            print(classification_report(y_test, rfpredict))
            print("CONFUSION MATRIX")
            print(confusion_matrix(y_test, rfpredict))
            models.append(('RandomForestClassifier', rf_clf))


            classifier = VotingClassifier(models)
            classifier.fit(X_train, y_train)
            y_pred = classifier.predict(X_test)

            Fid1 = [Fid]
            vector1 = cv.transform(Fid1).toarray()
            predict_text = classifier.predict(vector1)

            pred = str(predict_text).replace("[", "")
            pred1 = pred.replace("]", "")

            prediction = int(pred1)

            if prediction == 0:
                val = 'Fraudulent Not Found'
            elif prediction == 1:
                val = 'Fraudulent Found'


            print(val)
            print(pred1)

            detect_fraudulent_cc_transactions.objects.create(
            Fid=Fid,
            Trans_Date=Trans_Date,
            CC_No=CC_No,
            CC_type=CC_type,
            Trans_Type=Trans_Type,
            Amount=Amount,
            Firstname=Firstname,
            Lastname=Lastname,
            Gender=Gender,
            Age=Age,
            lat=lat,
            lon=lon,
            Transid=Transid,
            Prediction=val)

            return render(request, 'RUser/Detection_Of_Fraudulent_CreditCard_Transactions.html',{'objs':val})
        return render(request, 'RUser/Detection_Of_Fraudulent_CreditCard_Transactions.html')

