def count_bi_grams(text):
    words = text.split()
    bi_grams = [f"{words[i]}_{words[i+1]}" for i in range(len(words)-1)]
    return len(bi_grams)

input_text ="I am Pranjay kumar.I study in B.I.T Patna.Patna is capital of Bihar."

total_bi_grams = count_bi_grams(input_text)
print(f"Total number of bi-grams: {total_bi_grams}")