emoji_dict = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}

sentence = input("Please enter a sentence: ")
words = sentence.split()
sentence_changed = []

for element in words:
    if element in emoji_dict:
        sentence_changed.append(emoji_dict[element] + ' ')
    else:
        sentence_changed.append(element + ' ')
        
final_sentence = ''.join(sentence_changed)

print(final_sentence)