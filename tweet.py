import csv
null = None
false = False
true = True


def after(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

with open('twitterm.json', 'r') as js:
    with open('tweettext.csv', 'w') as csvfile:
        fieldnames = ['ins', 'tw', 'text', 'location1','location2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for line in js:
            try:

                tweet = eval(line)
                username = tweet[0]["doc"]["user"]["screen_name"]


                location1,location2 = tweet[0]["doc"]["coordinates"]["coordinates"]

                url = tweet[0]["doc"]["user"]["entities"]["url"]["urls"][0]["expanded_url"]

                text = tweet[0]["doc"]["text"]

                if "instagram" in url:
                    ins = after(url, "com/")
                    writer.writerow({'ins': ins, 'tw': username, 'text': text , 'location1': location1, 'location2': location2})








            except Exception as e:

                pass
