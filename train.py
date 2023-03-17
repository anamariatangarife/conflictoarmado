{\rtf1\ansi\deff3\adeflang1025
{\fonttbl{\f0\froman\fprq2\fcharset0 Times New Roman;}{\f1\froman\fprq2\fcharset2 Symbol;}{\f2\fswiss\fprq2\fcharset0 Arial;}{\f3\froman\fprq2\fcharset0 Liberation Serif{\*\falt Times New Roman};}{\f4\fswiss\fprq2\fcharset0 Liberation Sans{\*\falt Arial};}{\f5\froman\fprq2\fcharset0 Helvetica{\*\falt Arial};}{\f6\fnil\fprq2\fcharset0 Noto Sans CJK SC Regular;}{\f7\fnil\fprq2\fcharset0 FreeSans;}{\f8\fswiss\fprq0\fcharset128 FreeSans;}}
{\colortbl;\red0\green0\blue0;\red0\green0\blue255;\red0\green255\blue255;\red0\green255\blue0;\red255\green0\blue255;\red255\green0\blue0;\red255\green255\blue0;\red255\green255\blue255;\red0\green0\blue128;\red0\green128\blue128;\red0\green128\blue0;\red128\green0\blue128;\red128\green0\blue0;\red128\green128\blue0;\red128\green128\blue128;\red192\green192\blue192;}
{\stylesheet{\s0\snext0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033 Normal;}
{\s15\sbasedon0\snext16\sb240\sa120\keepn\dbch\af6\dbch\af7\afs28\loch\f4\fs28 Heading;}
{\s16\sbasedon0\snext16\sl288\slmult1\sb0\sa140 Text Body;}
{\s17\sbasedon16\snext17\sl288\slmult1\sb0\sa140\dbch\af8 List;}
{\s18\sbasedon0\snext18\sb120\sa120\noline\i\dbch\af8\afs24\ai\fs24 Caption;}
{\s19\sbasedon0\snext19\noline\dbch\af8 Index;}
}{\*\generator LibreOffice/5.1.6.2$Linux_X86_64 LibreOffice_project/10m0$Build-2}{\info{\creatim\yr0\mo0\dy0\hr0\min0}{\revtim\yr0\mo0\dy0\hr0\min0}{\printim\yr0\mo0\dy0\hr0\min0}}\deftab560
\viewscale100
{\*\pgdsctbl
{\pgdsc0\pgdscuse451\pgwsxn12240\pghsxn15840\marglsxn1440\margrsxn1440\margtsxn1440\margbsxn1440\pgdscnxt0 Default Style;}}
\formshade{\*\pgdscno0}\paperh15840\paperw12240\margl1440\margr1440\margt1440\margb1440\sectd\sbknone\sectunlocked1\pgndec\pgwsxn12240\pghsxn15840\marglsxn1440\margrsxn1440\margtsxn1440\margbsxn1440\ftnbj\ftnstart1\ftnrstcont\ftnnar\aenddoc\aftnrstcont\aftnstart1\aftnnrlc
{\*\ftnsep}\pgndec\pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
#Importando librer\u237\'edas}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
import numpy as np}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
import pandas as pd}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
from simpletransformers.ner import NERModel,NERArgs}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
from sklearn.metrics import accuracy_score}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
#Convirtiendo los excels a dataframe}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
def train_model():}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab train_data = pd.read_excel("train_data.xlsx")}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab test_data = pd.read_excel("test_data.xlsx")}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Borrando los datos nulos}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab train_data = train_data.dropna()}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab test_data = test_data.dropna()}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Convertir estas columnas a string}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab train_data["labels"] = train_data["labels"].astype(str)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab train_data["words"] = train_data["words"].astype(str)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab test_data["labels"] = test_data["labels"].astype(str)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab test_data["words"] = test_data["words"].astype(str)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Obtengo los labels para utilizarlo como salidas de clasificaci\u243\'f3n}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab label = train_data["labels"].unique().tolist()}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Hiper-parametros del modelo}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab args = NERArgs()}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab args.num_train_epochs = 30}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab args.learning_rate = 1e-4}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab args.overwrite_output_dir =True}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab args.train_batch_size = 32}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab args.eval_batch_size = 32}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Creando el modelo clasificador}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab model = NERModel('roberta', "roberta-base" ,labels=label, args =args, use_cuda=True)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Entrenamos el modelo}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab model.train_model(train_data,eval_data = test_data,acc=accuracy_score)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Obtener los resultados del modelo entrenado}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab result, model_outputs, preds_list = model.eval_model(test_data)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Resultado del modelo entrenado}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab print(result)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab #Pruebas con el modelo}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab prediction, model_output = model.predict(["Amanda P\u233\'e9rez sufri\u243\'f3 un atentado en el corregimiento Villahermosa del municipio del Choc\u243\'f3. Su esposo fue desaparecido y ella actualmente recibe atenci\u243\'f3n psicosocial por parte de Acnur"])}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
\tab print(prediction)}
\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033\cf1\rtlch \ltrch\loch\fs24\loch\f5

\par \pard\plain \s0\nowidctlpar\hyphpar0\cf0\kerning1\dbch\af6\langfe2052\dbch\af7\afs24\alang1081\loch\f3\fs24\lang1033{\cf1\rtlch \ltrch\loch\fs24\loch\f5
train_model()}
\par }