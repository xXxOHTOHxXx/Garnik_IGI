import re
import zipfile
from nltk.tokenize import sent_tokenize

def analyze_text(text):
    # Количество предложений в тексте
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)

    # Количество предложений каждого вида
    num_declarative = len([s for s in sentences if s.endswith('.')])
    num_interrogative = len([s for s in sentences if s.endswith('?')])
    num_exclamatory = len([s for s in sentences if s.endswith('!')])

    # Средняя длина предложения в символах
    avg_sentence_length = sum(len(s) for s in sentences) / num_sentences

    # Средняя длина слова в тексте в символах
    words = re.findall(r'\b\w+\b', text)
    avg_word_length = sum(len(w) for w in words) / len(words)

    # Количество смайликов в тексте
    num_smileys = len(re.findall(r'[:;]-*[()\[\]]+', text))

    return {
        'num_sentences': num_sentences,
        'num_declarative': num_declarative,
        'num_interrogative': num_interrogative,
        'num_exclamatory': num_exclamatory,
        'avg_sentence_length': avg_sentence_length,
        'avg_word_length': avg_word_length,
        'num_smileys': num_smileys,
    }

def save_results(results, filename):
    with open(filename, 'w') as f:
        for key, value in results.items():
            f.write(f'{key}: {value}\n')

# Пример использования
text = "Ваш текст здесь. Пожалуйста, замените его на свой текст."
results = analyze_text(text)
save_results(results, 'results.txt')
