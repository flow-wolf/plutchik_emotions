import json
from collections import defaultdict

recursivedict = lambda: defaultdict(recursivedict)
emotions = recursivedict()
emotions = {
  "happy":{
    "playful":["aroused","cheeky"],
    "content":["free","joyful"],
    "interested":["curious","inquisitive"],
    "proud":["successful","confident"],
    "accepted":["respected","valued"],
    "powerful":["courageous","creative"],
    "peaceful":["loving","thankful"],
    "trusting":["sensitive","intimate"],
    "optimistic":["hopeful","inspired"]
  },
  "surprised":{
    "startled":["shocked","dismayed"],
    "confused":["disillusioned","perplexed"],
    "amazed":["astonished","awe"],
    "excited":["eager","energetic"]
  },
  "bad":{
    "bored":["indifferent","apathetic"],
    "busy":["pressured","rushed"],
    "stressed":["overwhelmed","out of control"],
    "tired":["sleepy","unfocussed"]
  },
  "fearful":{
    "scared":["helpless","frightened"],
    "anxious":["ooverwhelmed","worried"],
    "insecure":["inadequate","inferior"],
    "weak":["worthless","insignificant"],
    "rejected":["excluded","persecuted"],
    "threatened":["nervous","exposed"]
  },
  "angry":{
    "let down":["betrayed","resentful"],
    "humiliated":["disrespected","ridiculed"],
    "bitter":["indignant","vioted"],
    "mad":["furious","jealous"],
    "aggressive":["provoked","hostile"],
    "frustrated":["infuriated","annoyed"],
    "distant":["withdrawn","numb"],
    "critical":["sceptical","dismissive"]
  },
  "disgusted":{
    "dissaproving":["judgemental","embarrassed"],
    "disappointed":["appalled","revolted"],
    "awful":["nauseated","detestable"],
    "repelled":["horrified","hesitant"]
  },
  "sad":{
    "hurt":["embarrassed","dissapointed"],
    "depressed":["inferior","empty"],
    "guilty":["remorseful","ashamed"],
    "despair":["grief","powerless"],
    "vulnerable":["victimised","fragile"],
    "lonely":["isolated","abandoned"]
  }
}

print(json.dumps(emotions,indent=4,sort_keys=True))
