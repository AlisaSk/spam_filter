class BinaryConfusionMatrix:
    def __init__(self, pos_tag, neg_tag):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
         
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0
         
    def as_dict(self):
       return {'tp': self.tp, 'tn': self.tn, 'fp': self.fp, 'fn': self.fn}
     
    def update(self, truth, prediction):
        correct_values = (truth == self.pos_tag or truth == self.neg_tag) and (prediction == self.pos_tag or prediction == self.neg_tag)
        if not(correct_values):
            raise ValueError
             
        if truth == prediction:
            self.tp += 1 if truth == self.pos_tag else 0
            self.tn += 1 if truth == self.neg_tag else 0
             
        else:    
            self.fn += 1 if truth == self.pos_tag else 0
            self.fp += 1 if truth == self.neg_tag else 0
             
    def compute_from_dicts(self, truth_dict, pred_dict):
        for mail in truth_dict.keys():
            self.update(truth_dict[mail], pred_dict[mail])              
         
         
if __name__ == '__main__':
    truth_dict = {'em1': 'SPAM'}
    pred_dict = {'em1': 'OK'}
    cm2 = BinaryConfusionMatrix(pos_tag='SPAM', neg_tag='OK')
    cm2.compute_from_dicts(truth_dict, pred_dict)
    print(cm2.as_dict())
    # {'tp': 1, 'tn': 1, 'fp': 1, 'fn': 1}