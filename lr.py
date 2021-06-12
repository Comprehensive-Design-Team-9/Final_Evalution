from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib
import matplotlib.pyplot as plt
import pickle
import numpy as np

import pandas as pd



def ml_run(new_sub_csv):

    post = pd.read_csv(new_sub_csv)
    print(type(post))
    print(len(post))
    post = post.fillna(0)
    print(post.isnull().sum())
    #post.drop_duplicates(['url'], keep='first', inplace=True)#, ignore_index=True)
    print("데이터 개수 len(post): ", len(post))
    print(post.head(20))

    # df_one_hot_encoded = pd.get_dummies(post.url)
    # post = pd.concat([post, df_one_hot_encoded], axis=1)

    train, test = train_test_split(post, test_size=0.2, random_state=0)

    train_y=train['label']
    train_x=train.drop(['label'], axis=1)
    train_x=train_x.drop(['url'], axis=1)
    train_x=train_x.drop(['indication_reward_img'], axis=1)
    train_x=train_x.drop(['indication_reward_text'], axis=1)

    test_y=test['label']
    test_x=test.drop(['label'], axis=1)
    test_x=test_x.drop(['url'], axis=1)
    test_x=test_x.drop(['indication_reward_img'], axis=1)
    test_x=test_x.drop(['indication_reward_text'], axis=1)

    # DecisionTree, RandomForest, LogisticRegression을 위한 사이킷런 Classifier 클래스 생성
    dt_clf = DecisionTreeClassifier(random_state=0)
    rf_clf = RandomForestClassifier(random_state=0)
    lr_clf = LogisticRegression()

    # DecisionTreeClassifier 학습/예측/평가
    dt_clf.fit(train_x, train_y)
    dt_pred = dt_clf.predict(test_x)
    print('DecisionTreeClassifier 정확도 : {0:.4f}'.format(accuracy_score(test_y, dt_pred)))

    # RandomForestClassifier 학습/예측/평가
    rf_clf.fit(train_x, train_y)
    rf_pred = rf_clf.predict(test_x)
    print('RandomForestClassifier 정확도 : {0:.4f}'.format(accuracy_score(test_y, rf_pred)))

    # LogisticRegression 학습/예측/평가
    lr_clf.fit(train_x, train_y)
    lr_pred = lr_clf.predict(test_x)
    print('LogisticRegression 정확도 : {0:.4f}'.format(accuracy_score(test_y, lr_pred)))

    #
    # seoul_post = pd.read_csv(seoul_csv)
    # print("데이터 개수 len(post): ", len(seoul_post))
    # # df_one_hot_encoded = pd.get_dummies(seoul_post.url)
    # # seoul_post = pd.concat([seoul_post, df_one_hot_encoded], axis=1)
    # tests = seoul_post
    # test_sl = tests['label']
    # test_s = tests.drop(['label'], axis=1)
    # test_s = test_s.drop(['url'], axis=1)
    # test_s = test_s.drop(['indication_reward_img'], axis=1)
    # test_s = test_s.drop(['indication_reward_text'], axis=1)

    #lr_seoul_clf = LogisticRegression()
    # lr_seoul_pred = lr_clf.predict(test_s)
    # print('LogisticRegression 정확도 : {0:.4f}'.format(accuracy_score(test_sl, lr_seoul_pred)))
    #print(lr_clf.predict_proba(test_s))

    #새로운 파일 입력
    post_s = pd.read_csv(seoul_csv)
    save_pred = post_s
    save_pred = save_pred.drop(['label'], axis=1)
    save_pred = save_pred.drop(['url'], axis=1)
    save_pred = save_pred.drop(['indication_reward_img'], axis=1)
    save_pred = save_pred.drop(['indication_reward_text'], axis=1)

    save_rf = rf_clf.predict_proba(save_pred)
    save_dt = dt_clf.predict_proba(save_pred)
    save_lr = lr_clf.predict_proba(save_pred)
    print(len(save_rf[:,1]))
    print(len(save_dt))
    print(len(save_lr))


    submit = pd.DataFrame({'url': post_s['url'], 'label':post_s['label'],
                           'indication_reward_img':post_s['indication_reward_img'],
                           'indication_reward_text': post_s['indication_reward_text'],
                           'tmi': post_s['tmi'],
                           'use_unique_words': post_s['use_unique_words'],
                           'use_similar_sentences(including_body)': post_s['use_similar_sentences(including_body)'],
                           'use_similar_sentences(without_body)': post_s['use_similar_sentences(without_body)'],
                           'lr_pred': save_lr[:,1],
                           'dt_pred': save_dt[:,1],
                           'rf_pred': save_rf[:,1]})
    submit.to_csv(pred_csv, index=False)
    #
    #
    # joblib.dump(dt_clf, '/Users/sonjung-yeong/Desktop/naver_blog_post/DT_model_with_url.pkl')
    # joblib.dump(rf_clf, '/Users/sonjung-yeong/Desktop/naver_blog_post/RF_model_with_url.pkl')
    # joblib.dump(lr_clf, '/Users/sonjung-yeong/Desktop/naver_blog_post/LR_model_with_url.pkl')







