import json

# read transcript
with open("../dataset/chat.txt","r") as f:
    text = f.read()

print("Transcript Loaded:\n")
print(text)

data = {
    "account_id": "bens_electric",
    "notes": "Extracted from transcript",
    "raw_text": text
}

# save output
with open("../outputs/accounts/bens_electric/v1/extracted.json","w") as f:
    json.dump(data,f,indent=2)

print("\nExtraction Complete!")