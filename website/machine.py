import pickle
from website.model import TempatWisata

cosine_similiarity = pickle.load(open('website/Content_recomendation.pkl', 'rb'))

def get_recommendation(idx, cosine_similiarity=cosine_similiarity):
    similiarity_score = list(enumerate(cosine_similiarity[idx]))
    similiarity_score = sorted(similiarity_score, key=lambda x: x[1], reverse=True)
    similiarity_score = similiarity_score[1:11]
    place_indices = [i[0] for i in similiarity_score]
    data ={}
    for place in place_indices:
        temp = TempatWisata.query.filter_by(Place_Id=place).first()   
        data[temp.Place_Id] = temp.__repr__()     
    return data