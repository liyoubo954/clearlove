import os
import re
import jieba
import jieba.analyse
import pandas as pd
from collections import Counter


def load_stopwords(stopword_path):
    """加载停用词表"""
    stopwords = set()
    if os.path.exists(stopword_path):
        with open(stopword_path, 'r', encoding='utf-8') as f:
            stopwords = set(f.read().splitlines())
    return stopwords


def process_txt_files(input_dir, output_dir, stopword_path):
    """处理TXT文件，分词并去除停用词"""
    os.makedirs(output_dir, exist_ok=True)
    stopwords = load_stopwords(stopword_path)
    global_word_counter = Counter()
    document_word_count = {}

    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            words = jieba.lcut(content, cut_all=False)
            filtered_words = [word for word in words if
                              word not in stopwords and re.match(r'^[\u4e00-\u9fa50-9]+$', word)]

            global_word_counter.update(filtered_words)
            document_word_count[filename] = Counter(filtered_words)

            with open(output_path, 'w', encoding='utf-8') as f_out:
                f_out.write(' '.join(filtered_words))

    return global_word_counter, document_word_count


def compute_tfidf(global_word_counter, document_word_count, output_csv):
    """计算TF-IDF并保存到CSV"""
    total_documents = len(document_word_count)
    word_doc_freq = Counter()

    for doc_words in document_word_count.values():
        for word in doc_words.keys():
            word_doc_freq[word] += 1

    data = []
    for word, total_freq in global_word_counter.items():
        doc_freq = word_doc_freq[word]

        # 避免除零错误
        if doc_freq == 0:
            continue

        avg_tfidf = sum((doc_words[word] / sum(doc_words.values())) * (total_documents / doc_freq)
                        for doc_words in document_word_count.values() if word in doc_words) / total_documents

        data.append([word, total_freq, doc_freq, avg_tfidf])

    df = pd.DataFrame(data, columns=['词名称', '全局词频', '文档频率', '平均TF-IDF'])
    df = df.sort_values(by='平均TF-IDF', ascending=False)
    df.to_csv(output_csv, index=True, index_label='序号', encoding='utf-8-sig')


def main():
    input_dir = "F:\\ddg\\KG\\text"
    output_dir = "F:\\ddg\\KG\\fenci_file"
    stopword_path = "F:\\ddg\\KG\\stopwords.txt"
    output_csv = "F:\\ddg\\KG\\key\\tfidf_results.csv"

    global_word_counter, document_word_count = process_txt_files(input_dir, output_dir, stopword_path)
    compute_tfidf(global_word_counter, document_word_count, output_csv)

    print("处理完成，TF-IDF 结果已保存！")


if __name__ == '__main__':
    main()
