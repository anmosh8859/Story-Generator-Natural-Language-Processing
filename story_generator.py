import nltk
import random
from string import punctuation

stopwords_folder = 'stopwords/english'
stopword_set = set()
with open(stopwords_folder, 'r', encoding='utf-8') as file:
    words = file.read().split()
    stopword_set.update(words)

punkt_path = 'tokenizers/punkt'

nltk.data.path.append(punkt_path)

from nltk.tokenize import word_tokenize

# Sample text data (replace this with your text corpus)
text_data = """
In the bustling city of Metropolis, skyscrapers towered above the streets where people hurried about their daily lives. Cars honked, sirens wailed, and the city breathed with a rhythm all its own.

Amidst the urban landscape, a lush park sprawled, adorned with blooming flowers and ancient trees. Children laughed and played while adults found solace in the tranquility of nature amid the concrete jungle.

Venturing beyond the city limits, a serene countryside unfolded. Rolling hills embraced fields of golden wheat, swaying gently in the breeze. Here, farmers toiled, reaping the harvest and tending to their livestock.

Further still, a rugged terrain of mountains and valleys awaited exploration. Majestic peaks kissed the sky while deep ravines hid untold mysteries. Adventurers sought the thrill of scaling cliffs and discovering hidden caverns.

Nearby, an expansive coastline stretched as far as the eye could see. Waves crashed against rocky shores, and sandy beaches beckoned sun-seekers to bask in the warmth of the sun.

In the heart of a dense forest, wildlife thrived in harmony. Squirrels darted among branches, birds sang melodious tunes, and elusive creatures lurked in the shadows.

Across diverse landscapes, cultures intertwined. Festivals celebrated traditions passed down through generations, showcasing music, dance, and art that reflected the richness of humanity.

In laboratories and observatories, scientists and astronomers peered into the depths of the cosmos, unlocking the mysteries of the universe. Their experiments and discoveries propelled civilization forward.

Meanwhile, poets penned verses that captured the essence of love, joy, and sorrow. Their words painted vivid imagery, evoking emotions that resonated with readers across generations.

And in the ever-evolving world of technology, innovation thrived. Engineers and inventors pushed boundaries, creating marvels that shaped the way humans interacted with the world.

From the minutiae of daily routines to the grandeur of natural wonders, this tapestry of experiences wove together the fabric of life, showcasing the vastness and diversity of the human experience.
"""

tokens = word_tokenize(text_data.lower())
tokens = [token for token in tokens if token not in stopword_set and token not in punctuation]

word_pairs = list(nltk.bigrams(tokens))

# Generate Markov chain dictionary
chain_dict = {}
for word1, word2 in word_pairs:
    if word1 in chain_dict.keys():
        chain_dict[word1].append(word2)
    else:
        chain_dict[word1] = [word2]


def generate_story(start_word, length=50):
    story = [start_word]
    for _ in range(length):
        if story[-1] in chain_dict:
            next_word = random.choice(chain_dict[story[-1]])
            story.append(next_word)
        else:
            break
    return ' '.join(story)
