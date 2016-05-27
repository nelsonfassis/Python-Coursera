text = "X-DSPAM-Confidence:    0.8475";
count_start = text.find(":")
print float(text[(count_start + 1):len(text)].strip())