
#Importando librer\u237\'edas}

import numpy as np
import pandas as pd

from simpletransformers.ner import NERModel,NERArgs
from sklearn.metrics import accuracy_score
#Convirtiendo los excels a dataframe

def train_model():
	train_data = pd.read_excel("train_data.xlsx")
	test_data = pd.read_excel("test_data.xlsx")
	train_data = train_data.dropna()
	test_data = test_data.dropna()
	train_data["labels"] = train_data["labels"].astype(str)
	train_data["words"] = train_data["words"].astype(str)
	test_data["labels"] = test_data["labels"].astype(str)
	test_data["words"] = test_data["words"].astype(str)
	label = train_data["labels"].unique().tolist()
	args = NERArgs()
	args.num_train_epochs = 200
	args.learning_rate = 1e-4
	args.overwrite_output_dir =True
	args.train_batch_size = 32
	args.eval_batch_size = 32
	model = NERModel('roberta', "roberta-base" ,labels=label, args =args, use_cuda=True)
	model.train_model(train_data,eval_data = test_data,acc=accuracy_score)
	result, model_outputs, preds_list = model.eval_model(test_data)
	print(result)
	prediction, model_output = model.predict(["Amanda P\u233\'e9rez sufri\u243\'f3 un atentado en el corregimiento Villahermosa del municipio del Choc\u243\'f3. Su esposo fue desaparecido y ella actualmente recibe atenci\u243\'f3n psicosocial por parte de Acnur"])
	print(prediction)

train_model()
