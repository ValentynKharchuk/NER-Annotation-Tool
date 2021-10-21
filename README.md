# NER-Annotation-Tool
NN based tool for data labeling of ukrainian texts for resolving NER task

### Example of training scripts launch:
```
python model_training.py 
{"model": {"name": "noname","locale": "uk"},"data": [{"node": "subSentence","text": "Кабмін затвердив проєкт постанови","entities": [{"type": "ORGANIZATION","pos": [0,5]},{"type": "LOCATION","pos": [17,22]}]},{"text": " Про це повідомила пресслужба Міністерства фінансів України","entities": [{"type": "ORGANIZATION","pos": [30,58],"nestedIn": ["subSentence"]}]}]}
```

#### Output should be like:
```
{"model": {"name": "noname", "locale": "uk", "losses": [10.799998462200165, 10.571893095970154, 10.275183200836182, 9.596847832202911, 8.726697146892548, 7.802149474620819, 5.9745200872421265, 4.810515910387039, 4.400107033550739, 4.532589679583907, 4.794591702520847, 5.099115784978494, 4.250343264080584, 3.912178149446845, 3.3282315370161086, 5.589973955415189, 3.1999236876145005, 4.499815300107002, 3.49600762873888, 3.226840253919363, 3.0761756766587496, 2.6321781063452363, 2.1561748906970024, 1.9634855100885034, 1.629924092325382, 1.5041019909767783, 1.1774751855555223, 0.9850692263735255, 0.5902386240977648, 0.5561446660158254, 0.3032168019008168, 0.29182885101195666, 0.0905654267687197, 0.027600084950904602, 0.01498246684775495, 0.010298716465285906, 0.002788229277030041, 0.002901617209509766, 0.0013339000946928081, 1.5402350868498615e-05, 5.0265502654411875e-05, 2.1590413240346606e-05, 2.089464632959448e-05, 1.197992786217128e-05, 9.924468358235572e-07, 1.1887809273636307e-06, 5.186940293722131e-06, 7.894115079398745e-07, 4.203730275535722e-06, 5.303997728800525e-07]}, "data": [{"node": "subSentence", "text": "Кабмін затвердив проєкт постанови", "entities": [{"type": "ORGANIZATION", "pos": [0, 5]}, {"type": "LOCATION", "pos": [17, 22]}]}, {"text": " Про це повідомила пресслужба Міністерства фінансів України", "entities": [{"type": "ORGANIZATION", "pos": [30, 58], "nestedIn": ["subSentence"]}]}]}
```

### Example of prediction scripts launch:
```
python model_prediction.py
{"model": {"name": "noname","locale": "uk"},"data": [{"id": "e74ed2e2-ff00-499f-a760-3c516f657169","node": "subSentence","concept":"SYNTAX","text": "Кабмін затвердив проєкт постанови","entities": []},{"id": "6b26ebfb-9350-4e46-912c-d4237424a822","node": "subSentence","concept": "SYNTAX","text": " яка дозволяє в рамках державних зовнішніх запозичень залучити до 21 млн фунтів стерлінгів від Агентства експортного фінансування Сполученого Королівства ","entities": []}]}
```
#### Output should be like:
```
{"model": {"name": "noname", "locale": "uk"}, "data": [{"id": "e74ed2e2-ff00-499f-a760-3c516f657169", "node": "subSentence", "concept": "SYNTAX", "text": "Кабмін затвердив проєкт постанови", "entities": [{"type": "ORGANIZATION", "pos": [0, 5]}, {"type": "LOCATION", "pos": [17, 22]}]}, {"id": "6b26ebfb-9350-4e46-912c-d4237424a822", "node": "subSentence", "concept": "SYNTAX", "text": " яка дозволяє в рамках державних зовнішніх запозичень залучити до 21 млн фунтів стерлінгів від Агентства експортного фінансування Сполученого Королівства ", "entities": [{"type": "ORGANIZATION", "pos": [95, 140]}]}]}
```
### Example of evaluation scripts launch:
```
python model_evaluation.py 
{"model": {"name": "noname","locale": "uk"},"data": [{"node": "subSentence","text": "Кабмін затвердив проєкт постанови","entities": [{"type": "ORGANIZATION","pos": [0,5]},{"type": "LOCATION","pos": [17,22]}]},{"text": " Про це повідомила пресслужба Міністерства фінансів України","entities": [{"type": "ORGANIZATION","pos": [30,58],"nestedIn": ["subSentence"]}]}]}
```
#### Output should be like:
```
{"model": {"name": "noname", "locale": "uk", "metrics": {"ORGANIZATION": {"p": 100.0, "r": 100.0, "f": 100.0}, "LOCATION": {"p": 100.0, "r": 100.0, "f": 100.0}}}, "data": [{"node": "subSentence", "text": "Кабмін затвердив проєкт постанови", "entities": [{"type": "ORGANIZATION", "pos": [0, 5]}, {"type": "LOCATION", "pos": [17, 22]}]}, {"text": " Про це повідомила пресслужба Міністерства фінансів України", "entities": [{"type": "ORGANIZATION", "pos": [30, 58], "nestedIn": ["subSentence"]}]}]}
```
