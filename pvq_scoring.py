def pvq_calculate_scores(data):
    pvq_scoring = {
        'Self-Direction': ['D2LP-1', 'D2LP-11'],
        'Power': ['D2LP-2', 'D2LP-17'],
        'Universalism': ['D2LP-3', 'D2LP-8', 'D2LP-19'],
        'Achievement': ['D2LP-4', 'D2LP-13'],
        'Security': ['D2LP-5', 'D2LP-14'],
        'Stimulation': ['D2LP-6', 'D2LP-15'],
        'Conformity': ['D2LP-7', 'D2LP-16'],
        'Tradition': ['D2LP-9', 'D2LP-21'],
        'Hedonism': ['D2LP-10', 'D2LP-22'],
        'Benevolence': ['D2LP-12', 'D2LP-18']
    }
    scores = {}
    for category, items in pvq_scoring.items():
        score = sum(data[item] for item in items) / len(items)
        scores[category] = score
    return scores

def generate_pvq_prompt(data):
    scores = pvq_calculate_scores(data)
    pvq_template = ""
    for key, score in scores.items():
        if 1 <= score <= 2:
            pvq_template += '- {0} is of minimal importance to this character, rarely influencing their decisions or behaviors.\n'.format(key)
        elif score <= 3:
            pvq_template += "- {0} holds some importance but are not primary drivers of this character's actions.\n".format(key)
        elif score <= 4:
            pvq_template += "- This character considers {0} somewhat important, but {0} may not consistently guide this character's daily choices.\n".format(key)
        elif score <= 5:
            pvq_template += "- {0} is important to this character and often influences their decisions and how they interact with the world.\n".format(key)
        elif score <= 6:
            pvq_template += "- This character places a high level of importance on {0}, and {0} significantly influences this character's life choices and behaviors.\n".format(key)
        elif score <= 7:
            pvq_template += "- {0} is of utmost importance and is central to this character's life. {0} guides their actions, decisions, and priorities.\n".format(key)
        else:
            pvq_template += "{0}: Score not in the expected range.\n".format(key)
    return pvq_template