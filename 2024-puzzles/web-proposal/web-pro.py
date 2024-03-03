import re
import json

with open('web-proposal.txt', 'r') as file:
    proposal_text = file.read()

sentences = re.split(r'\. ', proposal_text)
sentences = [sentence.strip() for sentence in sentences]
sentences = [sentence for sentence in sentences if sentence]
longest_sentence_without_comma = max((sentence for sentence in sentences if ',' not in sentence), key=len)

shortest_sentence = min(sentences, key=len)

sentence_with_most_commas = max(sentences, key=lambda x: x.count(','))

result = {
  "Longest without comma": longest_sentence_without_comma,
  "Shortest": shortest_sentence,
  "Most Commas": sentence_with_most_commas
}

with open('result.json', 'w') as json_file:
  json.dump(result, json_file, indent=4)
