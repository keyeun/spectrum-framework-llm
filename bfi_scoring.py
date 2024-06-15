def bfi_score_to_level(score):
    if 1 <= score < 2:
        return 'very low'
    elif score < 3:
        return 'low'
    elif score < 4:
        return 'slightly below average'
    elif score < 5:
        return 'slightly above average'
    elif score < 6:
        return 'high'
    elif score <= 7:
        return 'very high'
    else:
        return 'out of range'

def bfi_calculate_scores(data):
    data = {key: int(value) for key, value in data.items()}

    bfi_scoring = {
        'Extraversion': {
            'items': ['D1PB-1', 'D1PB-6', 'D1PB-11', 'D1PB-16', 'D1PB-21', 'D1PB-26'],
            'reverse': [True, False, False, False, True, True],
            'facets': {
                'Sociability': ['D1PB-1', 'D1PB-16'],
                'Assertiveness': ['D1PB-6', 'D1PB-21'],
                'Energy Level': ['D1PB-11', 'D1PB-26']
            }
        },
        'Agreeableness': {
            'items': ['D1PB-2', 'D1PB-7', 'D1PB-12', 'D1PB-17', 'D1PB-22', 'D1PB-27'],
            'reverse': [False, True, False, True, False, True],
            'facets': {
                'Compassion': ['D1PB-2', 'D1PB-17'],
                'Respectfulness': ['D1PB-7', 'D1PB-22'],
                'Trust': ['D1PB-12', 'D1PB-27']
            }
        },
        'Conscientiousness': {
            'items': ['D1PB-3', 'D1PB-8', 'D1PB-13', 'D1PB-18', 'D1PB-23', 'D1PB-28'],
            'reverse': [True, True, False, False, False, True],
            'facets': {
                'Organization': ['D1PB-3', 'D1PB-18'],
                'Productiveness': ['D1PB-8', 'D1PB-23'],
                'Responsibility': ['D1PB-13', 'D1PB-28']
            }
        },
        'Negative Emotionality': {
            'items': ['D1PB-4', 'D1PB-9', 'D1PB-14', 'D1PB-19', 'D1PB-24', 'D1PB-29'],
            'reverse': [False, False, True, True, True, False],
            'facets': {
                'Anxiety': ['D1PB-4', 'D1PB-19'],
                'Depression': ['D1PB-9', 'D1PB-24'],
                'Emotional Volatility': ['D1PB-14', 'D1PB-29']
            }
        },
        'Open-Mindedness': {
            'items': ['D1PB-5', 'D1PB-10', 'D1PB-15', 'D1PB-20', 'D1PB-25', 'D1PB-30'],
            'reverse': [False, True, False, True, False, True],
            'facets': {
                'Aesthetic Sensitivity': ['D1PB-5', 'D1PB-20'],
                'Intellectual Curiosity': ['D1PB-10', 'D1PB-25'],
                'Creative Imagination': ['D1PB-15', 'D1PB-30']
            }
        }
    }

    domainSentence = "This character's overall tendency in the domain of ${domain} is ${level}.\n"
    facetSentence = "- This character has a ${level} level of ${facet}.\n"
    bfi_sentences = ''
    for domain, info in bfi_scoring.items():
        domain_score = sum(data[item] if not reverse else 8 - data[item] for item, reverse in zip(info['items'], info['reverse']))
        level = bfi_score_to_level(domain_score // len(info['items']))
        sentence = domainSentence.replace('${domain}', domain).replace('${level}', level)
        bfi_sentences += sentence
        
        for facet, items in info['facets'].items():
            facet_score = sum(data[item] if not bfi_scoring[domain]['reverse'][bfi_scoring[domain]['items'].index(item)] else 8 - data[item] for item in items)
            level = bfi_score_to_level(facet_score // len(items))
            sentence = facetSentence.replace('${facet}', facet).replace('${level}', level)
            bfi_sentences += sentence

    return bfi_sentences