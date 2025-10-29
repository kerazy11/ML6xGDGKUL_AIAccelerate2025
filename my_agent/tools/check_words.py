import nltk
from nltk.corpus import words

ENGLISH_WORDS = set(w.lower() for w in words.words())


def is_english_word(word: str) -> bool:
    """Check if a single word is valid English."""
    return word.lower() in ENGLISH_WORDS


def all_english(words_list) -> bool:
    """Return True if all words in a list are English."""
    return all(is_english_word(w) for w in words_list)


def split_into_words(s: str):

    result = []
    i = 0
    while i < len(s):
        found = False

        for j in range(len(s), i, -1):
            candidate = s[i:j]
            if candidate in ENGLISH_WORDS:
                result.append(candidate)
                i = j
                found = True
                break
        if not found:

            result.append(s[i:])
            break
    return result


def extract_sentence_from_block(block: str, max_loops: int = 10) -> str:
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    letters = "".join(lines).lower()


    best_result = []
    for loop in range(max_loops):
        words_list = split_into_words(letters)
        if all_english(words_list):
            best_result = words_list
            print(f"All English words found on iteration {loop + 1}")
            break
        else:

            print(f"Iteration {loop + 1}: not all words are English -> {words_list}")

            letters = letters[:-1]  
    else:
        print("Could not find a fully English split.")

    if best_result:
        sentence = " ".join(best_result).capitalize() + "."
        return sentence
    else:
        return "No valid English sentence found."


# Example usage:
block_text = """THESE
AGULL
GLIDE
DPEAC
EFULL
YTOMY
CHAIR"""

result = extract_sentence_from_block(block_text)
print("\nFinal sentence:\n", result)

