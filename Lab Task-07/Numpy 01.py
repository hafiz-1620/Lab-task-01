import Numpy as np # type: ignore
score=np.array([85,90,78,92,88])
score=score.astype('f')
print(score)
print(type(score.dtype))
a_score=score.copy()
print(a_score)
a_score+=5
print(a_score)
print(score)
print(score.shape)
print(score.ndim)
print(score.size)
print(score.itemsize)
print(score.dtype)
print(np.sort(score))
print(np.where(score>80))
print(score.max())
print(score.min())
print(score.sum())
print(score.std())
print(score.var())
print(score.mean())
print(score.mean(axis=0))
print(score[::2])
print(score[-3:-1])
print(score[1:4])
