import csv
import data_filltering
import lr

file_path = ""
# file_name = "submission.csv"

drop_submission_csv = ""
img_label_csv = ""
new_submission_csv = ""
# path_name = file_path + file_name

seoul_submission_csv = ""
seoul_img_label_csv = ""
seoul_new_sub_csv = ""

#data_list = []
data_list1 = []
data_list2 = []
new_sub_list = []

seoul_data_list1 = []
seoul_data_list2 = []

"------lr.lr_run()------"
#서브미션 파일 위치
new_sub_csv = ""
#새롭게 저장하고자 하는 위치
pred_csv = ""
#새로운 테스트 셋
seoul_csv = ""
test_csv = ""



if __name__ == "__main__":
    #이미지 라벨링 및 종합 라벨링 추
    print("Make new submission")
    data_filltering.make_new_sub(["url", "label",
              "indication_reward_img",
              "indication_reward_text",
              "tmi",
              "use_unique_words",
              "use_similar_sentences(including_body)",
              "use_similar_sentences(without_body)"], new_sub_csv)
    print("Write new submission")
    data_filltering.add_file(drop_submission_csv, img_label_csv, data_list1, data_list2, new_sub_list, new_sub_csv)
    #서울 submission2
    data_filltering.make_new_sub(["url", "label",
                                  "indication_reward_img",
                                  "indication_reward_text",
                                  "tmi",
                                  "use_unique_words",
                                  "use_similar_sentences(including_body)",
                                  "use_similar_sentences(without_body)"], seoul_new_sub_csv)
    print("Write new submission")
    data_filltering.add_file(seoul_submission_csv, seoul_img_label_csv, seoul_data_list1, seoul_data_list2, new_sub_list, seoul_new_sub_csv)

    lr.ml_run(new_sub_csv)

