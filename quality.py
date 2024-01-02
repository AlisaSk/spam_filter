import os
import confmat
import utils
def compute_quality_for_corpus(corpus_dir):
    truth_dict = utils.read_classification_from_file(os.path.join(corpus_dir, '!truth.txt'))
    pred_dict = utils.read_classification_from_file(os.path.join(corpus_dir, '!prediction.txt'))
    bcm = confmat.BinaryConfusionMatrix("SPAM", "OK")
    bcm.compute_from_dicts(truth_dict, pred_dict)
    dic = bcm.as_dict()
    return quality_score(dic['tp'], dic['tn'], dic['fp'], dic['fn'])
     
def quality_score(tp, tn, fp, fn):
    quality = (tp + tn) / (tp + tn + 10*fp + fn)
    return quality