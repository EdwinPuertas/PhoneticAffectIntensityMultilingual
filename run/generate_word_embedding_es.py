
from logic.embedding import Embedding

em = Embedding(lang='es')
'''
em.words_embedding(model_name='word_embedding')
em.plot('word_embedding_es')
em.plot_clusters('word_embedding_es')
'''
em.get_similarity(model_name='word_embedding')